const express = require('express')
const app = express();

app.get("/", (req, res) => {
  res.send("hello world")
})


// elm 中间件
const elm = require('./router/elm')
app.use('/elm', elm)

// model 中间件
const model = require('./router/model')
app.use('/model', model)


const post = 3000;
app.listen(post, () => {
  console.log(`express start at http://localhost:${post}`);
})