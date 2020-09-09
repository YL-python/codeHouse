import Vue from 'vue'
import App from './App'

Vue.config.productionTip = false

App.mpType = 'app'

// 引入全局组件
import divider from "./components/common/divider.vue"
Vue.component("divider", divider)
import loadMore from "./components/common/load-more.vue"
Vue.component("loadMore", loadMore)
import noThing from "./components/common/no-thing.vue"
Vue.component("noThing", noThing)

const app = new Vue({
	...App
})
app.$mount()
