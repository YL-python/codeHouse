import Vue from 'vue'
import App from './App.vue'

Vue.config.productionTip = false

// 全局注册组件
import hehe from './hehe/index.js'
Vue.use(hehe)

new Vue({
  render: h => h(App),
}).$mount('#app')