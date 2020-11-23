export default class Map {
  // 传参 元素和比例
  constructor(el, rect) {
    this.el = el
    this.rect = rect
    // 计算每行列多少个
    this.rows = Math.ceil(Map.getStyle(el, 'height') / rect)
    this.cells = Math.ceil(Map.getStyle(el, 'width') / rect)
    // 修复小细节
    Map.setStyle(el, 'height', rect * this.rows)
    Map.setStyle(el, 'width', rect * this.cells)
    this.data = []
  }
  static getStyle(el, attr) {
    return parseFloat(getComputedStyle(el)[attr])
  }
  static setStyle(el, attr, val) {
    el.style[attr] = val
  }
  // 向data中添加数据
  setData(newData) {
    this.data = this.data.concat(newData)
  }
  // 清空data
  clearData() {
    this.data.length = 0
  }
  // 判断data中是否包含
  include({ x, y }) {
    return !!this.data.some((item) => item.x == x && item.y == y)
  }
  // 渲染
  rander() {
    this.el.innerHTML = this.data
      .map((item) => {
        return `<span
          style="position:absolute;
          left:${item.x * this.rect}px;top:${item.y * this.rect}px;
          width:${this.rect}px;height:${this.rect}px;
          background:${item.color};"></span>`
      })
      .join('')
  }
}