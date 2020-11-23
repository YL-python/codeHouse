// game 处理游戏逻辑
import Map from './map.js'
import Event from './event.js'
import Snake from './snake.js'
import Food from './food.js'

export default class Game extends Event {
  constructor(el, rect) {
    super()
    this.map = new Map(el, rect)
    // 创建蛇
    this.snake = new Snake()
    this.map.setData(this.snake.data)
    // 创建食物
    this.food = new Food(this.map.cells, this.map.rows)
    this.createFood()
    this.rander()
    this.timer = null
    this.interval = 200
    this.keyDown = this.keyDown.bind(this)
    this.grade = 0 // 分数
    // 执行绑定事件函数
    this.control()
  }
  // 创建食物
  createFood() {
    this.food.create()
    if (this.map.include(this.food.data)) {
      this.createFood()
    }
  }
  // 开始游戏
  start() {
    this.move()
  }
  // 暂停游戏
  stop() {
    clearInterval(this.timer)
  }
  // 渲染数据
  rander() {
    this.map.clearData()
    this.map.setData(this.snake.data)
    this.map.setData(this.food.data)
    this.map.rander()
  }
  // 控制移动
  move() {
    this.stop()
    this.timer = setInterval(() => {
      this.snake.move()
      if (this.isEat()) {
        this.stop()
        this.snake.eatFood()
        this.createFood()
        this.grade++
        this.changeGrade(this.grade)
        this.interval *= 0.95
        if (this.grade > 20) {
          this.over(1)
          return
        }
        this.start()
      }
      if (this.isOver()) {
        this.over(0)
        return
      }
      this.rander()
    }, this.interval)
  }
  // 判断是否吃到食物
  isEat() {
    return this.snake.data[0].x === this.food.data.x && this.snake.data[0].y === this.food.data.y
  }
  // 判断是否结束游戏
  isOver() {
    // 判断 蛇出地图
    // console.log(this.snake.data)
    if (
      this.snake.data[0].x < 0 ||
      this.snake.data[0].x >= this.map.cells ||
      this.snake.data[0].y < 0 ||
      this.snake.data[0].y >= this.map.rows
    ) {
      return true
    }
    // 判断蛇撞到自己
    for (let i = 1; i < this.snake.data.length; i++) {
      if (this.snake.data[0].x === this.snake.data[i].x && this.snake.data[0].y === this.snake.data[i].y) {
        return true
      }
    }
    return false
  }
  // 结束游戏
  over(overState) {
    if (overState) {
      this.dispatch('win', grade)
    } else {
      this.dispatch('over', grade)
    }
    this.stop()
  }
  keyDown(e) {
    let keyCode = e.keyCode
    switch (keyCode) {
      case 38:
      case 87:
        this.snake.changeDir('top')
        break
      case 40:
      case 83:
        this.snake.changeDir('bottom')
        break
      case 37:
      case 65:
        this.snake.changeDir('left')
        break
      case 39:
      case 68:
        this.snake.changeDir('right')
        break
    }
  }
  // 分数
  changeGrade(grade) {
    this.dispatch('changeGrade', grade)
  }
  // 控制器
  control() {
    if (this.toControl) {
      this.toControl()
      return
    }
    window.addEventListener('keydown', this.keyDown)
  }
  // 用户自定义控制器
  addControl(fn) {
    fn.call(this)
    window.removeEventListener('keydown', this.keyDown)
  }
}