# Express 复习

## 快速入门

### 简单的hello world

```js
const express = require('express')
const app = express()
const port = 3000

app.get('/', (req, res) => res.send('Hello World!'))

app.listen(port, () => console.log(`Example app listening on port ${port}!`))

// 执行：node app.js
```

### 路由

基本形式如下

```js
app.METHOD(PATH, HANDLER)

// app是一个 express的实例
// METHOD是请求的方法 get post put delete
// PATH 是请求的路径
// HANDLER是匹配路由时执行的函数。
```

### express 托管静态文件

```js
express.static(root, [options])
// 返回值是一个 express的中间件
```

例如，通过如下代码就可以将 `public` 目录下的图片、CSS 文件、JavaScript 文件对外开放访问了：

```js
app.use(express.static('public'))

// http://localhost:3000/images/kitten.jpg
// http://localhost:3000/css/style.css
// http://localhost:3000/js/app.js
// http://localhost:3000/images/bg.png
// http://localhost:3000/hello.html
```

Express 在静态目录查找文件，因此，存放静态文件的目录名不会出现在 URL 中。

问访问的路径创建一个虚拟路径

```js
app.use('/static', express.static('public'))

// http://localhost:3000/static/images/kitten.jpg
// http://localhost:3000/static/css/style.css
// http://localhost:3000/static/js/app.js
// http://localhost:3000/static/images/bg.png
// http://localhost:3000/static/hello.html
```

可以有多个，访问的顺序是定义的顺序

```javascript
app.use(express.static('public'))
app.use(express.static('files'))
```

最好的写法：

```js
app.use('/static', express.static(path.join(__dirname, 'public'))
```

## 路由详解

### 基本创建

```js
app.METHOD(PATH, HANDLER)
```

### all方法

所有请求路径包括 /secret 的请求会先被all()的方法拦截到，然后在next给下一个进行处理

```js
app.all('/secret', function (req, res, next) {
  console.log('Accessing the secret section ...')
  next() // pass control to the next handler
})
```

### path

可以写正则

想想其实比较简单，内部实现就直接匹配一下就好了

```js
app.get('/ab?cd', function (req, res) {
  res.send('ab?cd')
})
// 匹配 acd 和 abc

app.get('/ab+cd', function (req, res) {
  res.send('ab+cd')
})
// 匹配 abbcd 和 abbbcd ...

// 还有很多 比如*号，比如分组(cd)?  比如 /a/ 会匹配路径中带有a 的请求，还可以写复杂的正则
```

### handlers

处理起可以有多个函数，或者一个函数数组。或者函数和函数数组组合，处了最后一个处理起以外，其他的处理起都需要提供next参数并且最后调用next()方法

处理起是多个方法

```js
app.get('/example/b', function (req, res, next) {
  console.log('the response will be sent by the next function ...')
  next()
}, function (req, res) {
  res.send('Hello from B!')
})
```

处理起是方法数组
```javascript
var cb0 = function (req, res, next) {
  console.log('CB0')
  next()
}

var cb1 = function (req, res, next) {
  console.log('CB1')
  next()
}

var cb2 = function (req, res) {
  res.send('Hello from C!')
}

app.get('/example/c', [cb0, cb1, cb2])
```

处理起是方法和数组
```javascript
var cb0 = function (req, res, next) {
  console.log('CB0')
  next()
}

var cb1 = function (req, res, next) {
  console.log('CB1')
  next()
}

app.get('/example/d', [cb0, cb1], function (req, res, next) {
  console.log('the response will be sent by the next function ...')
  next()
}, function (req, res) {
  res.send('Hello from D!')
})
```

### 子路由

子路由更有利于帮助我们的代码模块化

第一种创建方法，在express实力上直接创建

```js
app.route('/book')
  .get(function (req, res) {
    res.send('Get a random book')
  })
  .post(function (req, res) {
    res.send('Add a book')
  })
  .put(function (req, res) {
    res.send('Update the book')
  })
```

第二种创建方法，用express.Router方法创建，最后在实力上用 use方法绑定，

```js
// birds.js
var express = require('express')
var router = express.Router()

// middleware that is specific to this router
router.use(function timeLog (req, res, next) {
  console.log('Time: ', Date.now())
  next()
})
// define the home page route
router.get('/', function (req, res) {
  res.send('Birds home page')
})
// define the about route
router.get('/about', function (req, res) {
  res.send('About birds')
})

module.exports = router


//index.js
var birds = require('./birds')
// ...
app.use('/birds', birds)
```

第三种方法，两个express实例嵌套

```js
var express = require('express')

var app = express() // the main app
var admin = express() // the sub app

admin.get('/', function (req, res) {
  console.log(admin.mountpath) // /admin
  res.send('Admin Homepage')
})

app.use('/admin', admin) // mount the sub app
```



