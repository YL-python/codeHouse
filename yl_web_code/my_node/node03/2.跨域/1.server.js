const express = require("express")
app = express()

// 使用 cors 解决跨域问题   核心就是设置了请求头
const cors = require("cors")
// cors 自带中间件 来解决跨域问题
app.use(cors());

app.get("/test", (req, res) => {
    res.send({ err: 0, msg: '访问成功' });
});

app.listen(3000, () => {
    console.log("服务器启动");
});