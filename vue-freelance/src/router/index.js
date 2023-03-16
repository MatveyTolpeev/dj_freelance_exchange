import Vue from 'vue';
import Router from 'vue-router';
import SignIn from '@/views/auth/SignIn';
import SignUp from '@/views/auth/SignUp';
import VueAxios from "vue-axios";
import axios from "axios";

Vue.use(VueAxios, axios)
Vue.use(BootstrapVue)
Vue.use(router)
Vue.use(Vuelidate)

export default new Router({
  mode: 'history',
  routes: [{
    path: '/auth/signin',
    name: 'SignIn',
    component: SignIn,
  },
  {
    path: '/auth/signup',
    name: 'SignUp',
    component: SignUp,
  },
  ],
});
