import Vuex from 'vuex'
import Vue from 'vue'
Vue.use(Vuex)

const moduleA = {
  namespaced:true,
  state: {
    name: '韩梅梅'
  },
  mutations: {
    changeName(state, params) {
      state.name = params.name
    }
  },
  actions: {},
  getters: {}
}

const moduleB = {
  state: {
    age: 16
  },
  mutations: {
    changeAge(state, params) {
      state.age = params.age
    }
  },
  actions: {},
  getters: {}
}

const store = new Vuex.Store({
  modules:{
    hehe:moduleA,
    xixi:moduleB
  }
})

export default store