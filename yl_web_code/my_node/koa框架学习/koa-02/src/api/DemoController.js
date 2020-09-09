class DemoController {
  constructor() {}
  async demo(ctx) {
    ctx.body = {
      msg: 'body msg',
    }
  }
}

export default new DemoController()
