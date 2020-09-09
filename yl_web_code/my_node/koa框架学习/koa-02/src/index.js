const path = require('path')

const koa = require('koa')
const app = new koa()
const helmet = require('koa-helmet')
import router from './routes/routes'
const statics = require('koa-static')
const koaBody = require('koa-body')
const jsonutil = require('koa-json')
const cors = require('@koa/cors')
const compose = require('koa-compose')
const compress = require('koa-compress')

// app.use(helmet())
// app.use(statics(path.join(__dirname, '../public')))
// app.use(router())

const isDevMode = process.env.NODE_ENV === 'production' ? false : true

// compose整合中间件
const middleware = compose([
  koaBody(),
  statics(path.join(__dirname, '../public')),
  cors(),
  jsonutil({ pretty: false, param: 'pretty' }),
  helmet(),
])

if (!isDevMode) {
  app.use(compress())
}

app.use(middleware)
app.use(router())

app.listen(3000)
// router 目录对请求的路径进行管理
// api 目录对实际业务进行操作
