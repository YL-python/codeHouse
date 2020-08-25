const express = require("express")

// 创建路由对象
const router = express.Router()

router.get("/login", (req, res) => {
    res.send("这里是 user login");
});

router.get("/reg", (req, res) => {
    res.send("这里是 user reg");
});

// 抛出 路由模块
module.exports = router