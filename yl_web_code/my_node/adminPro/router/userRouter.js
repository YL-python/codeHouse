/*
处理 用户 的中间件
    注册
    验证码
    登陆
*/

const express = require('express')
const router = express.Router()

const Mail = require('../util/mail')
const mails = {}

const userDao= require('../controls/userControls')

// token 中间件
let tokenMiddleWare = require('./middleware/tokenMiddleWare')

/**
 * @api {post} /admin/user/getCode   获取验证码
 * @apiName getCode
 * @apiGroup User
 *
 * @apiParam {String} mail 邮箱.
 *
 * @apiSuccess {String} err 状态码.
 * @apiSuccess {String} msg  信息提示.
 * 
 * @apiError {String} err 状态码.
 * @apiError {String} msg  信息提示.
 */
router.post('/getCode',(req,res)=>{
    let {mail} = req.body;
    let code = parseInt(Math.random() * 10000)
    let htmlData = `验证码是${code}`
    Mail.send(mail,htmlData).then(()=>{
        // 存到内存中
        mails[mail] = code;
        res.send({err:0,msg:'验证码发送ok'})
    }).catch(()=>{
        res.send({err:-1,msg:'验证码发送 no ok'})
    })
})

/**
 * @api {post} /admin/user/reg   注册
 * @apiName reg
 * @apiGroup User
 * 
 * @apiParam {String} mail 邮箱.
 * @apiParam {String} code 验证码.
 * @apiParam {String} password 密码.
 *
 * @apiSuccess {String} err 状态码.
 * @apiSuccess {String} msg  信息提示.
 * 
 * @apiError {String} err 状态码.
 * @apiError {String} msg  信息提示.
 */
router.post('/reg',(req,res)=>{
    let {mail,code,password} = req.body;
    if(code == mails[mail]){  // 类型不一样
        userDao.userReg(mail,password)
        .then(()=>{
            res.send({err:0,msg:'注册 ok'})
        }).catch((errinfo)=>{
            res.send({err:-2,msg:errinfo})
        })
    }else{
        res.send({err:-1,msg:'验证码 no ok'})
    }
})

/**
 * @api {post} /admin/user/login   登陆
 * @apiName login
 * @apiGroup User
 * 
 * @apiParam {String} mail 邮箱.
 * @apiParam {String} password 密码.
 *
 * @apiSuccess {String} err 状态码.
 * @apiSuccess {String} msg  信息提示.
 * @apiSuccess {String} token 用户的token.
 * 
 * @apiError {String} err 状态码.
 * @apiError {String} msg  信息提示.
 */
router.post('/login',(req,res)=>{
    let {mail,password} = req.body;
    userDao.userLogin(mail,password)
    .then((userInfo)=>{
        res.send({err:0,msg:'登陆 ok',userInfo})
    }).catch((errInfo)=>{
        res.send({err:-1,msg:errInfo})
    })
})

/**
 * @api {post} /admin/user/logout   退出登陆
 * @apiName logout
 * @apiGroup User
 * 
 * @apiParam {String} id 用户id.
 *
 * @apiSuccess {String} err 状态码.
 * @apiSuccess {String} msg  信息提示.
 * 
 * @apiError {String} err 状态码.
 * @apiError {String} msg  信息提示.
 */
// 需要在登陆情况下才能退出，就是说需要验证token
router.post('/logout',tokenMiddleWare,(req,res)=>{
    let {_id} = req.body;
    userDao.userLogout(_id)
    .then(()=>{
        res.send({err:0,msg:'退出 ok'})
    }).catch((errInfo)=>{
        res.send({err:-1,msg:errInfo})
    })
})

module.exports = router;