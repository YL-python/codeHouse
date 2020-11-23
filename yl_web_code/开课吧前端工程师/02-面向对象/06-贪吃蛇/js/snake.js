export default class Snake {
  constructor() {
    this.data = [
      { x: 5, y: 2, color: 'green' },
      { x: 4, y: 2, color: 'white' },
      { x: 3, y: 2, color: 'white' },
      { x: 2, y: 2, color: 'white' },
    ]
    // 当前方向
    this.direction = 'right'
    this.lastData = {}
  }
  move() {
    let lastIndex = this.data.length - 1
    this.lastData = {
      x: this.data[lastIndex].x,
      y: this.data[lastIndex].y,
      color: this.data[lastIndex].color,
    }
    // 让最后一格走到第一格上
    for (let i = this.data.length - 1; i > 0; i--) {
      this.data[i].x = this.data[i - 1].x
      this.data[i].y = this.data[i - 1].y
    }
    switch (this.direction) {
      case 'left':
        this.data[0].x--
        break
      case 'right':
        this.data[0].x++
        break
      case 'top':
        this.data[0].y--
        break
      case 'bottom':
        this.data[0].y++
        break
    }
  }
  changeDir(dir) {
    // 上下走的时候能左右调转方向
    if (this.direction === 'left' || this.direction === 'right') {
      if (dir === 'left' || dir === 'right') {
        return false
      }
    } else {
      // 左右走的时候能上下调转方向
      if (dir === 'top' || dir === 'bottom') {
        return false
      }
    }
    this.direction = dir
    return true
  }
  // 吃食物蛇加长
  eatFood() {
    this.data.push(this.lastData)
  }
}