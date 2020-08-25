const express = require('express')
const bodyParse = require('body-parser')
const path = require('path')
const fs = require('fs')

const app = express()

const multer = require('multer')
// 创建multer对象 
const upload = multer({})

app.use('/public', express.static(path.join(__dirname, './www')))

// 对应的接口添加中间件  upload.single('上传的key值')
app.post('/file', upload.single('upload'), (req, res) => {
    // 上传的文件信息，默认是不存在的，只有multer中间件处理过才存在
    console.log(req.file);
    // buffer 上传的图片的数据
    let { buffer,  mimetype, size, originalname } = req.file
    // 将buffer写入到文件内部
    // 防止文件被覆盖 保证文件名的唯一性
    let name = (new Date()).getTime() + '_' + parseInt(Math.random() * 767457165) + parseInt(Math.random() * 12313)
    // 让后缀名 和源文件保持一致
    let ext = originalname.split('.')[1]
    fs.writeFile(path.join(__dirname, `./www/${name}.${ext}`), buffer, (err) => {
        if (err) { 
            res.send({ err: 0, msg: '图片上传失败' })
        } else {
            res.send({ err: 0, msg: '图片上传0k' })
        }
    })
})

app.get('/test',(req,res)=>{
    res.send({mas:'请求成功'})
})

app.listen(3000, () => {
    console.log('服务器启动')
})