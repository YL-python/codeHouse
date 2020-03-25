// 错误的捕获

const fs = require('fs')

console.log(1)
// fs.mkdirSync("./haha")
console.log(2)
// 抛出错误终止程序运行

// 使用try catch 捕获 同步代码可能会出现的错误
console.log(3)
try {
    fs.mkdirSync("./haha")
} catch (error) {
    console.log(error)
}
console.log(4)

// 异步代码错误的捕获   错误代码的回调优先  在回调函数中，第一个参数一定是错误信息
// 错误状态是 null 表示执行成功 ，如果包含错误信息表示执行失败
fs.mkdir('./haha',(err)=>{
    console.log(err)
})