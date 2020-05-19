import Vuex from 'vuex'
import Vue from 'vue'
Vue.use(Vuex)

const store = new Vuex.Store({
  state: {
    name: '韩梅梅',
    age:16
  },
  mutations: {
    changeName(state,params){
      state.name = params.name
    },
    changeAge(state,params){
      state.age = params.age
    }
  }
})

export default store