const express = require('express')
const bodyParser = require('body-parser')

const app = express()

// 接口支持解析表单格式
app.use(bodyParser.urlencoded({ extended: false }))
// 接口支持解析json格式
app.use(bodyParser.json())

app.post('/test',(req,res)=>{
  console.log(req.body)
})

app.listen(3000,()=>{
  console.log('服务器启动')
})