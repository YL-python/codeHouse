const Koa = require('koa');
const Router = require('koa-router');

let app = new Koa();
let router = new Router();

router.get('/', (ctx) => {
  ctx.body = 'some value...';
});

router.get('/proxy', (ctx) => {
  ctx.body = '4000端口 proxy 返还的数据';
});

app.use(router.routes());
app.listen(4000);
