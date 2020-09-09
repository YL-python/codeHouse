import Vue from 'vue'
import Vuex from 'vuex'
Vue.use(Vuex)

const store = new Vuex.Store({
	state: {
		// state中记录两个对象，一个是系统获取的当前位置，一个是用户收藏的位置列表
		nowLocation: {},
		LocationList: []
	},
	mutations: {
		setNowLocation(state, location) {
			// console.log(state, location);
			state.nowLocation = location
			// console.log(state);
		},
		setLocationList(state, location) {
			state.LocationList = location
		}
	},
	actions: {
		// 传过来一个 location 对象存到本地缓存中
		saveLocationList({
			commit
		}, location) {
			commit("setLocationList", saveLocation(location))
		},
		// 传一个 location对象 存到本地缓存中
		deleteLocationList({
			commit
		}, location) {
			commit("setLocationList", deleteLocation(location))
		}
	}
})
export default store
