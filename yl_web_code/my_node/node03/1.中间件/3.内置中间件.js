const express = require("express")
const path = require("path")

app = express()
/*
内置中间件只有一种  静态资源路径中间件
指定一个文件夹能在线访问
*/
// 指定静态资源路径  http://localhost:3000/111.png
// 映射  本地./www   映射到服务器 / 路径
app.use(express.static('/', path.join(__dirname, "./www")));
// 映射到服务器路径是  /  时 可以不写 上面等价下面写法
// app.use(express.static(path.join(__dirname, "./www")));

app.listen(3000, () => {
    console.log("服务器启动");
})