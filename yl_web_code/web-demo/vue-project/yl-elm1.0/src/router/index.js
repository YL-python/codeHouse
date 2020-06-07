import Vue from 'vue'
import VueRouter from 'vue-router'

const goods = () => import(/* webpackChunkName: "elm-1.0" */ 'views/goods/goods.vue')
const ratings = () => import(/* webpackChunkName: "elm-1.0" */ 'views/ratings/ratings.vue')
const seller = () => import(/* webpackChunkName: "elm-1.0" */ 'views/seller/seller.vue')

Vue.use(VueRouter)

const routes = [{
    path: '/goods',
    name: 'goods',
    component: goods
  },
  {
    path: '/ratings',
    name: 'ratings',
    component: ratings
  },
  {
    path: '/seller',
    name: 'seller',
    component: seller
  },
  {
    path: '/',
    redirect: '/goods'
  }
]

const router = new VueRouter({
  routes,
  linkActiveClass: "active",
  linkExactActiveClass: "active"
})

export default router