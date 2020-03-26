// 引入用户信息文件
const userList = require("./userList.js")
console.log(userList[0].name)


var d = new Date(2020, 2, 12, 14, 05, 00);
console.log(d)

function myFunc(arg) {
    console.log(`arg was => ${arg}`);
}

setInterval(myFunc, 1500, 'funky');