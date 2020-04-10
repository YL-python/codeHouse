import Vue from 'vue'
import App from './App.vue'
import router from './router'
import './style/reset.css'
import axios from './utils/axios'

Vue.prototype.$axios = axios
Vue.config.productionTip = false // 吧axios挂载到原型上，形成一个全局变量

new Vue({
  router,
  render: h => h(App)
}).$mount('#app')
