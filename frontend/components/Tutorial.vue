<!-- Please remove this file from your project -->
<template>
  <div
    class="
      relative
      flex
      items-top
      justify-center
      min-h-screen
      bg-blue-100
    "
  >
    <div class="w-full mx-auto sm:px-6 lg:px-8">
      <div class="mt-8 bg-white overflow-hidden shadow sm:rounded-lg p-6">
        <div class="space-y-8">
          <div class="block">
            <h2 class="text-2xl leading-7 font-semibold">
              Example Socket.io Integration
            </h2>
          </div>
          <div class="block">
            <button
              v-on:click="getMessage()"
              class="
                bg-blue-500
                hover:bg-blue-700
                text-white
                font-bold
                py-2
                px-4
                rounded
              "
            >
              Get Message
            </button>
            <p>{{ messageRxd }}</p>
          </div>
          <div class="block">
            <p class="font-bold">Socket Status</p>
            <code
              class="
                block
                whitespace-pre
                overflow-scroll
                h-36
                bg-gray-50
                rounded-md
              "
            >
              {{ socketStatus }}
            </code>
          </div>
          <div class="block">
            <p class="font-bold">Event Subscription</p>
            <code
              class="
                block
                whitespace-pre
                overflow-scroll
                h-36
                bg-gray-50
                rounded-md
              "
            >
              <template v-for="r in server_responses.slice().reverse()">
                {{ r }}
              </template>
            </code>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  data() {
    return {
      messageRxd: "",
      socketStatus: {},
      server_responses: [],
    };
  },
  mounted() {
    this.socket = this.$nuxtSocket({
      name: "main",
      reconnection: true,
    });
    // Listen for Events
    this.socket.on("my_response", (msg, cb) => {
      this.server_responses.push(msg);
    });
  },
  methods: {
    getMessage() {
      this.socket.emit(
        "chat_message",
        { param: "Example Parameter" },
        (resp) => {
          this.messageRxd = resp;
        }
      );
    },
  },
};
</script>

