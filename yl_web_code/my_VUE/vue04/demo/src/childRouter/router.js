import Vue from 'vue'
import VueRouter from 'vue-router'
Vue.use(VueRouter)

// 引入组件
import Recommend from './recommend'
import Singer from "./singer"
import My from "./my"
import UserInfo from "./userInfo.vue"
import UserLogin from "./userLogin.vue"

let router = new VueRouter({
  mode: 'hash',
  routes: [{
      path: '/recommend',
      component: Recommend
    },
    {
      path: '/singer',
      component: Singer,
      beforeEnter: (to, from, next) => {
        // 路由独享守卫
        console.log('歌手守卫')
        next()
      }
    },
    {
      path: '/my',
      component: My,
      children: [{ //  /斜杠表示是根路径，子路由里面不能加斜杠
          path: 'userinfo',
          component: UserInfo
        },
        {
          path: 'userlogin',
          component: UserLogin
        }
      ]
    },
    {
      path: '/',
      redirect: '/recommend'
    }
  ]
})

// 全局前置守卫 所有的路由切换都会触发
// router.beforeEach((to, from, next) => {
//   console.log('from',from)
//   console.log("to",to)
//   let islogin = false 
//   if(to.path==='/singer'){
//     if(islogin){
//       next()
//     }else{
//       next('/my/userlogin')
//     }
//   }else{
//     next()
//   }
// })
//全局后置守卫 跳转完成之后触发
router.afterEach((to, from) => {
  console.log('from',from)
  console.log("to",to)
})

export default router
