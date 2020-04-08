import Vue from 'vue'
import App from './App.vue' // 引入一个单文件组件
import router from './router/router'

Vue.config.productionTip = false

new Vue({ // 创建一个实例
  router:router, //注册路由
  render: h => h(App)  // 渲染app组件
}).$mount('#app') // 关联页面中的app div
