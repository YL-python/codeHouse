const Koa = require('koa');
const static = require('koa-static');
const Router = require('koa-router');
let app = new Koa();
let router = new Router();
app.use(static(__dirname + '/static'));

// 创建一个 socket.io
const server = require('http').createServer(app.callback());
const io = require('socket.io')(server);

router.get('/', (ctx) => {
  ctx.body = 'some value...';
});

app.use(router.routes());
io.on('connection', (socket) => {
  console.log('有socket连接');
  // socket.on("testFn",function(data){
  //     console.log(data);
  //     // socket.emit("clientFn",data); //发送给一个用户
  //    setTimeout(() => {
  //      socket.broadcast.emit("clientFn",data); //广播给出了自己之外的所有用户；
  //    }, 2000);
  // })
  socket.on('addData', function (data) {
    console.log(data);
    socket.broadcast.emit('addInputData', data);
  });
});
server.listen(3000);
