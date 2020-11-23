const http = require('http');
const fs = require('fs');
// res.write();  res.end();

// 单攻，只能服务器给客户端，不能客户端给服务端
let server = http.createServer((req, res) => {
  let url = req.url;
  if (url == '/') {
    let data = fs.readFileSync('index.html');
    res.end(data);
  } else if (url == '/sse') {
    // 设置请求头
    res.setHeader('content-type', 'text/event-stream;charset=utf-8');
    // 服务端端定时推送数据到客户端；
    setInterval(() => {
      // data:  是开始的标记符    \r\n\r\n 是结束的标记符
      res.write('data:时间是' + new Date() + '\r\n\r\n');
      // 不能有  end()
    }, 1000);
  }
  // res.write()
});
server.listen(4000);
