const Koa = require('koa');
const app = new Koa();
const url = require('url');
// app.use((ctx, next) => {
//   // ctx-->context 上游 或者下游的对象；
//   // res ===ctx.res ; req===ctx.req;
//   // ctx.response ; ctx.request;
//   let urlObj = url.parse(ctx.req.url, true);
//   console.log(urlObj.query.name);
//   console.log(ctx.request.query.name);
//   ctx.body = '你好';
// });
// 中间件;
let middleware1 = async function (ctx, next) {
  console.log('one start...');
  ctx.state = 100;
  // console.log(ctx.header);
  // ctx.status = 302;
  // ctx.set("location","http://www.baidu.com");
  // 200  ---> {code:1,info:"成功"}  {code:0,info:"失败"}
  ctx.body = 'hello';

  // await new Promise(resolve=>{
  //     setTimeout(()=>{
  //         console.log(111);
  //         resolve();
  //     },1000)
  // })
  // throw new Error("something error....");
  await next();
  // (function(ctx,next){
  //     console.log("two start...")
  //     ctx.body = "world";

  //     console.log("two end...")
  // })();
  console.log('one end...');
};
let middleware2 = async function (ctx, next) {
  console.log('two start...');
  console.log(ctx.state);
  ctx.body = 'world';
  console.log('two end...');
};

app.use(middleware1);
app.use(middleware2);
// 错误处理中间件；
app.on('error', (err) => {
  console.log(err);
});

app.listen(3000);
