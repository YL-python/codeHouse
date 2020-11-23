export default class Food {
  constructor(cells, rows, colors = ['red', 'yellow', 'blue', 'pink']) {
    this.cells = cells
    this.rows = rows
    this.colors = colors
    this.data = {}
  }
  // 随机创建一个食物
  create() {
    let x = Math.floor(Math.random() * this.cells)
    let y = Math.floor(Math.random() * this.rows)
    let color = this.colors[parseInt(Math.random() * this.colors.length)]
    this.data = { x, y, color }
  }
}