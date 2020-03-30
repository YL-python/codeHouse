// 处理文件的中间件

const express = require('express')
const router = express.Router()

const multer = require('multer')
const upload = multer({})

const path = require('path')
const fs = require('fs')

// 被允许的文件类型
const types = ['jpg','png','gif','jpeg'];

/**
 * @api {post} /admin/upload/img   上传图片
 * @apiName img
 * @apiGroup Upload
 *
 * @apiParam {File} file 图片.
 *
 * @apiSuccess {String} err 状态码.
 * @apiSuccess {String} msg  信息提示.
 * @apiSuccess {String} path  图片存储在服务器的路径.
 * 
 * @apiError {String} err 状态码.
 * @apiError {String} msg  信息提示.
 */
router.post('/img', upload.single('file'), (req, res) => {
    // console.log(req.file);
    let {buffer, mimetype, size} = req.file;
    // 判断尺寸
    if(size > 2*1024*1024){
        return res.send({err:-1,msg:"图片尺寸过大"});
    }
    let fileType = mimetype.split('/')[1];
    if(types.indexOf(fileType) === -1){
        return res.send({err:-2,msg:"图片类型未知"});
    }
    // 接收文件
    let fileName = (new Date()).getTime() + '_' + parseInt(Math.random() * 12345) + "_" + parseInt(Math.random() * 54321);
    fs.writeFile(path.join(__dirname,`../public/img/${fileName}.${fileType}`),buffer,(err)=>{
        if(err){
            res.send({err:-3,msg:"上传失败，请重试"});
        }else{
            // http://localhost:3000/public/img/1585400862798_9804_41604.jpeg
            res.send({err:0,msg:"上传成功",path:`/public/img/${fileName}.${fileType}`});
        }
    })
})

module.exports = router;