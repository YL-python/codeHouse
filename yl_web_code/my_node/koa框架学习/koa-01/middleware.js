const koa = require('koa')
const app = new koa()


const middleware1 = function async (ctx, next) {
  console.log('this is a middleware1 start');
  console.log(ctx.request.path);
  next()
  console.log('this is a middleware1 end');
}
const middleware2 = function async (ctx, next) {
  console.log('this is a middleware2 start');
  console.log(ctx.request.path);
  next()
  console.log('this is a middleware2 end');
}
const middleware3 = function async (ctx, next) {
  console.log('this is a middleware3 start');
  console.log(ctx.request.path);
  next()
  console.log('this is a middleware3 end');
}

app.use(middleware1)
app.use(middleware2)
app.use(middleware3)

app.listen(3000)