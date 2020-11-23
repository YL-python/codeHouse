const Koa = require('koa');
const static = require('koa-static');
const Router = require('koa-router');
const koaBody = require('koa-body');
// 引入 fs模块处理文件
const fs = require('fs');
const mysql2 = require('mysql2');

let app = new Koa();
let router = new Router();
app.use(static(__dirname + '/static'));
const connection = mysql2.createConnection({
  host: 'localhost',
  user: 'root',
  password: 'root',
  database: 'kkb',
});

app.use(
  koaBody({
    multipart: true, //允许文件上传
  })
);

router.get('/', (ctx) => {
  ctx.body = 'something...';
});

router.post('/upload', async (ctx) => {
  // 获取的文件数据ctx.request.files
  // console.log(ctx.request.files.img.path);
  // 转存文件
  fs.writeFileSync('./static/img/uploads/' + ctx.request.files.img.name, fs.readFileSync(ctx.request.files.img.path));
  // 将文件路径数据存入到数据库；
  let imgUrl = '/img/uploads/' + ctx.request.files.img.name;
  let imgName = ctx.request.files.img.name;
  // 当前登录用户；
  let uid = ctx.cookies.get('uid') || 1;
  let [rows] = await connection
    .promise()
    .query('INSERT INTO photo(imgUrl,imgName,uid) VALUES (?,?,?)', [imgUrl, imgName, uid]);
  let resData;
  if (rows.affectedRows > 0) {
    resData = { info: '添加成功', status: 1 };
  } else {
    resData = { info: '添加失败', status: 0 };
  }
  ctx.body = resData;
});
//获取图片数据做对应呈现；

router.get('/getPhotoData', async (ctx) => {
  let uid = ctx.cookies.get('uid') || 1;
  let [rows] = await connection.promise().query('SELECT * FROM photo WHERE uid=?', [uid]);
  console.log(rows);
  ctx.body = rows;
});

router.all('/checkUser', async (ctx) => {
  // 认证是否登录；
  // console.log(ctx.request.body);
  let { username, pwd } = ctx.request.body;
  console.log(username, pwd);
  let [rows] = await connection.promise().query('SELECT * FROM users WHERE username=? AND pwd=?', [username, pwd]);
  // console.log(rows);
  let resData;

  if (rows.length > 0) {
    // 将id存入cookie；
    ctx.cookies.set('uid', rows[0].id, { maxAge: 3600 * 1000 * 24 * 7 });
    resData = { info: '用户名密码正确', status: 1 };
  } else {
    resData = { info: '用户名或者密码错误', status: 0 };
  }
  ctx.body = resData;
});

app.use(router.routes());
app.listen(8686);
