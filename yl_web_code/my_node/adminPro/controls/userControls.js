// 数据库相关代码抽离

const userModel = require('../db/model/userModel')

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

// 用户注册
let userLogin = async (mail, password) => {
    let result = await userModel.findOne({mail,password});
    if(result){
        return result;
    }else{
        throw '邮箱或密码错误！'
    }
}


module.exports = {
    userReg,
    userLogin
}