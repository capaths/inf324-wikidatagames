import Vue from 'vue';
import App from './App.vue';
import router from './router';
import vuetify from './plugins/vuetify';

import Vuex from 'vuex';
import VueSocketIO from 'vue-socket.io';
import {store} from './_store';

Vue.config.productionTip = false;
Vue.use(Vuex);

Vue.use(new VueSocketIO({
    debug: true,
    connection: 'http://localhost:8080/',
    vuex: {
      store,
      actionPrefix: 'SOCKET_',
      mutationPrefix: 'SOCKET_',
    },
  }),
);


new Vue({
    store,
    router,
    vuetify,
    render: (h) => h(App),
}).$mount('#app');
