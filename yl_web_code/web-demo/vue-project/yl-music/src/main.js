import 'babel-polyfill'
// babel-polyfill 解决低版本浏览器对es6不支持问题，需要最先引入
import Vue from 'vue'
import App from './App'
import router from './router'
import fastclick from 'fastclick'

import 'common/stylus/index.styl'
fastclick.attach(document.body)
// 解决移动端点击300ms 延迟问题

Vue.config.productionTip = false

/* eslint-disable no-new */
new Vue({
  el: '#app',
  router,
  render: h => h(App)
})