## 中间件

中间件，拦截器，也就是`app.METHOD(PATH, HANDLER)`中的 HANDLER 处理器。也就是说，其实就是一个方法，然后插入到路由中去。

### 定义一个中间件

定义中间件就是定义一个方法，参数多了一个next,并且最后要调用一下next()

```js
var myLogger = function (req, res, next) {
  console.log('LOGGED')
  next()
}
```

### 全局使用中间件

就是说在经过所有路由之前都会被这个处理器处理一下。使用的是实例.use()方法

```js
app.use(myLogger)
```

中间件设置请求时间案例：

```js
var express = require('express')
var app = express()

var requestTime = function (req, res, next) {
  req.requestTime = Date.now()
  next()
}

app.use(requestTime)

app.get('/', function (req, res) {
  var responseText = 'Hello World!<br>'
  responseText += '<small>Requested at: ' + req.requestTime + '</small>'
  res.send(responseText)
})

app.listen(3000)
```

### 局部使用中间件

也就是对某一个路由使用中间件,下面的代码只有`/user/:id` 路径才会使用中间件

```js
app.use('/user/:id', function (req, res, next) {
  console.log('Request Type:', req.method)
  next()
})

app.all('/user/:id', function (req, res, next) {
  console.log('Request Type:', req.method)
  next()
})
```

只有`/user/:id` 路径，并且是get方法才会使用中间件

```js
app.get('/user/:id', function (req, res, next) {
  console.log('ID:', req.params.id)
  next()
}, function (req, res, next) {
  res.send('User Info')
})
```

看了一下官网API

```js
app.all(path, callback [, callback ...])

app.use([path,] callback [, callback...])

// all方法和use方法的区别就是一个path是必须参数一个是可选参数
// 并且后面都是多个 callback 回调函数
// 看到这就明白了，中间件啥的就是函数
```

### 内置中间件

```js
express.static // 提供静态目录，如HTML文件、图像等。
express.json // 用JSON有效负载解析传入的请求。注意:可用于Express 4.16.0+
express.urlencoded // 用url编码的有效负载解析传入的请求。注意:可用于Express 4.16.0+
```

## 错误处理

express中有自带的错误捕获机制

下面说说几种常见错误。并且都是express能捕获到的。

+ 我们写程序的时候自己用 throw new Error('BROKEN') 抛出的错误
+ 中间件内没有调用next()方法，会报错误和跳过剩下的所有中间件
+ next方法中可以传递err对象，就是定义方法的时候有个err参数，其他的参数在next()方法中是不允许的

express不会捕获异步的错误，需要我们把错误通过next方法传递出来

```js
app.get('/', function (req, res, next) {
  fs.readFile('/file-does-not-exist', function (err, data) {
    if (err) {
      next(err) // Pass errors to Express.
    } else {
      res.send(data)
    }
  })
})

app.get('/', function (req, res, next) {
  setTimeout(function () {
    try {
      throw new Error('BROKEN')
    } catch (err) {
      next(err)
    }
  }, 100)
})

app.get('/', function (req, res, next) {
  Promise.resolve().then(function () {
    throw new Error('BROKEN')
  }).catch(next) // Errors will be passed to Express.
})
```

发生的错误如果被 express捕获到了，那么程序就不会终止，如果没有被捕获到就会直接结束程序。

## req对象

> req对象表示HTTP请求，并具有请求查询字符串、参数、正文、HTTP头等的属性。

### 属性

+ req.baseUrl  基础的url ，返回父路由的路径
+ req.originalUrl  原始的url, url是啥就返回啥
+ req.path   包含请求URL的路径部分。

```javascript
// GET 'http://www.example.com/admin/new'
app.use('/admin', function (req, res, next) {
  console.dir(req.originalUrl) // '/admin/new'
  console.dir(req.baseUrl) // '/admin'
  console.dir(req.path) // '/new'
  next()
})
```

+ req.hostname  主机名
+ req.ip  请求的ip 
+ req.method   请求用的方法
+ req.params   请求的参数
+ req.query  请求的参数
+ req.body  get请求的请求体 

```
body：请求体中的数据
query：请求的参数，URL后面以？的形式，例：user?id
params：请求的参数，URL后面以/的形式，例：user/:id
```

## res对象

### 属性

+ res.locals  绑定一些常量数据

### 方法

+ res.json([body])  返回一个json响应，使用JSON.stringify()转换为JSON字符串
+ res.jsonp([body])  发送带有JSONP支持的JSON响应。这个方法与res.json()相同，只是它选择加入JSONP回调支持。
+ res.redirect([status,] path)  指定状态码的重定向
+ res.render(view [, locals] [, callback])  用来渲染模板文件的
+ res.send([body]) 返回一个http响应。可以是缓冲区对象、字符串、对象或数组。
+ res.sendFile(path [, options] [, fn])  返回服务器上的文件
+ res.status(code)  设置响应的状态码

