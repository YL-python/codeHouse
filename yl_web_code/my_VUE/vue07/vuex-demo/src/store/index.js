import Vuex from 'vuex'
import Vue from 'vue'

import todolist from './todolistStore'

Vue.use(Vuex)

const store = new Vuex.Store({
  modules:{
    todolist
  }
})

export default store