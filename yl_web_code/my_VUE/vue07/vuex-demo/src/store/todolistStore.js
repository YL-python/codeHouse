const todolist = {
  namespaced: true,
  state: {
    list: [{
      msg: '明天看笔记',
      finish: true
    }, {
      msg: '明天看敲代码',
      finish: false
    }],
    all: 0 // 0 全部 1 已完成 2 未完成
  },
  mutations: {
    addList(state, params) {
      // console.log("addList:",params);
      state.list.push({
        msg: params.msg,
        finish: false
      })
    },
    delList(state, index) {
      // console.log("delList:",index);
      state.list.splice(index, 1)
    },
    finishList(state, index) {
      state.list[index].finish = true
    },
    changeAll(state, code) {
      state.all = code
    }
  },
  actions: {},
  getters: {
    showList(state) {
      let res = null
      switch (state.all) {
        case 1:
          res = state.list.filter((item) => {
            return item.finish == true
          })
          break;
        case 2:
          res = state.list.filter((item) => {
            return item.finish == false
          })
          break;
        default:
          res = state.list
          break;
      }
      return res
    }
  }
}

export default todolist