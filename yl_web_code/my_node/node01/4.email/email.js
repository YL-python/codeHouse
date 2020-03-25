/*
邮箱轰炸器 每隔1s 发一条邮件
通过第三方模块发送邮件 nodemailer
*/
// 服务器信息: node_modules/nodemailer/lib/well-know/services.json

// 引入第三方模块
const nodemailer = require("nodemailer");

//创建发送邮件的对象
let transporter = nodemailer.createTransport({
    host: "smtp.qq.com",  // 服务器信息
    port: 465,
    secure: true, // true for 465, false for other ports
    auth: {
        user: '2336739721@qq.com', // 发送方邮箱账号
        pass: 'pydbwqadnshldhhh' // 邮箱的授权码
    }
});

// 邮件的内容
let content = {
    from: '"node服务器" <2336739721@qq.com>',
    to: ["2336739721@qq.com","1581983629@qq.com"], // list of receivers
    subject: "天气预报", // 标题
    // text:"123",   // 文本和 html只能写一个
    html: "邮箱 test" // html body
}

//调用sendMail方法发送 
transporter.sendMail(content, (err) => {
    console.log(err)
});