import Vue from 'vue'
import App from './App.vue'
import router from './router'
import './style/reset.css'
import axios from './utils/axios'
import VueLazyload from 'vue-lazyload'

// 吧axios挂载到原型上，形成一个全局变量
Vue.prototype.$axios = axios
Vue.config.productionTip = false

// 图片懒加载
Vue.use(VueLazyload, {
  preLoad: 1.3,
  error: '/favicon.ico',
  loading: '/favicon.ico',
  attempt: 1
})

new Vue({
  router,
  render: h => h(App)
}).$mount('#app')
