import "@babel/polyfill";
import "mutationobserver-shim";
import Vue from "vue";
import "./plugins/bootstrap-vue";
import App from "./App.vue";
import router from "./router";
import store from "./store";
import axios from "axios";
import VueAxios from "vue-axios";

Vue.use(VueAxios, axios);
Vue.config.productionTip = false;

var vueAwesomeCountdown = require("vue-awesome-countdown").default;
Vue.use(vueAwesomeCountdown);

new Vue({
  router,
  store,
  render: (h) => h(App),
}).$mount("#app");
