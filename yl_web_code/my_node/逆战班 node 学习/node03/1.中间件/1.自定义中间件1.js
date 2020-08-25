const express = require("express")

app = express()

//中间件的本质是一个函数   常用的情况下有三个参数 req  res next
function middleware1(req,res,next){
    console.log("这里是中间件：middleware1");
    // 执行下一个中间件
    next()
}  // 自定义中间件

function middleware2(req,res,next){
    console.log("这里是中间件：middleware2");
    // 执行下一个中间件
    next()
}  // 自定义中间件

// 添加中间件
app.get("/test",middleware1,middleware2, (req, res) => {
    console.log(111111);
})

app.listen(3000, () => {
    console.log("服务器启动");
})