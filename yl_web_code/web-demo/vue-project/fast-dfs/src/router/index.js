import Vue from 'vue'
import VueRouter from 'vue-router'

Vue.use(VueRouter)

const routes = [{
  path: '/',
  redirect: "/login",
}, {
  name: 'login',
  path: '/login',
  component: () => import('@/views/login/login'),
}, {
  name: 'register',
  path: '/register',
  component: () => import('@/views/register/register'),
}, {
  name: 'index',
  path: '/index',
  component: () => import('@/views/index'),
  children: [{
    path: '/index',
    redirect: 'fileall/list'
  }, {
    path: 'fileall/list',
    component: () => import('@/views/fileall/index.vue')
  }, {
    path: 'fileall/card',
    component: () => import('@/views/fileall/index_card.vue')
  }]
}]

const router = new VueRouter({
  routes
})

// 路由白名单 在白名单内的不需要登陆即可访问
// const whiteList = ['/login', '/register']

// router.beforeEach((to, from, next) => {
//   // 全局前置路由

//   // 白名单内的不需要任何权限就能访问
//   if (whiteList.indexOf(to.path) !== -1) {
//     // if is logged in, redirect to the home page
//     next()
//   } else {
//     // 需要权限才能访问的页面
//     // 检查权限
//     if (whiteList.length ? 0 : 0) {
//       next()
//     } else {
//       // 权限不足
//       next({
//         "name": "login"
//       })
//     }
//   }
// })

export default router