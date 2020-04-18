# yl-music

> 一个使用vue制作的音乐项目

## Build Setup

``` bash
# Project setup
npm install
# Compiles and hot-reloads for development
npm run serve
# Compiles and minifies for production
npm run build
# Lints and fixes files
npm run lint
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
    fastclick 会阻止click事件  标签上添加一个 needclick的class属性就可以跳过
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
缓存使用
销毁生命周期清楚计时器
```

#### 推荐歌单

```
推荐歌单需要用到 better-scroll ，但是每一次用到我们就初始化一次是很机械的写代码
所以把初始化 better-scroll 写成了一个组件
然后重写 一些better-scroll 的方法
推荐页面完全加载完成的时候调用
完全加载这个在代码里面有体现，轮播图的图片第一次加载成功
```

#### loading组件

```
布局用定位在最中间
创建一个loading组件可以复用
```

### 歌手页面

```
请求数据-处理数据
头部标题和快速入口数据使用计算属性
快速入口点击事件可以直接跳转到对应下标的元素
快速入口移动事件就要获取两次的距离差从而计算移动了多少个
监听滚动事件，获取滚动Y坐标，看Y坐标在那个 group里面（需要计算出每一个group的高度）
点击边界，拖动边界的处理
监听 滚动的Y值，来设置当前选中的值，点击事件自己触发Y值的改变
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
官网介绍：https://cn.vuejs.org/v2/api/#keep-alive
```

### axios

```
github:https://github.com/axios/axios
```

### 懒加载

```
github:https://github.com/hilongjw/vue-lazyload
main.js：
    import VueLazyload from 'vue-lazyload'
    Vue.use(VueLazyload, {
      preLoad: 1.3,
      error: require('common/image/default.png'),
      // webpack会解析require语法，解析不了ico文件
      loading: '/favicon.ico',  // 引入public目录下文件
      attempt: 1
    })
需要加载图片的地方：
    <img width="60px" height="60px" :src="item.imgurl" alt />
    :src 换成 v-lazy 即可
    <img width="60px" height="60px" v-lazy="item.imgurl" alt />
```

### better-scroll

```
https://ustbhuangyi.github.io/better-scroll/doc/zh-hans/
```

