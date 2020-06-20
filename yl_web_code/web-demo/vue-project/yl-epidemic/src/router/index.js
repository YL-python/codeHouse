import Vue from 'vue'
import VueRouter from 'vue-router'
const domestic = () => import( /* webpackChunkName: "group-app" */ '../views/domestic/domestic.vue')
const foreign = () => import( /* webpackChunkName: "group-app" */ '../views/foreign/foreign.vue')
const information = () => import( /* webpackChunkName: "group-app" */ '../views/information/information.vue')

Vue.use(VueRouter)

const routes = [{
    path: '/domestic',
    name: 'domestic',
    component: domestic,
    props: (route) => ({
      query: route.query.showMap
    })
  },
  {
    path: '/foreign',
    name: 'foreign',
    component: foreign
  },
  {
    path: '/information',
    name: 'information',
    component: information
  },
  {
    path: '/',
    redirect: '/domestic?showMap=china'
  }
]

const router = new VueRouter({
  routes
})

export default router