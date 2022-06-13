import Vue from "vue";
import Router from "vue-router";
import Login from "../src/login/Login.vue";
import Index from "../src/index/index.vue";



Vue.use(Router);

export default new Router({
  mode: "history",
  base: process.env.BASE_URL,
  routes: [
    {
      path: "/",
      name: "login",
      component: Login,
      meta: {
        title: "欢迎使用松勤教管系统",
        type: ""
      }
    },
    {
      path: "/about",
      name: "about",
      // route level code-splitting
      // this generates a separate chunk (about.[hash].js) for this route
      // which is lazy-loaded when the route is visited.
      component: () =>
        import("./views/About.vue")
    },
    {
      path: "/index",
      name: "index",
      component: Index,
      meta: {
        title: "欢迎页",
        type: "login"
      },
      children: [
        {
          path: "/home",
          component: resolve => require(["../src/index/home/home"], resolve),
          meta: {
            title: "系统公告",
            type: "login"
          }
        },
        {
          path: "/getLesson",
          component: resolve => require(["../src/index/getLesson/getLesson"], resolve),
          meta: {
            title: "课程查询",
            type: "login"
          }
        }
      ]
    }
  ]
});
