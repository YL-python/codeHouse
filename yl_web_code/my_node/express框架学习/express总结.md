# 服务器搭API接口总结

## es6中export和export default的区别

export与export default均可用于导出常量、函数、文件、模块
你可以在其它文件或模块中通过import+(常量 | 函数 | 文件 | 模块)名的方式，将其导入，以便能够对其进行使用

在一个文件或模块中，export、import可以有多个，export default**仅有一个**

通过export方式导出，在导入时要**加{ }**，export default则不需要

## module.exports、exports

这两个是在node服务器里面用的，导入的时候用 require

exports 等价于 let exports = module.exports;

不能直接将exports变量指向一个值，因为这样等于切断了exports与module.exports的联系。

 module.exports={}  用来抛出变量和方法，require导入的时候用对象解构

## express框架相关的

### 错误处理代码

```js
// 错误处理  要放在最后
app.use(function (err, req, res, next) {
    res.status(500).json({
        status: 500,
        message: "服务器错误！" + err.message,
        help: "QQ:2336739721"
    })
})
```

### ApiDoc的使用

咋用就不说了，之前学的时候笔记也写了很多

说一下 express访问到ApiDoc生成的index.html文件

先把 apidoc加到静态资源目录，因为生成的文件中，引用别人的时候用的是双斜线，不加静态资源就会报错。

```js
// 静态资源
app.use(express.static(path.join(__dirname, 'apidoc')))
```

然后是访问根路径的时候怎么把html页面返回给用户。用res对象的 sendFile方法

```js
// 首页
app.get('/', (req, res) => {
    res.sendFile(path.join(__dirname, './apidoc/index.html'))
})
```

## 对象键名称的修改

其实没有直接的修改方法。现在的做法是

```js
let obj = {data:1,msg:"123"}
obj.message = obj.msg
delete obj.msg
```

就是把先改的键值直接生成，最后删掉旧的值

## cors跨域

```js
const cors = require("cors")
app.use(cors());
```

## nginx方向代理的时候用户真实ip获取

需要nginx 做配置  location中添加 proxy_set_header  X-real-ip $remote_addr;

```
location ^~/node/ {
    proxy_set_header  X-real-ip $remote_addr;
}
```

服务器就可以在请求头在用 X-real-ip 获取到用户真实ip

express获取请求头。req对象的使用get方法

```js
console.log("req.headers:",req.get("X-Real-IP"));
```

