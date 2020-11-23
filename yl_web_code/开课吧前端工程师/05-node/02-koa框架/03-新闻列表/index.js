const Koa = require('koa');
const Router = require('koa-router');
const views = require('koa-views');
const static = require('koa-static');
let app = new Koa();
let router = new Router();
let data = require('./data/data.json');
app.use(views(__dirname + '/views'), {
  extension: 'pug', //jade
});
// /static --->locahost:8888
app.use(static(__dirname + '/static'));
router.get('/', (ctx) => {
  ctx.redirect('/index');
});
router.get('/index', async (ctx) => {
  // ctx.redirect("/index");
  // ctx.body = "主页";
  let p = parseInt(ctx.query.p) || 1;
  let perPage = 5;
  let newData = JSON.parse(JSON.stringify(data)).splice((p - 1) * perPage, perPage);
  // [{},{}]
  let pageCount = Math.ceil(JSON.parse(JSON.stringify(data)).length / perPage);
  await ctx.render('index.pug', {
    newData,
    pageCount,
    p,
  });
});
router.get('/detail', async (ctx) => {
  // ctx.redirect("/index");
  // ctx.body = "详细页面"
  let id = ctx.query.id || 1;
  let detailData = data.filter((v) => v.id == id)[0];
  // console.log(detailData);
  await ctx.render('detail.pug', {
    detailData,
  });
});
app.use(router.routes());
app.listen(4000);
//作业 ：通过koa实现 新闻 列表、分页、详细页面；
