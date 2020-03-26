const express = require("express")
app = express()

const cors = require("cors")
app.use(cors());


app.get("/user/login", (req, res) => {
    res.send("这里是 user login");
});

app.get("/user/reg", (req, res) => {
    res.send("这里是 user reg");
});

app.get("/food/add", (req, res) => {
    res.send("这里是 food add");
});

app.get("/food/del", (req, res) => {
    res.send("这里是 food del");
});

app.listen(3000, () => {
    console.log("服务器启动");
});