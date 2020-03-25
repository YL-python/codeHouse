/*
文件操作：
    创建一个文件 
        writeFile 覆盖写入
    修改一个文件
        rename 修改名称
        appendFile 追加写入
    删除一个文件
        unlink
    读取一个文件
        readFile
*/
const fs = require('fs')

// 覆盖写入
// fs.writeFile('./hehe.txt', '我独自一个人抗下了所有', (err) => {
//     console.log(err)
// })

// 修改名称
// fs.rename('./haha.txt',"./hehe.txt",(err)=>{
//     console.log(err)
// })

// 追加写入
// fs.appendFile('./hehe.txt', '韩梅梅和李雷', (err) => {
//     console.log(err)
// })

// 删除文件  直接干掉，不存在回收站
// fs.unlink('./hehe.txt', (err) => {
//     console.log(err)
// })

// 读取文件
// fs.readFile('./hehe.txt', 'utf8', (err, data) => {
//     console.log(err)
//     // buffer 二进制数据流
//         // 解决方法一
//         // console.log(data.toString())
//         // 解决方法二
//         // 可选参数中加入编码指定为 utf-8
//     console.log(data)
// })

// 判断读取的文件类型 
fs.stat('./hehe.txt',(err,state)=>{
  // console.log(state)   // 文件的信息
  console.log(state.isFile()) //是不是一个文件
  console.log(state.isDirectory()) //是不是一个文件夹
})