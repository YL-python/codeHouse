// 食品相关的数据模型

const mongoose = require('mongoose')

let userSchema = new mongoose.Schema({
    mail : { type:String, required:true },
    password : { type:String, required:true }
})

let userModel = mongoose.model('users', userSchema)

module.exports = userModel