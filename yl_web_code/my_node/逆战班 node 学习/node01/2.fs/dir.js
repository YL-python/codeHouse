/*
同步方法没有返回值，没有回调函数，发生错误会直接中断程序
异步方法有回调函数，发生错误回调函数优先,必须要有回调函数

文件夹操作：
    创建: mkdir
    删除: rmdir
    修改: rename
    读取: readdir
*/

// 引入文件相关模块
const fs = require('fs')

/*
// 创建文件夹
console.log(1)
fs.mkdir("./hehe",(err)=>{
    console.log(2)
    console.log(err)
})
console.log(3)

// nodejs 是非阻塞io  上面程序会打印  132

let result = fs.mkdirSync('./haha')
console.log(result)

// mkdir是异步创建，mkdirSync是同步创建
*/

/*  
// 异步方法 删除文件夹
fs.rmdir('./haha', (err) => {
    if (err) {
        console.log("删除失败")
    } else {
        console.log("删除成功")
    }
})

// 同步方法 删除文件夹
let result =  fs.rmdirSync('./haha')
console.log(result)
*/


/*  
// 异步方法 修改文件夹
fs.rename("./hehe","./haha",(err)=>{
    if (err) {
        console.log("修改失败")
    } else {
        console.log("修改成功")
    }
})
*/

/*  */
// 异步方法 读取文件夹  回调函数有两个参数，一个是错误信息，一个是读取到的内容
fs.readdir("./", (err, infos) => {
    if (err) {
        console.log("读取失败" + err)
    } else {
        console.log(infos)
    }
})
