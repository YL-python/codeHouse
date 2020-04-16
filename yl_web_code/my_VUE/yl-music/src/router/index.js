import Vue from 'vue'
import VueRouter from 'vue-router'

import Recommend from '../components/Recommend/index.vue'
// singer 包里面有两个index文件
import Singer from '../components/Singer/index.vue'
import My from '../components/My/index.vue'
import Rank from '../components/Rank/index.vue'
import Detail from '../components/Detail/index.vue'

Vue.use(VueRouter)

const routes = [{
  path: '/recommend',
  component: Recommend
},
{
  path: '/singer',
  component: Singer,
  children: [
    {
      path: ':singermid',
      component: Detail
    }
  ]
},
{
  path: '/my',
  component: My
},
{
  path: '/rank',
  component: Rank
},
{
  path: '/',
  redirect: '/recommend'
}]

const router = new VueRouter({
  routes
})

export default router