## form标签

### 重要的属性

| 属性                                                         | 值                                                           | 描述                                                         |
| ------------------------------------------------------------ | ------------------------------------------------------------ | ------------------------------------------------------------ |
| [action](https://www.w3cschool.cn/htmltags/att-form-action.html) | *URL*                                                        | 表单提交的地址                                               |
| [enctype](https://www.w3cschool.cn/htmltags/att-form-enctype.html) | application/x-www-form-urlencoded multipart/form-data text/plain | 规定在向服务器发送表单数据之前如何对其进行编码。（适用于 method="post" 的情况） |
| [method](https://www.w3cschool.cn/htmltags/att-form-method.html) | get post                                                     | 表单提交的HTTP 方法。                                        |

### enctype详解

| 值                                | 描述                                                         |
| :-------------------------------- | :----------------------------------------------------------- |
| application/x-www-form-urlencoded | 默认。在发送前对所有字符进行编码（将空格转换为 "+" 符号，特殊字符转换为 ASCII HEX 值）。 |
| multipart/form-data               | 不对字符编码。当使用有文件上传控件的表单时，该值是必需的。   |
| text/plain                        | 将空格转换为 "+" 符号，但不编码特殊字符。                    |

## body-parser

表单提交的时候编码方式有四种（见上面form标签enctype属性）

body-parser这个插件就是把被form表单加密的数据进行解码

```js
const bodyParser = require('body-parser')

// 解析post数据
// 解析表单格式的数据 x-www-form-urlencode 
app.use(bodyParser.urlencoded({ extended: false }))
// 解析json数据格式
app.use(bodyParser.json())
```

一般上面几句话就直接能用了

## 跨域问题的解决

第一个，访问自己服务器出现跨域

+ 设置一下请求头让谁都能访问

```js
//解决跨域
app.all('*',function (req, res, next) {
	res.header("Access-Control-Allow-Origin", "*");
	res.header("Access-Control-Allow-Headers", "X-Requested-With");
	res.header("Access-Control-Allow-Methods","PUT,POST,GET,DELETE,OPTIONS");
	res.header("X-Powered-By",' 3.2.1')
	res.header("Content-Type", "application/json;charset=utf-8");
	next();
});
```

+ 使用cors 插件---内部实现原理和上面是一样的，只不过逻辑更完善
```js
//解决跨域
const cors = require("cors")
app.use(cors());
```

第二个 访问别人服务器出现跨域，只能自己搭服务器，用服务器去请求别人的服务器

```js
const axios = require("axios")
// 发起服务器请求
axios.get(url)
    .then((data)=>{
    // console.log(data.data)
    res.send(data.data)
})
```

## 图片上传

https://www.cnblogs.com/pingfan1990/p/4701355.html

### 原理

### 手写实现

### 插件实现

## APIDOC

全局安装

```
npm install apidoc -g

如果不是全局安装的话就会找不到  apidoc这个命令
```

在根目录 先编写一个 apidoc.json进行介绍接口文档

```json
{
  "name": "yl-node",
  "version": "0.1.0",
  "description": "yl-node 包含的所有的api接口文档",
  "title": "yl-node apiDoc",
  "url" : "http://coderyl.top/node/"
}
```

然后弄一个文件夹写要生成接口的注释比如根目录下新建一个叫 xxx  的文件夹，然后在xxx文件夹里面写js代码  并且用上 apidoc的注释

```js
/**
 * @api {请求路径} 路径 标题
 * @apiGroup Group
 * @apiDescription 描述这个API的信息
 *
 * @apiParam {String} userName 用户名
 * @apiParamExample {json} request-example
 * {
 *  "userName": "Eve"
 * }
 *
 * @apiError {String} message 错误信息
 * @apiErrorExample  {json} error-example
 * {
 *   "message": "用户名不存在"
 * }
 * 
 * 
 * @apiSuccess {String} userName 用户名
 * @apiSuccess {String} createTime 创建时间
 * @apiSuccess {String} updateTime 更新时间
 * @apiSuccessExample  {json} success-example
 * {
 *   "userName": "Eve",
 *   "createTime": "1568901681"
 *   "updateTime": "1568901681"
 * }
 */
function getUserInfo(username) {
  // 假如这个函数是根据用户名返回用户信息的
}
```

现在的目录情况

```
根目录
--xxx
----xxx.js
--apidoc.json
```

然后要生成文档的话就在根目录下执行

```
apidoc -i xxx/ -o apidoc/

-i参数是要扫描带注释的文件夹  -o参数是要生成文档的文件夹
```

说一下node项目  apidoc.json文件可以放到packge.json文件中