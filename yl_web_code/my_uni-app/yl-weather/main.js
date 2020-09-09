import Vue from 'vue'
import App from './App'

Vue.config.productionTip = false

// 全局挂载 自定义 请求对象
import {
	myRequest
} from './utils/api.js'
Vue.prototype.$myRequest = myRequest

//引入vuex
import store from './store'
//把vuex定义成全局组件
Vue.prototype.$store = store

// 全局的时间过滤器
Vue.filter('formatDate', (dateStr, type) => {
	if (!dateStr) return
	let weekObj = { "0": "星期日", "1": "星期一", "2": "星期二", "3": "星期三", "4": "星期四", "5": "星期五", "6": "星期六" }
	let year = dateStr.slice(0, 4)
	let month = dateStr.slice(4, 6)
	let day = dateStr.slice(6, 8)
	let hours = dateStr.slice(8, 10)
	let minutes = dateStr.slice(10, 12)

	let date = `${year}年${month}月${day}日`;
	let time = `${hours}:${minutes}`;
	let week = weekObj[new Date(`${year}-${month}-${day}`).getDay()]
	switch (type) {
		case "1":
			return date
			break;
		case "2":
			return time
			break;
		case "3":
			return week
			break;
	}
})

App.mpType = 'app'

const app = new Vue({
	...App,
	store
})
app.$mount()
