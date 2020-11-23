var WebSocketServer = require('ws').Server;
wss = new WebSocketServer({ port: 8181 });
wss.on('connection', function (ws) {
  console.log('client connected');
  // rs.on("data",)
  ws.on('message', function (message) {
    //监听接收的数据
    console.log(message);
  });
  // setInterval(() => {
  let somedata = {
    name: '张三',
    age: 20,
  };
  ws.send(JSON.stringify(somedata));
  // }, 1000);
});
