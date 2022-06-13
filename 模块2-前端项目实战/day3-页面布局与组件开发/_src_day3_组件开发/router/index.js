import { createRouter, createWebHistory } from 'vue-router'
import Home from '../views/Home.vue'
import Haiwen from '../views/Haiwen.vue'
import Afeng from '../views/Afeng.vue'
import Login from '../views/Login.vue'

const routes = [  //路由列表
  {
    path: '/',   // 请求的路径从Host之后开始计算--一级路由
    name: 'Home',  // 路由名称，方便后续引用
    component: Home,  // 组件
    children:[  //子路由，这里的路由组件会显示到当前父组件的router-view中
      {
        path: 'cases', //二级路由这里开头不需要加/
        component: ()=>import("../pages/Cases.vue")
      },{
        path: 'request',
        component: ()=>import("../pages/Request.vue")
      },{
        path: 'plans',
        component: ()=>import("../pages/Plans.vue")
      },{
        path: 'reports',
        component: ()=>import("../pages/Reports.vue")
      }

    ]
  },
  {
    path: '/about',
    name: 'About',
    // route level code-splitting
    // this generates a separate chunk (about.[hash].js) for this route
    // which is lazy-loaded when the route is visited.
    component: () => import(/* webpackChunkName: "about" */ '../views/About.vue')
  },
  {
    path: '/haiwen',
    name: 'haiwen',
    component: Haiwen
  },
  {
    path: '/afeng',
    name: 'afeng',
    component: Afeng
  },
  {
    path: '/login',
    name: 'login',
    component: Login
  },
]
// 创建了router
const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes
})

//全局路由前置守卫，
router.beforeEach((to,from,next)=>{ //回调接收to,from, next
  // console.log('to',to);             // 即将访问的路由
  // console.log('from',from);           // 即将离开的路由
  //可以控制要访问的路由
  if(to.name!=='login' && localStorage.getItem('islogin')!=='yes'){  //如果不访问login页面,且没有登录，就重定向到login
    console.log('未登录')
    next('/login')  
  }else{  
    if(to.name!='login'){
      console.log('已登录')
    }else{
      console.log('未登录')
    }                //直接放行
    next()
  }
})
export default router
