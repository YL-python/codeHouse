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

写完music-list组件之后，这里套用一下就可以了
```

#### loading组件

```
布局用定位在最中间
创建一个loading组件可以复用
```

### 歌手列表页面

```
请求数据-处理数据
头部标题和快速入口数据使用计算属性
快速入口点击事件可以直接跳转到对应下标的元素
快速入口移动事件就要获取两次的距离差从而计算移动了多少个
监听滚动事件，获取滚动Y坐标，看Y坐标在那个 group里面（需要计算出每一个group的高度）
点击边界，拖动边界的处理
监听 滚动的Y值，来设置当前选中的值，点击事件自己触发Y值的改变
头部标题减少dom操作可以让一个值在一定范围内才去进行操作
```

### 歌手详情页

```
在list-view 内用 $emit 吧点击事件派发给父组件，就是基础组件内我们不做业务逻辑，只是告诉父组件我们被点击了以及点击的元素是什么，让父组件去处理业务逻辑

歌手页跳过来的时候向vuex内传递singer对象，在详情页使用vuex内的singer对象去发送请求获取数据。
因为是传递歌手对象，但是直接访问的时候是没有这个歌手对象的，可以做一个跳回歌手页面的优化

发现歌曲信息在很多地方都用的到，然后就是定义一个song对象来存放我们需要的每一首歌的信息
在对数据进行处理的时候可以用一个工厂方法帮助我们创建对象
```

#### 音乐列表页

```
很多地方用到歌曲列表  因为涉及到业务逻辑所以开发出来一个组件（不是基础组件）

向上滚动，监听Y的值，控制用一块背景div滚动，滚动到距离顶部一定距离的时候修改 图片z-index的层级以及图片的高度
向下滚动设置图片的放大倍率
```

#### 歌曲列表

```
发现音乐列表中有很多歌曲列表是复用的，开发一个歌曲列表的基础组件
```

### 播放器

```
关键参数，播放列表，是否播放，播放方式，歌曲列表（配合播放方式生成播放列表），大屏小屏，播放歌曲的下标
大小屏切换功能（有交互动画） create-keyframe-animation  实现js动画
歌曲播放暂停功能
	播放按钮的样式，子元素点击事件阻止冒泡
	cd图片旋转
上下一首：
	暂定时点击会播放，
	点击太快的时候数据可能还没请求到，所以要点限制
	样式也要有变化，请求错误的时候逻辑的处理
进度条：跟随动，拖动，播放时间（audio提供）
模式切换：每一次切换模式的时候都重新给vuex内的playlist赋值，实际播放的时候，当前正在播放的歌曲的下标要重新设置
每一首歌播放完成之后要进行播放下一首，如果模式是单曲循环就要重新播放这首歌

歌词：与滚动条的绑定

左右滑动：记录滑动的百分比，超过一个值的时候进行dom操作展示动画就好了

mixin：播放器组件加载后容器的高度需要增加，用全局混入的方式，监听播放的歌曲列表改变，改变了就增加高度
```

#### 进度条组件

```
跟随播放显示，获取播放时长的百分比
拖动控制，点击控制
点击和移动事件的监听过程中我们只是修改样式，只有在和父组件通信之前才去获取百分比参数

圆形进度条 用 svg实现
```

#### 歌词

```
推荐直接写一个解析歌词的方法
在audio 的updateTime 方法里面匹配歌词的时间来显示
```

### 排行榜

```
请求数据，加载数据
注意小播放器打开的时候滚动组件的长度要修改
加个loading组件
套用 music-list组件
```

### 搜索

```
搜索历史：吧数据存储到本地，有最大值，vuex初始化是读取本地数据
```

#### 搜索框

```
基础组件，作用是输入值，清空值以及返回值这样的一些基础操作
```

#### 搜索结果列表

```
业务相关的一个组件，用来展示搜索到的结果列表
当前搜索第几页，要不要搜索歌手，搜索关键词
上拉加载：scroll组件实现监听 scrollEnd事件并emit给父组件
搜索关键词改变的时候 要初始化一些值（page  hasMore  scroll的位置）
```

#### 搜索历史

```
点击歌曲的时候添加历史，点击X的时候删除，删除全部的时候有提示
```

### 歌曲播放列表

```
很多时候 scroll组件初始化成功了但是不能滚动是因为初始化的时候dom数据还没有渲染
transition-group 定义列表动画
多组件之间相同功能的代码使用mixin封装起来
还有就算业务逻辑
```

### 歌曲添加列表

```
之前写了很多组件都可以复用了，歌曲播放历史是在audio  准备好的时候添加的
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

### create-keyframe-animation

```
js方式实现动画的一个库
```
### good-storage

```
对 localStorage和sessionStorage 的封装
```

###  一些事件

```
@click.stop   阻止事件向上冒泡
@touchstart.prevent  组织浏览器默认行为
```

### 父子路由之间的参数传递

```
使用Vuex
父路由使用点击事件传递对象给 vuex 并进行跳转
子路由检测参数是否完全，不完全就退回父路由
```

### 移动端调试

```
vconsole
在main中导入就行 不需要使用
```

## 优化

```
路由懒加载
<keep-alive></keep-alive> 缓存动态组件
```

