const http = require('http');
const url = require('url'); // 内置解析url的一个类
const fs = require('fs');
const mime = require('./mime.json');
const path = require('path');
const server = http.createServer((req, res) => {
  res.setHeader('content-type', 'text/html;charset=utf-8');
  //    res.writeHead(300,{"content-type":"text/html;charset=utf-8"})
  console.log(req.url);
  let urlObj = url.parse(req.url);
  console.log(urlObj);
  // 1."/product"    2."/product?name=zhangsan"; 查询参：querystring
  if (urlObj.pathname === '/' || urlObj.pathname === '/index') {
    // 文件读取；
    // let indexData =  fs.readFileSync("./views/index.html")
    // res.end(indexData);
    // 流方式；
    let indexData = fs.createReadStream('./views/index.html');
    indexData.pipe(res);
  } else if (urlObj.pathname === '/product') {
    // let indexData =  fs.readFileSync("./views/product.html")
    // res.end(indexData);
    let indexData = fs.createReadStream('./views/product.html');
    indexData.pipe(res);
  } else {
    if (urlObj.pathname !== '/favicon.ico') {
      // 获取扩展名；
      let ext = path.extname(urlObj.pathname);
      //    console.log("??",ext);
      res.setHeader('Content-Type', mime[ext]);
      let resData = fs.createReadStream('./views' + urlObj.pathname);
      resData.pipe(res);
    }
  }
});
server.listen(3000);
