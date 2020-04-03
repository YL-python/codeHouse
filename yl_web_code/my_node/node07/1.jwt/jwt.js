/*
产生 token
验证 token 合法性

http://www.ruanyifeng.com/blog/2018/07/json_web_token-tutorial.html
*/

const jsonwebtoken = require('jsonwebtoken')

// 需要加密的对象
let payload = {
    name: '网易',
    ps: 123
}
// 加密的密钥
let secret = 'sdjflskj13123131'
// 加密方法
let token = jsonwebtoken.sign(payload, secret) 

console.log(token)
// 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJuYW1lIjoi572R5piTIiwicHMiOjEyMywiaWF0IjoxNTgxOTkxOTMyfQ.B8CbpW3rB29QcUFfw404JJizQ1ndg9CyxYY1VOxg27w'


// 解密函数 参数1 要验证的token 参数2产生token的秘钥
let result = jsonwebtoken.verify(token, 'sdjflskj13123131')
console.log(result)