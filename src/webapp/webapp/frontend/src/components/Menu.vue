<template>
    <v-container fluid grid-list-md :fill-height="true" pa-0 ma-0>
        <v-layout row wrap>
            <v-flex d-flex md2 xs4 pa-0>
                <Profile></Profile>
            </v-flex>
            <v-flex d-flex md10 xs8 pa-0>
                <PlayerList></PlayerList>
            </v-flex>
        </v-layout>
    </v-container>
</template>

<script>
    import Profile from './menu/Profile';
    import PlayerList from './menu/PlayerList';

    export default {
        name: 'Menu',
        components: {
            Profile,
            PlayerList,
        },
    };
</script>

<style scoped>

</style>