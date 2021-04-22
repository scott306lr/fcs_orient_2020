import Vue from "vue";
import VueRouter from "vue-router";
import Select from "../views/Select.vue";
import Secret from "../views/Secret.vue";
Vue.use(VueRouter);

const routes = [
  {
    path: "/home",
    name: "Home",
    component: () => import(/* webpackChunkName: "home" */ "../views/Home.vue"),
    props: (route) => ({ from: route.query.group }),
  },
  {
    path: "/",
    name: "Select",
    component: Select,
  },
  {
    path: "/score",
    name: "Score",
    component: () =>
      import(/* webpackChunkName: "score" */ "../views/Score.vue"),
    props: (route) => ({ from: route.query.group }),
  },
  {
    path: "/about",
    name: "About",
    component: () =>
      import(/* webpackChunkName: "about" */ "../views/About.vue"),
    props: (route) => ({ from: route.query.group }),
  },
  {
    path: "/secret",
    name: "Secret",
    component: Secret,
  },
];

const router = new VueRouter({
  mode: "history",
  base: process.env.BASE_URL,
  routes,
});

export default router;
