// The Vue build version to load with the `import` command
// (runtime-only or standalone) has been set in webpack.base.conf with an alias.
import { BootstrapVue } from 'bootstrap-vue';
import 'bootstrap/dist/css/bootstrap.css';
import 'bootstrap-vue/dist/bootstrap-vue.css';
import axios from 'axios';
import VueAxios from 'vue-axios';

import Vue from 'vue';
import App from './App';
import router from './router';

Vue.use(BootstrapVue);
Vue.use(VueAxios, axios);

Vue.config.productionTip = false;

/* eslint-disable no-new */
new Vue({
  // el: '#app',
  render: h => h(App),
  router,
  // components: { App },
  // template: '<App/>',
  axios,
}).$mount('#app')
