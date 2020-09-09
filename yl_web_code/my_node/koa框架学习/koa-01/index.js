const koa = require('koa')
const app = new koa()
const Router = require('koa-router')
const router = new Router()

const koaBody = require('koa-body')
const cors = require('@koa/cors')
const json = require('koa-json')

router.prefix('/api')

router.get('/', (ctx) => {
  console.log(ctx)
  // console.log(ctx.request);
  ctx.body = 'hello world'
})

router.get('/api', (ctx) => {
  const params = ctx.request.query
  console.log(params)
  ctx.body = ctx.request
})

router.get('/async', async (ctx) => {
  let result = await new Promise((resolve) => {
    setTimeout(() => {
      resolve('hello async')
    }, 2000)
  })
  ctx.body = result
})

router.post('/post', async (ctx) => {
  let { body } = ctx.request
  console.log(body)
  console.log(ctx.request)
  ctx.body = {
    ...body,
  }
})

app.use(koaBody())
app.use(cors())
app.use(json({ pretty: false, param: 'pretty' }))
app
  .use(router.routes()) // 使用路由
  .use(router.allowedMethods()) // 拦截没有定义的路由

app.listen(3000)
