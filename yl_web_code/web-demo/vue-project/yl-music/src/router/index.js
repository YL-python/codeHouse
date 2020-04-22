import Vue from 'vue'
import Router from 'vue-router'

import Rank from 'components/rank/rank'
import Recommend from 'components/recommend/recommend'
import Singer from 'components/singer/singer'
import Search from 'components/search/search'
import SingerDetail from 'components/singer-detail/singer-detail'
import Disc from 'components/disc/disc'
import topList from 'components/top-list/top-list'

Vue.use(Router)

export default new Router({
  routes: [{
      path: '/rank',
      component: Rank,
      children: [{
        path: ':id',
        component: topList,
      }]
    }, {
      path: '/recommend',
      component: Recommend,
      children: [{
        path: ':id',
        component: Disc,
      }]
    },
    {
      path: '/singer',
      component: Singer,
      children: [{
        path: ':id',
        component: SingerDetail,
      }]
    },
    {
      path: '/search',
      component: Search
    },
    {
      path: '/',
      redirect: '/recommend'
    }
  ]
})