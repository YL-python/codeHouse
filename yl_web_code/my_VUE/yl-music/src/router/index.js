import Vue from 'vue'
import VueRouter from 'vue-router'

import Recommend from '../components/Recommend/index.vue'
import Singer from '../components/Singer/index.vue'
import My from '../components/My/index.vue'
import Rank from '../components/Rank/index.vue'

Vue.use(VueRouter)

const routes = [{
  path: '/recommend',
  component: Recommend
},
{
  path: '/singer',
  component: Singer
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
