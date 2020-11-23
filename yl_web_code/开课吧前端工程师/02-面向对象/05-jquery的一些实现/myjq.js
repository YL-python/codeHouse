class Jq {
  constructor(arg, root) {
    // 保存上一次操作的节点
    if (typeof root === 'undefined') {
      this.prevObject = [document]
    } else {
      this.prevObject = root
    }

    // 根据不同的参数干不同的事情
    if (typeof arg === 'function') { // 传入方法需要等浏览器渲染完成在执行
      this.ready(arg)
    } else if (typeof arg === 'string') { // 传入选择器
      let ele = document.querySelectorAll(arg)
      // 获取到的节点直接挂到 this 上
      this.addElement(ele)
    } else { // 传入原生节点需要转成jq对象
      this.addElement(arg)
    }
  }

  // 原生节点绑定到jq对象上
  addElement(arg) {
    if (typeof arg.length === 'undefined') {
      this[0] = arg
      this.length = 1
    } else {
      arg.forEach((e, i) => {
        this[i] = e
      })
      this.length = arg.length
    }
  }

  // 实现链式操作
  eq(index) {
    // return $(this[index])
    // this 指向的就是上一次操作的节点
    return new Jq(this[index], this)
  }

  // 浏览器渲染完成执行函数
  ready(arg) {
    window.addEventListener('DOMContentLoaded', arg, false)
  }

  // jq绑定点击方法
  click(fn) {
    for (let i = 0; i < this.length; i++) {
      this[i].addEventListener('click', fn, false)
    }
  }
  get(index) {
    return this[index];
  }
  // 返回上一次操作的对象
  end() {
    return this.prevObject
  }

  // on绑定事件需要有简单的错误处理
  on(eventName, fn) {
    let reg = /\s+/g
    eventName.replace(reg, ' ')
    let eventArr = eventName.split(' ')
    // 绑定事件
    for (let i = 0; i < this.length; i++) {
      for (let j = 0; j < eventArr.length; j++) {
        this[i].addEventListener(eventArr[j], fn, false)
      }
    }
  }

  // css 操作
  css(...arg) {
    if (arg.length === 1) {
      if (typeof arg[0] === 'string') { // 一个参数 获取值
        if (arg[0] in cssHooks) {
          return $.cssHooks[arg[0]].get(this[0])
        } else {
          return this.getStyle(this[0], arg[0])
        }
      } else { // 一个参数根据对象设置值
        for (let i = 0; i < this.length; i++) {
          for (let j in arg[0]) {
            this.setStyle(this[i], j, arg[0][j])
          }
        }
      }
    } else { // 二个参数设置值
      for (let i = 0; i < this.length; i++) {
        this.setStyle(this[i], arg[0], arg[1])
      }
    }
    // 实现CSS的链式操作 
    return this;
  }
  // 根据元素属性设置css值
  setStyle(ele, styleName, styleValue) {
    if (typeof styleValue === 'Number' && !(styleName in $.cssNumber)) {
      styleValue = styleValue + 'px'
    }

    if (styleName in $.cssHooks) {
      $.cssHooks.set(styleName, styleValue)
    } else {
      ele.style[styleName] = styleValue
    }
  }
  // 根据元素属性获取css值
  getStyle(ele, styleName) {
    return window.getComputedStyle(ele, null)[styleName]
  }
}


function $(arg) {
  return new Jq(arg)
}

$.cssNumber = {
  animationIterationCount: true,
  columnCount: true,
  fillOpacity: true,
  flexGrow: true,
  flexShrink: true,
  fontWeight: true,
  gridArea: true,
  gridColumn: true,
  gridColumnEnd: true,
  gridColumnStart: true,
  gridRow: true,
  gridRowEnd: true,
  gridRowStart: true,
  lineHeight: true,
  opacity: true,
  order: true,
  orphans: true,
  widows: true,
  zIndex: true,
  zoom: true,
}

// cssHooks
$.cssHooks = {}