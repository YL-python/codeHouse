export default class Event {
  // 事件池 记录所有的相关事件以及对应的函数
  events = {}
  // 添加一个事件对应的处理函数
  on(eventName, fn) {
    if (!this.events[eventName]) {
      this.events[eventName] = []
    }
    if (!this.events[eventName].includes(fn)) {
      !this.events[eventName].push(fn)
    }
  }
  // 删除一个事件对应的处理函数
  off(eventName, fn) {
    if (!this.events[eventName]) {
      return
    }
    this.events[eventName] = this.events[eventName].filters((item) => item != fn)
  }
  dispatch(eventName, ...arg) {
    if (!this.events[eventName]) {
      return
    }
    this.events[eventName].forEach((item) => {
      item.call(this, ...arg)
    })
  }
}