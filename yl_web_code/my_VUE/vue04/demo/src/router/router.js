import Vue from 'vue'
import VueRouter from 'vue-router'
Vue.use(VueRouter)
// 引入相关的文件并且使用

//引入要使用的组件
import son1 from './son1'
import son2 from './son2'
import dtly from './dtly'
import recommend from './recommend'
import index from './index'

// 创建一个路由对象
let router = new VueRouter({
  mode: 'hash', // 'history ',
  routes: [{
      path: '/son1', //地址栏的path 
      name: 'son1',
      component: son1 //组件   如果地址栏变成son1 渲染son1组件
    },
    {
      path: '/son2',
      component: son2
    },
    {
      path: '/dtly/:hehe',// 可以有很多级
      component: dtly  // 动态路由
    },
    {
      path: '/recommend',
      name: 'hehe', // 给路由取一个名字
      component: recommend
    },
    {
      path: '/namerouter',
      name: 'namerouter', // 命名视图
      components: {
        default: son1,
        a: son2,
        b: recommend
      }
    },
    {
      path: '/',
      redirect: '/index' //如果路径是地址栏路径是 / 跳转到 /index
    },
    {
      path: '/index',
      component: index
    }
  ]
})

// 抛出
export default router
