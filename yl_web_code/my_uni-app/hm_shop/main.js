import Vue from 'vue'
import App from './App'

// 全局挂载 自定义 请求对象
import {
	myRequest
} from './utils/api.js'
Vue.prototype.$myRequest = myRequest

// 全局的时间过滤器
Vue.filter('formatDate', (date) => {
	let ndate = new Date(date)
	let year = ndate.getFullYear()
	let month = ndate.getMonth().toString().padStart(2, 0)
	let day = ndate.getDate().toString().padStart(2, 0)
	return `${year}-${month}-${day}`
})

Vue.config.productionTip = false

App.mpType = 'app'

const app = new Vue({
	...App
})
app.$mount()
