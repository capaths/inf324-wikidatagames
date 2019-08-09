<template>
    <v-layout align-end>
        <v-list dense width="100%">
            <ChatMessage
                    v-for="(value, name, index) in msgs"
                    :sender="value.sender"
                    :content="value.content"
                    :key="index"
            ></ChatMessage>
            <v-textarea
                    v-model="message"
                    auto-grow
                    rows="1"
                    ma-2
                    filled
                    full-width
                    row-height="30"
                    @keydown.enter.prevent="sendMessage"
            ></v-textarea>
        </v-list>
    </v-layout>
</template>

<script>
    import ChatMessage from './ChatMessage';
    import {mapState} from 'vuex';

    export default {
        name: 'Chat',
        data() {
            return {
                message: '',
                msgs: [],
            };
        },
        components: {
            ChatMessage,
        },
        computed: {
            ...mapState('account', ['user']),
        },
        sockets: {
            connect() {
                // console.log('socket connected');
            },
            receiveMessage(data) {
                this.msgs.push(data);
            },
        },
        methods: {
            sendMessage() {
                this.$socket.emit('sendChatMessage', {
                    sender: this.user.username,
                    content: this.message,
                });
                this.message = '';
            },
        },
    };
</script>
