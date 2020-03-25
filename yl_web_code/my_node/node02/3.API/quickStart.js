const express = require('express')
const app = express() // 实例化 express 对象

// 监听请求地址
app.get('/login', (req, res) => {
    res.send("呵呵哒")
})

// 监听3000端口号启动一个 node服务器
// 本地服务器 域名 http://localhost:3000/login
app.listen(3000, () => {
    console.log('服务器启动')
})