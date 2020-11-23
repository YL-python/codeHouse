const Koa = require('koa');
const static = require('koa-static');
const Router = require('koa-router');
const koaBody = require('koa-body');
let app = new Koa();
let router = new Router();
app.use(static(__dirname + '/static'));
app.use(
  koaBody({
    multipart: true,
  })
);
router.get('/', (ctx) => {
  ctx.body = 'some value...';
});
router.post('/post', (ctx) => {
  // console.log(111);
  console.log(ctx.request.body);
  ctx.body = 'some value...';
});
router.post('/xml', (ctx) => {
  // console.log(111);
  // console.log(ctx.request.body);
  // ctx.set("content-type","text/xml");
  ctx.body = `<?xml version='1.0' encoding='utf-8'?>
                <books>
                    <nodejs>nodejs从入门到实战</nodejs>
                    <nodejs>vue从入门到精通</nodejs>
                </books>
            `;
});

router.post('/myajax', (ctx) => {
  // console.log(111);
  // console.log(ctx.request.body);
  // ctx.body = "some value11...";
  ctx.body = {
    name: '李四',
    age: 29,
  };
});
app.use(router.routes());
app.listen(8989);
