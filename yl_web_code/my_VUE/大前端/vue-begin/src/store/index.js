import Vue from 'vue'
import Vuex from 'vuex'

Vue.use(Vuex)

export default new Vuex.Store({
  state: {
    lists: []
  },
  mutations: {
    setList(state, value) {
      state.lists = value
    }
  },
  actions: {},
  modules: {}
})
