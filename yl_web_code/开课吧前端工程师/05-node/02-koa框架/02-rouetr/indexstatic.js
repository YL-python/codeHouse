const Koa = require('koa');
const Router = require('koa-router');
const views = require('koa-views');
const static = require('koa-static');
let app = new Koa();
let router = new Router();

app.use(views(__dirname + '/views'), {
  extension: 'pug',
});
// /static --->locahost:8888
app.use(static(__dirname + '/static'));
router.get('/', async (ctx, next) => {
  // ctx.body = "新闻页面";
  ctx.redirect('/index');
});
router.get('/index', async (ctx, next) => {
  // ctx.body = "新闻页面";
  await ctx.render('index.pug');
});
router.get('/detail', async (ctx, next) => {
  ctx.body = '详细页面';
});
// get: 地址栏； script src=""  img src  href=""
router.all('/getData/:id', async (ctx, next) => {
  console.log(ctx.params.id);
  ctx.body = {
    name: '张三',
    age: 20,
  };
});
// get ：获取数据 post：添加数据   put：更新  delete：删除;
// 以前接口；
// 添加  http://localhsot/addUser?id=1
// 删除  http://localhsot/delUser
// RESTful 设计架构接口；
// 添加： http://localhsot/user  （post）
// 查询:  http://localhsot/user?id=1  (get)

app.use(router.routes());
app.listen(8888);
