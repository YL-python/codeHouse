const express = require('express')
const path = require('path')
const app = express()
const post = 3000
const bodyParser = require('body-parser')
app.use(bodyParser.urlencoded({
    extended: false
}))
app.use(bodyParser.json())
const cors = require("cors")
app.use(cors());

const axios = require("axios")
const cheerio = require("cheerio")

// 静态资源
app.use(express.static(path.join(__dirname, '')))

function reconvert(str) {
    str = str.replace(/(\\u)(\w{1,4})/gi, function ($0) {
        return (String.fromCharCode(parseInt((escape($0).replace(/(%5Cu)(\w{1,4})/g, "$2")), 16)));
    });
    str = str.replace(/(&#x)(\w{1,4});/gi, function ($0) {
        return String.fromCharCode(parseInt(escape($0).replace(/(%26%23x)(\w{1,4})(%3B)/g, "$2"), 16));
    });
    str = str.replace(/(&#)(\d{1,6});/gi, function ($0) {
        return String.fromCharCode(parseInt(escape($0).replace(/(%26%23)(\d{1,6})(%3B)/g, "$2")));
    });

    return str;
}

// 首页
app.get('/', (req, res) => {
    axios.get('https://voice.baidu.com/act/newpneumonia/newpneumonia/').then((adata) => {
        // console.log(res.data);
        // 使用cheerio 分析数据内容
        // const $ = cheerio.load(res.data)
        // console.log($("script#captain-config").text);
        let data = adata.data.match(/<script type=\"application\/json\" id=\"captain-config\">(.*?)<\/script>/)
        // console.log(data);
        data = reconvert(data[1])
        console.log(typeof data);
        let jsonData = JSON.parse(data)
        console.log(jsonData.component[0].mapLastUpdatedTime);
        res.send(jsonData)
    })
})

// 监听3000端口号启动一个 node服务器
app.listen(post, () => {
    console.log('服务器启动')
})