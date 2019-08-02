<template>
    <v-container fluid grid-list-md>
        <v-layout row wrap>
            <v-flex d-flex xs12>
                <v-card>
                    <v-card-title primary class="title">Lorem</v-card-title>
                    <v-card-text>
                        <p>Logged in: {{user.username}}</p>
                        <v-btn @click="logout">Log-out</v-btn>
                    </v-card-text>
                </v-card>
            </v-flex>
        </v-layout>
    </v-container>
</template>

<script>
    import {mapState, mapActions} from 'vuex';

    export default {
        name: "Menu",
        computed: {
            ...mapState("account", ["user"]),
        },
        methods: {
            ...mapActions("account", ["logout"])
        },
    }
</script>

<style scoped>

</style>