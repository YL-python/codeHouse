const Koa = require('koa');
const static = require('koa-static');
const Router = require('koa-router');
const mysql2 = require('mysql2');
const koaBody = require('koa-body');
let app = new Koa();
app.use(static(__dirname + '/static'));
app.use(koaBody());
const connection = mysql2.createConnection({
  host: 'localhost',
  user: 'root',
  password: 'root',
  database: 'kkb',
});

let router = new Router();
router.get('/', (ctx) => {
  ctx.body = 'some value...';
});
router.get('/getData', async (ctx) => {
  let [rows] = await connection.promise().query('SELECT * FROM message');
  ctx.body = rows;
});
router.post('/addData', async (ctx) => {
  let { content } = ctx.request.body;
  console.log(content);
  let [rows] = await connection.promise().query('INSERT INTO message(content) VALUES (?)', [content]);
  // ctx.body = rows;
  console.log(rows);
  let resData;
  if (rows.affectedRows > 0) {
    resData = {
      info: '添加成功',
      status: 1,
    };
  } else {
    resData = {
      info: '添加失败',
      status: 0,
    };
  }
  ctx.body = resData;
});
app.use(router.routes());
app.listen(3000);
