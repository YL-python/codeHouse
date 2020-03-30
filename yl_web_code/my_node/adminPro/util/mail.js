const nodemailer = require("nodemailer");

//创建发送邮件的对象
let transporter = nodemailer.createTransport({
    host: "smtp.qq.com", // 服务器信息
    port: 465,
    secure: true, // true for 465, false for other ports
    auth: {
        user: '2336739721@qq.com', // 发送方邮箱账号
        pass: 'pydbwqadnshldhhh' // 邮箱的授权码
    }
});

function send(mail, htmlData) {
    // 邮件的内容
    let content = {
        from: '"node服务器" <2336739721@qq.com>',
        to: `${mail}`, // list of receivers
        subject: "node服务器", // 标题
        html: htmlData // html body
    }

    //调用sendMail方法发送 
    return new Promise((resolve, reject) => {
        transporter.sendMail(content, (err, infos) => {
            if (err) {
                reject("邮件 发送失败")
            } else {
                resolve("邮件 发送成功");
            }
        });
    })
}

module.exports = {
    send
}