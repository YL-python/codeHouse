import 'babel-polyfill'
// babel-polyfill 解决低版本浏览器对es6不支持问题，需要最先引入
import Vue from 'vue'
import App from './App'
import router from './router'
import fastclick from 'fastclick'
import 'common/stylus/index.styl'
import VueLazyload from 'vue-lazyload'
import store from './store'

Vue.use(VueLazyload, {
  preLoad: 1.3,
  error: require('common/image/default.png'),  // webpack会解析require语法，解析不了ico文件
  loading: '/favicon.ico',  // 引入public目录下文件
  attempt: 1
})

fastclick.attach(document.body)
// 解决移动端点击300ms 延迟问题

Vue.config.productionTip = false

/* eslint-disable no-new */
new Vue({
  el: '#app',
  router,
  store,
  render: h => h(App)
})
