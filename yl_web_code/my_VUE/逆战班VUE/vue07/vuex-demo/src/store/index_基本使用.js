import Vuex from 'vuex'
import Vue from 'vue'
Vue.use(Vuex)

// 创建全局状态管理实例
const store = new Vuex.Store({
  // 存放全局状态值，在所有组件内可以使用
  state: {
    name: '韩梅梅',
    age: 16
  },
  // 修改全局状态值
  mutations: {
    changeName(state, params) {
      console.log('mutations changeName 方法', state, params);
      // 修改 state的数据
      state.name = params.name
    },
    changeAge(state, params) {
      console.log('mutations changeAge 方法', state, params);
      state.age = params.age
    }
  },
  actions: {
    changeAge(content, params) {
      console.log('actions changeAge 方法', content, params);
      content.commit('changeAge', params)
    }
  },
  // vuex 的计算属性
  getters: {
    double(state) {
      return state.age * 2;
    }
  }
})

export default store