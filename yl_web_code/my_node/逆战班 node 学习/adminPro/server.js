const express = require('express')
const app = express()
const bodyParser = require('body-parser')
const path = require('path')

// post 数据解析
app.use(bodyParser.urlencoded({extended:false}))
app.use(bodyParser.json())

// 启动数据库链接
require('./db/connect') 

// token 中间件
let tokenMiddleWare = require('./middleware/tokenMiddleWare')

/*
    路由
        1.文件路由
        2.食品路由
        3.用户路由
*/
const fileRouter = require('./router/uploadRouter')
app.use('/admin/upload', fileRouter)

const foodRouter = require('./router/foodRouter')
app.use('/admin/food',tokenMiddleWare, foodRouter) // 添加token验证中间件

const userRouter = require('./router/userRouter')
app.use('/admin/user', userRouter)

app.use('/public',express.static(path.join(__dirname,'./public')))

app.listen(3000, () => {
    console.log(`
    /**
*
* ━━━━━━神兽出没━━━━━━
* 　　 ┏┓     ┏┓
* 　　┏┛┻━━━━━┛┻┓
* 　　┃　　　　　 ┃
* 　　┃　　━　　　┃
* 　　┃　┳┛　┗┳  ┃
* 　　┃　　　　　 ┃
* 　　┃　　┻　　　┃
* 　　┃　　　　　 ┃
* 　　┗━┓　　　┏━┛　Code is far away from bug with the animal protecting
* 　　　 ┃　　　┃    神兽保佑,代码无bug
* 　　　　┃　　　┃
* 　　　　┃　　　┗━━━┓
* 　　　　┃　　　　　　┣┓
* 　　　　┃　　　　　　┏┛
* 　　　　┗┓┓┏━┳┓┏┛
* 　　　　 ┃┫┫ ┃┫┫
* 　　　　 ┗┻┛ ┗┻┛
*
* ━━━━━━感觉萌萌哒━━━━━━
*/
        服务器启动
    `)
})