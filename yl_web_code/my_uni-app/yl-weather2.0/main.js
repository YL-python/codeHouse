import Vue from 'vue'
import App from './App'

Vue.config.productionTip = false

App.mpType = 'app'

// 引入全局组件
import divider from "./components/divider.vue"
Vue.component("divider", divider)

//引入vuex
import store from './store'
//把vuex定义成全局组件
Vue.prototype.$store = store

const app = new Vue({
	...App,
	store
})
app.$mount()
