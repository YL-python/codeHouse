/*
1.前端先请求自己的服务器
2.我方服务器发起服务器请求 请求目标服务器
3.将网路请求的结果返回给前端
使用 axios 发起服务器请求
*/ 

const express = require("express")
const cors = require("cors")
const axios = require("axios")

app = express()
app.use(cors());

app.get("/cors", (req, res) => {
    // res.send({ err: 0, msg: '访问成功' });
    let url = 'https://apis.map.qq.com/ws/location/v1/ip?key=3BFBZ-ZKD3X-LW54A-ZT76D-E7AHO-4RBD5'
    // 发起服务器请求
    axios.get(url)
        .then((data)=>{
        // console.log(data.data)
        res.send(data.data)
    })
});

app.listen(3000, () => {
    console.log("服务器启动");
});