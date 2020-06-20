import Vue from 'vue'
import VueRouter from 'vue-router'
import artlist from '../components/artlist/artlist.vue'
import recommend from '../components/recommend/recommend.vue'
import search from '../components/search/search.vue'
import toplist from '../components/toplist/toplist.vue'
import mylike from '../components/mylike/mylike.vue'
import playhistory from '../components/playhistory/playhistory.vue'

Vue.use(VueRouter)

const routes = [{
    path: '/',
    redirect: '/recommend'
  },
  {
    path: '/recommend',
    name: 'recommend',
    component: recommend
  },
  {
    path: '/artlist',
    name: 'artlist',
    component: artlist
  },
  {
    path: '/search',
    name: 'search',
    component: search
  },
  {
    path: '/toplist',
    name: 'toplist',
    component: toplist
  },
  {
    path: '/mylike',
    name: 'mylike',
    component: mylike
  },
  {
    path: '/playhistory',
    name: 'playhistory',
    component: playhistory
  }
]

const router = new VueRouter({
  routes
})

export default router