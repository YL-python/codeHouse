const express = require('express')

// 引入数据库连接文件  启动服务器的时候同时连接数据库
// 引入一个文件的同时会将文件执行一次 抛出是为了在别的文件引用
const db = require('./db/connect') 
const app = express()

// 引入路由
let UserRouter = require('./router/userRouter')
app.use('/user', UserRouter)

app.listen(3000, () => {
    console.log('服务器启动')
})