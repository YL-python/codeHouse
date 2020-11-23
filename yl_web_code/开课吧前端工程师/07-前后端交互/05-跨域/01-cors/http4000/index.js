const Koa = require('koa');
const static = require('koa-static');
const Router = require('koa-router');
const koaBody = require('koa-body');

let app = new Koa();
app.use(static(__dirname + '/static'));
let router = new Router();

// 处理预检请求；
router.options('/*', (ctx) => {
  ctx.set('Access-Control-Allow-Origin', 'http://localhost:3000');
  ctx.set(
    'Access-Control-Allow-Headers',
    'Content-Type, Content-Length, Authorization, Accept, X-Requested-With , mytest'
  );
  // 预检请求有效期
  ctx.set('Access-Control-Max-Age', 600);
  // 不管返回啥一定要有返回
  ctx.body = '';
});

router.get('/', (ctx) => {
  ctx.body = 'some value...';
});

router.post('/getData', (ctx) => {
  // ctx.set("Access-Control-Allow-Origin","*"); //不能设置跨域携带凭证 withCredentials
  ctx.set('Access-Control-Allow-Origin', 'http://localhost:3000');
  // ctx.set("Access-Control-Allow-Headers", "Content-Type, Content-Length, Authorization, Accept, X-Requested-With , mytest");
  ctx.set('Access-Control-Expose-Headers', 'Date');
  console.log('接收到了3000端口的请求');
  ctx.body = '4000端口的数据';
});

router.get('/proxy', (ctx) => {
  ctx.body = '4000端口 proxy 返还的数据';
});

app.use(router.routes());
app.listen(4000);
