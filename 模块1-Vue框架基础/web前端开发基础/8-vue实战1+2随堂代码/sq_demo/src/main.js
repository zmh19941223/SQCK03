import Vue from "vue";
import App from "./App.vue";
import router from "./router";
import store from "./store";

import VueParticles from 'vue-particles';
Vue.use(VueParticles);

import ElementUI, { Message } from 'element-ui';
import 'element-ui/lib/theme-chalk/index.css';
Vue.use(ElementUI);

import axios from 'axios';
Vue.prototype.$axios = axios;
axios.defaults.baseURL = "/api";
axios.defaults.withCredentials = true;

import Cookies from 'js-cookie';
Vue.prototype.$cookies = Cookies;

Vue.config.productionTip = false;


router.beforeEach((to, from, next) => {
  document.title = to.meta.title;
  //window.console.log(to.path);
  //window.console.log(from.path);

  const type = to.meta.type;
  if (type === 'login') {
    var isLogin = Cookies.get("isLogin")
    if (isLogin) {
      next();
    } else {
      Message.error("您未登录，请先登录")
      next("/");
    }
  } else {
    next();
  }


});



new Vue({
  router,
  store,
  render: h => h(App)
}).$mount("#app");
