/* 深拷贝一个对象
 *
 * |Name  |Desc              |
 * |------|------------------|
 * |obj   |需要拷贝的对象      |
 * |cache |防止死循环的缓存数组|
 */
function deepCopy(obj, cache = []) {
  if (obj === null || typeof obj !== 'object') {
    return obj
  }
  if (obj instanceof RegExp) return new RegExp(obj);
  if (obj instanceof Date) return new Date(obj);

  const hit = find(cache, c => c.original === obj)
  if (hit) {
    return hit.copy
  }

  const copy = Array.isArray(obj) ? [] : {}

  cache.push({
    original: obj,
    copy
  })

  Object.keys(obj).forEach(key => {
    copy[key] = deepCopy(obj[key], cache)
  })

  return copy
}


/* 防抖函数
 *
 * |Name  |Desc              |
 * |------|------------------|
 * |func  |实际要执行的函数    |
 * |delay |防抖间隔时间       |
 */
function debounce(func, delay = 200) {
  let timeout = null
  return function () {
    clearTimeout(timeout)
    timeout = setTimeout(() => {
      func.apply(this, arguments)
    }, delay)
  }
}


/* 节流函数
 *
 * |Name  |Desc              |
 * |------|------------------|
 * |func  |实际要执行的函数    |
 * |delay |节流时间           |
 */
function throttle(func, delay = 200) {
  let prev = +new Date()
  return function (...args) {
    let now = +new Date()
    if (now - prev >= delay) {
      func.apply(this, arguments)
      prev = now
    }
  }
}


/* 区间随机函数
 *
 * |Name     |Desc            |
 * |---------|----------------|
 * |min      |最小值           |
 * |max      |最大值           |
 * |floating |是否返回浮点数    |
 */
function random(min, max, floating) {
  if (max == null) {
    max = min;
    min = 0;
  }

  const rand = Math.random();

  if (floating || min % 1 || max % 1) {
    return Math.min(
      min +
      rand *
      (max - min + parseFloat('1e-' + ((rand + '').length - 1))),
      max
    );
  }

  return min + Math.floor(rand * (max - min + 1));
};


/* 打乱一个数组
 *
 * |Name     |Desc            |
 * |---------|----------------|
 * |arr      |要打乱的数组     |
 */
function shuffle(arr) {
  let cloneArr = arr.slice()
  let len = cloneArr.length
  for (let i = 0; i < len; i++) {
    let j = Math.floor(Math.random * len)
    let t = cloneArr[i]
    cloneArr[i] = cloneArr[j]
    cloneArr[j] = t
  }
  return cloneArr
}