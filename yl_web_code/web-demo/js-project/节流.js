// 每隔一段时间会执行一次
const throttle = (func, delay = 200) => {
  let prev = +new Date()
  return function(...args) {
    let now = +new Date()
    if (now - prev >= delay) {
      func.apply(this, arguments)
      prev = now
    }
  }
}