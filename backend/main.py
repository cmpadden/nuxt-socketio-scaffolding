from aiohttp import web
import socketio
import logging

sio = socketio.AsyncServer(cors_allowed_origins='*')
app = web.Application()
sio.attach(app)
background_task_started = False

logging.basicConfig(level=logging.INFO)


async def background_task():
    """Example of how to send server generated events to clients."""
    count = 0
    while True:
        logging.info("background task: %s", count)
        await sio.sleep(3)
        count += 1
        await sio.emit(
            'my_response', {
                'data': 'Server generated event',
                'count': count
            }
        )


@sio.event
async def connect(sid, environ):
    logging.info("connect: %s", sid)
    global background_task_started
    if not background_task_started:
        sio.start_background_task(background_task)
        background_task_started = True
    await sio.emit('my_response', { 'data': 'Connected', 'count': 0 }, room=sid)


@sio.event
async def chat_message(sid, data):
    logging.info("message: %s, %s", sid, data)
    return "OK"


@sio.event
def disconnect(sid):
    logging.info('disconnect: %s', sid)


if __name__ == '__main__':
    web.run_app(app, port=5000)
