// 数据库相关代码抽离

const userModel = require('../db/model/userModel')

// 产生token
const {createToken} = require('../util/jwt')

// 用户注册
let userReg = async (mail, password) => {
    let isExst = await userModel.findOne({mail});
    let result;
    if(isExst){
        throw '邮箱已存在'
    }else{
        result = await userModel.insertMany({mail,password})
    }
    return result;
}

// 用户登陆
let userLogin = async (mail, password) => {
    let result = await userModel.findOne({mail,password});
    if(result){
        let {_id,mail} = result;
        // 登陆成功 产生新的token
        let token = createToken({_id,mail});
        await userModel.updateOne({_id},{token})
        return {_id,mail,token};
    }else{
        throw '邮箱或密码错误！'
    }
}

// 用户和token是否统一
let tokenCheck = async (_id,token)=>{
    let result = await userModel.findOne({_id,token})
    if(result){
        return result;
    }else{
        throw '用户token不匹配,请重新登陆';
    }
}

let userLogout = async (_id) => {
    let result = await userModel.updateOne({_id},{token:''})
    if(result){
        return result;
    }else{
        throw '退出失败请重试。';
    }
} 

module.exports = {
    userReg,
    userLogin,
    tokenCheck
}