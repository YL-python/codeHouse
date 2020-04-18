# yl-music

> 一个使用vue制作的音乐项目

## Build Setup

``` bash
# install dependencies
npm install
# serve with hot reload at localhost:8080
npm run dev
# build for production with minification
npm run build
# build for production and view the bundle analyzer report
npm run build --report
```

## 准备工作

```
package.json
devDependencies选项末尾添加
    "stylus": "^0.54.5"  # css使用 stylus
    "stylus-loader": "^2.1.1"
    "babel-polyfill": "^6.2.0",  # babel的一些补丁，解决低版本浏览器对es6不支持
dependencies选项末尾添加
	"babel-runtime": "^6.0.0", # 对es6语法解析加强的库，辅助es6的编译
    "fastclick": "^1.0.6"  # 解决移动端点击有300ms延迟的库
并且重新 npm install
```

```
eslintrc.js内添加两条规则
'eol-last': 0,
'space-before-function-paren':0
```

```
build/webpack.base.conf.js 下的resolve/alias 配置项内路径的别名
'common': resolve('src/common')
...
```

```
index.html页面设置 meta标签，移动端开发必备
<meta name="viewport"
          content="width=device-width, initial-scale=1.0, maximum-scale=1.0, minimum-scale=1.0, user-scalable=no">
```

## 页面骨架

### 头部组件 

```
m-header.vue
暂时没做我的入口，只是一个文字和logo图标，简单的布局，在APP.vue中引入并使用
```

### 导航栏

```
tab.vue
用router-link 放四个路由，路由要先注册好，简单的布局，在APP.vue中引入并使用
```

### 推荐页面

#### 轮播图

```
better-scroll默认是Y方向滚动，所以X方向滚动的时候要进行一些设置
初始化滚动框的X方向宽度
	子元素个数乘以视口宽度和
初始化better-scroll 监听scrollEnd事件
自动滚动使用next方法，而且每次结束之后还会触发scrollEnd事件，要先清楚计时器在执行自动滚动的方法
```



## 总结

### jsonp

```
浏览器同源策略的限制，非同源下的请求，都会产生跨域问题。
但是script标签的src，img标签的src，或者说link标签的href他们没有被通源策略所限制。
标签的属性也会发送一个get请求,请求静态资源,并且没有跨域问题。
原理：https://segmentfault.com/a/1190000009773724
github:https://github.com/webmodules/jsonp
源码不到100行还有很多注释，有时间一定要看看
```

### 缓存

```
keep-alive 标签包裹的组件会缓存
```

