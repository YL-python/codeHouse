const express = require("express")

// 创建路由对象
const router = express.Router()

router.get("/add", (req, res) => {
    res.send("这里是 food add");
});

router.get("/del", (req, res) => {
    res.send("这里是 food del");
});

// 抛出 路由模块
module.exports = router