const express = require("express")
const cors = require("cors")

app = express()
app.use(cors());

// 引入路由
const userRouter = require('./router/userRouter')
const foodRouter = require('./router/foodRouter')
// 使用路由
app.use('/user',userRouter);
app.use('/food',foodRouter);

app.listen(3000, () => {
    console.log("服务器启动");
});