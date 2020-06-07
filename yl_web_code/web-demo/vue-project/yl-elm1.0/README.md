# yl-elm1.0

## vue的介绍

### vue-resource和axioc

vue-resource是Vue.js的一款插件，它可以通过XMLHttpRequest或JSONP发起请求并处理响应。

vue2.0之后，就不再对vue-resource更新，而是推荐使用axios。基于 Promise 的 HTTP 请求客户端，可同时在浏览器和 Node.js 中使用。

### mvvm 的认识

m(Model) v(View) vm(ViewModel)

model 是对应到数据部分，也就是JavaScript 的对象

view 对应到视图部分就是，浏览器DOM

在mvvm模式在，数据和视图是不直接通讯的，他们的通讯使用的是ViewModel，ViewModel需要实现一个观察者，每当数据发生改变的时候，ViewModel可以监听到数据的变化，会通知到对应的视图做更新。当用户操作视图的时候 ViewModel 也会监听到视图的改变，从而通知数据的改动。就实现了数据的双向绑定。

### vue的核心思想

+ 数据驱动

  dom是数据的一种自然映射

  [响应式原理](https://vuejs.bootcss.com/guide/reactivity.html)

+ 组件化

  扩展HTML元素，封装可重用的代码

  [组件化](https://vuejs.bootcss.com/guide/index.html#组件化应用构建)

  组件化原则：1. 页面上每个独立的可视/可交互区域视为一个组件。2. 每个组件对应一个工程目录，组件所需要的各种资源在这个目录下就近维护。3.页面不过是组件的容器，组件可以嵌套自由组合形成完整的页面。

## npm卸载包

安装和卸载 xx-abc包

安装

```
【npm install xx-abc】安装但不写入package.json；
【npm install xx-abc --save】 安装并写入package.json的"dependencies"中；
【npm install xx-abc --save-dev】安装并写入package.json的"devDependencies"中。
```

卸载

```
【npm uninstall xx-abc】：删除模块，但不删除模块留在package.json中的对应信息
【npm uninstall xx-abc --save】：删除模块，同时删除模块留在package.json中dependencies下的对应信息
【npm uninstall xx-abc --save-dev】：删除模块，同时删除模块留在package.json中devDependencies下的对应信息
```



## package.json中dependencies 和devDependencies的差异

```
devDependencies:是你开发时候用的库， 比如测试库，测试服务器之类的，在真实生产环境是不需要的

dependencies:是你生产环境需要的依赖库 比如测试库 vue,vue-route

注意：如果你使用了一些构建工具，比如webpack之类的，打包的时候，是不会把dev库打进去的。
```

## vue全局引入样式

```
# main.js 中
import './common/css/reset.css';

App.vue 中
@import "./common/css/reset.css";
```



## 后端接口的搭建

服务器简单搭建了一个express 接口，数据都是视频给的死数据

http://coderyl.top/node2/elm/goods

## 路由配置

router index.js中注意的

```js
const goods = () => import(/* webpackChunkName: "elm-1.0" */ 'components/goods/goods.vue')

const goods = () => import('components/goods/goods.vue')
// 上面的注释貌似是在 webpack 打包的时候用到
```

router-link 标签

active-class属性，是模糊匹配，exact-active-class是精确匹配，但是现在不清楚是bug修复了官方文档没修改还是本身代码就有bug，bug就是 active-class 实现是 exact-active-class。

可以在创建 router对象的时候修改默认的值

```js
const router = new VueRouter({
  routes,
  linkActiveClass: "active",
  linkExactActiveClass: "active"
})
```

## 移动端 1像素边框

直接使用border-bottom设置边框的画，在不懂dpi的手机上显示是不一样的，解决办法就是用befor伪类添加一个 1像素的线，然后媒体查询控制缩放

## axios 数据请求

没啥好说的，注意一下箭头函数的this指向和function函数的this指向

## 数据区别

vue中有4种变量的定义

**data中定义数据**
data中定义的变量是我们需要去维护的，会被多次改变或者使用到

computed中定义数据
computed中计算属性中的定义的变量会被自动计算
需要注意的是computed中的变量不能在data中定义，会冲突，说简单点，data中的变量我们自己控制变化，在不同的methods中定义会怎样变化或者被赋值，比如购物车列表数据，在增删改过程中都会变化，我们需要自己去维护这个变量，在增删改的时候做相对应的处理，然而购物车数量这个变量却可以根据购物车数据计算出来，这时候就可以利用computed属性帮我们自动计算维护购物车数量这个属性值了，不需要在增删改的时候自己再次去手动维护修改这个变量值了

**created中定义数据**
在生命周期中，created在dom渲染之前，是最先执行的，在这里面定义的变量通常不会被改动。
常用场景有：
调用子组件时，我们需要向子组件传些个性化的参数，这些参数定义一次就好，通常不会改变，此时可以再 created中定义，因为它是在组件创建渲染之前执行的

methods中定义数据
在methods中的一些函数中有3种情况
一种是只在函数内部会被用到的变量，我们只需要用let 定义就好
一种是在多个函数中会被用到 我们可以用this.xxx来定义，就跟在data中定义差不多
还有一种是常量的定义 我们直接在export default的外面用const定义就好关于watch的使用

watch和computed的区别

+ 都能实时计算监听

+ watch可以监听data中的变量，computed不能计算data中的变量

+ watch使用场景
  + data中的变量变化太频繁，对变化处理可以采用监听的方式
  + 利用watch控制执行顺序，比如我们需要做的某个处理是需要某个值传进来后才能做的，那么就可以监听这个 值，一旦接收到这个值，或者这个值发生改变，我们才开始处理

## 头部组件

直接就把数据传进去，然后写样式。emm  这样代码复用性就比较小，不过这个例子本身就不是很大的项目。代码复用的话，自定义组件库的时候，就要考虑很多了，现在为了写头部组件写头部组件，吧数据一传然后写样式就 ok 了

## v-if 和 v-show

### 区别

- 1.手段：v-if是通过控制dom节点的存在与否来控制元素的显隐；v-show是通过设置DOM元素的display样式，block为显示，none为隐藏；
- 2.编译过程：v-if切换有一个局部编译/卸载的过程，切换过程中合适地销毁和重建内部的事件监听和子组件；v-show只是简单的基于css切换；
- 3.编译条件：v-if是惰性的，如果初始条件为假，则什么也不做；只有在条件第一次变为真时才开始局部编译（编译被缓存？编译被缓存后，然后再切换的时候进行局部卸载); v-show是在任何条件下（首次条件是否为真）都被编译，然后被缓存，而且DOM元素保留；
- 4.性能消耗：v-if有更高的切换消耗；v-show有更高的初始渲染消耗；

### 使用场景

基于以上区别，因此，如果需要非常频繁地切换，则使用 v-show 较好；如果在运行时条件很少改变，则使用 v-if 较好。

### 总结

v-if判断是否加载，可以减轻服务器的压力，在需要时加载,但有更高的切换开销;v-show调整DOM元素的CSS的dispaly属性，可以使客户端操作更加流畅，但有更高的初始渲染开销。如果需要非常频繁地切换，则使用 v-show 较好；如果在运行时条件很少改变，则使用 v-if 较好。

## sticky footer 布局

> http://www.fly63.com/article/detial/3028

视频给出的完美解决方案 

```html
<div class="detail">
    <!-- 需要使用一个容器包裹本身的内容并且清楚浮动 -->
    <div class="detail-wrapper clearfix">
        <div class="detail-content"></div>
    </div>
    <!-- footer -->
    <div class="detail-close">
    	<i class="icon-close" ></i>
    </div>
</div>
```

```stylus
.detail {
    position: fixed;
    z-index: 100;
    top: 0;
    left: 0;
    bottom: 0;
    right: 0;
    overflow: auto;
    background: rgba(7, 17, 27, 0.5);

    .detail-wrapper {
      min-height: 100%;

      .detail-content {
        margin-top: 64px;
        // 这个padding-bottom 很重要
        padding-bottom: 64px;
      }
    }

    .detail-close {
      position: relative;
      width: 32px;
      height: 32px;
      font-size: 32px;
      margin: -64px auto 0 auto;
      clear: both;
    }
  }
.clearfix::after {
    display: block;
    content: ".";
    height: 0;
    clear: both;
    visibility: hidden;
}
```

这个时候在 detail-content 中些内容的话就会满足 sticky footer 布局

## star 星星组件

遇到一个问题就是星星组件在父组件的样式定义，视频给的方法是 在子组件外面套一个div，然后给这个div设置样式。之前咋做的我忘记了 555。

百度了一下，因为写样式的时候设置了 scoped ，样式就只会在当前作用域起效。不会对全局样式进行污染，貌似是webpack中的一个功能。然后webpack提供了两种写法可以渗透到子组件上。

```css
<style lang="css" scoped>
  父组件样式选择器 /deep/ 子组件样式选择器{ //第一种写法
    color:red;
  }
  .父组件样式选择器 >>> 子组件样式选择器{   //二种写法
    color:red;
  }
</style>
```



## css3 backdrop filter 和 filter

emm  也没啥好说的，百度一下，filter 是当前模糊，backdrop filter是背景模糊