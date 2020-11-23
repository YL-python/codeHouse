const Koa = require('koa');
const static = require('koa-static');
const Router = require('koa-router');
const koaBody = require('koa-body');
const axios = require('axios');
let app = new Koa();

app.use(static(__dirname + '/static'));
app.use(koaBody());
let router = new Router();

router.get('/test', async (ctx) => {
  console.log(1111);
  ctx.body = 'run with 3000...';
});

router.all('/getData', async (ctx) => {
  console.log(ctx.request.body);
  // ctx.body = "run with 3000..."
  ctx.body = { name: '张三', age: 20 };
});

router.all('/changeRequest', (ctx) => {
  axios({ method: 'get', url: 'http://localhost:5000/axios' }).then((res) => {
    console.log(res.data);
  });
  ctx.body = { value: '返还的数据' };
});

app.use(router.routes());
app.listen(3000);
