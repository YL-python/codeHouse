import Vue from 'vue'
import App from './App.vue'
import router from './router'
import 'common/css/reset.css';
import "common/stylus/index.styl";

Vue.config.productionTip = false

new Vue({
  router,
  render: h => h(App)
}).$mount('#app')
