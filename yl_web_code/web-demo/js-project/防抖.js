// 防抖是子只有间隔 delay 时间内没有没触发才会执行对应的逻辑
// 第一次使用的时候也会间隔时间才去执行
const debounce = (func, delay = 200) => {
  let timeout = null
  return function () {
    clearTimeout(timeout)
    timeout = setTimeout(() => {
      func.apply(this, arguments)
    }, delay)
  }
}