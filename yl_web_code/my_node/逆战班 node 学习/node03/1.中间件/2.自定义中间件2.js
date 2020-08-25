const express = require("express")

app = express()

function middleware(req,res,next){
    console.log("这里是中间件");
    next();
}

app.use(middleware);  // 全局使用中间件，写的位置会有影响

app.get("/xixi", (req, res) => {
    console.log("xixi");
})

app.get("/hehe", (req, res) => {
    console.log("hehe");
})

app.listen(3000, () => {
    console.log("服务器启动");
})