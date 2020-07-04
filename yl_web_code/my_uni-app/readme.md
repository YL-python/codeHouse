# uni-app的基本使用

## 介绍

 [官方网页](https://uniapp.dcloud.io/resource)

`uni-app` 是一个使用 [Vue.js](https://vuejs.org/) 开发所有前端应用的框架，开发者编写一套代码，可发布到iOS、Android、H5、以及各种小程序（微信/支付宝/百度/头条/QQ/钉钉）等多个平台。

## 开发规范

为了实现多端兼容，综合考虑编译速度、运行性能等因素，`uni-app` 约定了如下开发规范：

- 页面文件遵循 [Vue 单文件组件 (SFC) 规范](https://vue-loader.vuejs.org/zh/spec.html)
- 组件标签靠近小程序规范，详见[uni-app 组件规范](https://uniapp.dcloud.io/component/README)
- 接口能力（JS API）靠近微信小程序规范，但需将前缀 `wx` 替换为 `uni`，详见[uni-app接口规范](https://uniapp.dcloud.io/api/README)
- 数据绑定及事件处理同 `Vue.js` 规范，同时补充了App及页面的生命周期
- 为兼容多端运行，建议使用flex布局进行开发

## 环境搭建

安装编辑器HbuilderX  [下载地址](https://www.dcloud.io/hbuilderx.html)

HBuilderX是通用的前端开发工具，但为`uni-app`做了特别强化。

下载App开发版，可开箱即用

安装微信开发者工具 [下载地址](https://developers.weixin.qq.com/miniprogram/dev/devtools/download.html)

## 项目目录

[官网介绍]( [https://uniapp.dcloud.io/frame?id=%e7%9b%ae%e5%bd%95%e7%bb%93%e6%9e%84](https://uniapp.dcloud.io/frame?id=目录结构) )

```txt
┌─components            uni-app组件目录
│  └─comp-a.vue         可复用的a组件
├─hybrid                存放本地网页的目录，详见
├─platforms             存放各平台专用页面的目录，详见
├─pages                 业务页面文件存放的目录
│  ├─index
│  │  └─index.vue       index页面
│  └─list
│     └─list.vue        list页面
├─static                存放应用引用静态资源（如图片、视频等）的目录，注意：静态资源只能存放于此
├─wxcomponents          存放小程序组件的目录，详见
├─main.js               Vue初始化入口文件
├─App.vue               应用配置，用来配置App全局样式以及监听 应用生命周期
├─manifest.json         配置应用名称、appid、logo、版本等打包信息，详见
└─pages.json            配置页面路由、导航条、选项卡等页面类信息，详见
└─uni.sass              默认 CSS 的一些变量
```

## 全局/页面配置

### globalStyle 全局样式配置

用于设置应用的状态栏、导航条、标题、窗口背景色等。[详细文档](https://uniapp.dcloud.io/collocation/pages?id=globalstyle)

| 属性                         | 类型     | 默认值  | 描述                                                         |
| ---------------------------- | -------- | ------- | ------------------------------------------------------------ |
| navigationBarBackgroundColor | HexColor | #F7F7F7 | 导航栏背景颜色（同状态栏背景色）                             |
| navigationBarTextStyle       | String   | white   | 导航栏标题颜色及状态栏前景颜色，仅支持 black/white           |
| navigationBarTitleText       | String   |         | 导航栏标题文字内容                                           |
| backgroundColor              | HexColor | #ffffff | 窗口的背景色                                                 |
| backgroundTextStyle          | String   | dark    | 下拉 loading 的样式，仅支持 dark / light                     |
| enablePullDownRefresh        | Boolean  | false   | 是否开启下拉刷新，详见[页面生命周期](https://uniapp.dcloud.io/use?id=%e9%a1%b5%e9%9d%a2%e7%94%9f%e5%91%bd%e5%91%a8%e6%9c%9f)。 |
| onReachBottomDistance        | Number   | 50      | 页面上拉触底事件触发时距页面底部距离，单位只支持px，详见[页面生命周期](https://uniapp.dcloud.io/use?id=%e9%a1%b5%e9%9d%a2%e7%94%9f%e5%91%bd%e5%91%a8%e6%9c%9f) |

### pages配置页面

| 属性  | 类型   | 默认值 | 描述                                                         |
| ----- | ------ | ------ | ------------------------------------------------------------ |
| path  | String |        | 配置页面路径                                                 |
| style | Object |        | 配置页面窗口表现，配置项参考 [pageStyle](https://uniapp.dcloud.io/collocation/pages?id=style) |

`pages`**数组数组中第一项表示应用启动页**

### 配置tabbar

如果应用是一个多 tab 应用，可以通过 tabBar 配置项指定 tab 栏的表现，以及 tab 切换时显示的对应页。

**Tips**

- 当设置 position 为 top 时，将不会显示 icon
- tabBar 中的 list 是一个数组，只能配置最少2个、最多5个 tab，tab 按数组的顺序排序。

**属性说明：**

| 属性            | 类型     | 必填 | 默认值 | 描述                                                 | 平台差异说明                             |
| --------------- | -------- | ---- | ------ | ---------------------------------------------------- | ---------------------------------------- |
| color           | HexColor | 是   |        | tab 上的文字默认颜色                                 |                                          |
| selectedColor   | HexColor | 是   |        | tab 上的文字选中时的颜色                             |                                          |
| backgroundColor | HexColor | 是   |        | tab 的背景色                                         |                                          |
| borderStyle     | String   | 否   | black  | tabbar 上边框的颜色，仅支持 black/white              | App 2.3.4+ 支持其他颜色值                |
| list            | Array    | 是   |        | tab 的列表，详见 list 属性说明，最少2个、最多5个 tab |                                          |
| position        | String   | 否   | bottom | 可选值 bottom、top                                   | top 值仅微信小程序支持，并且不会显示图标 |

其中 list 接收一个数组，数组中的每个项都是一个对象，其属性值如下：

| 属性             | 类型   | 必填 | 说明                                                         |
| ---------------- | ------ | ---- | ------------------------------------------------------------ |
| pagePath         | String | 是   | 页面路径，必须在 pages 中先定义                              |
| text             | String | 是   | tab 上按钮文字，在 5+APP 和 H5 平台为非必填。例如中间可放一个没有文字的+号图标 |
| iconPath         | String | 否   | 图片路径，icon 大小限制为40kb，建议尺寸为 81px * 81px，当 postion 为 top 时，此参数无效，不支持网络图片，不支持字体图标 |
| selectedIconPath | String | 否   | 选中时的图片路径，icon 大小限制为40kb，建议尺寸为 81px * 81px ，当 postion 为 top 时，此参数无效 |

### condition启动模式

启动模式配置，仅开发期间生效，用于模拟直达页面的场景，如：小程序转发后，用户点击所打开的页面。

**属性说明：**

| 属性    | 类型   | 是否必填 | 描述                             |
| ------- | ------ | -------- | -------------------------------- |
| current | Number | 是       | 当前激活的模式，list节点的索引值 |
| list    | Array  | 是       | 启动模式列表                     |

**list说明：**

| 属性  | 类型   | 是否必填 | 描述                                                         |
| ----- | ------ | -------- | ------------------------------------------------------------ |
| name  | String | 是       | 启动模式名称                                                 |
| path  | String | 是       | 启动页面路径                                                 |
| query | String | 否       | 启动参数，可在页面的 [onLoad](https://uniapp.dcloud.io/use?id=%e9%a1%b5%e9%9d%a2%e7%94%9f%e5%91%bd%e5%91%a8%e6%9c%9f) 函数里获得 |

## 创建页面

[官方介绍](https://uniapp.dcloud.io/collocation/pages?id=pages)

创建简单。HBuild直接新建，配置见文档

## 常用组件

### text组件

**[text](https://uniapp.dcloud.io/component/text?id=text)**

文本组件。用于包裹文本内容。类似 `span` 标签

**属性说明**

| 属性名     | 类型    | 默认值 | 说明         | 平台差异说明        |
| :--------- | :------ | :----- | :----------- | :------------------ |
| selectable | Boolean | false  | 文本是否可选 |                     |
| space      | String  |        | 显示连续空格 | App、H5、微信小程序 |
| decode     | Boolean | false  | 是否解码     | App、H5、微信小程序 |

**space 值说明**

| 值   | 说明                   |
| :--- | :--------------------- |
| ensp | 中文字符空格一半大小   |
| emsp | 中文字符空格大小       |
| nbsp | 根据字体设置的空格大小 |

**Tips**

- `` 组件内只支持嵌套 ``，不支持其它组件或自定义组件，否则会引发在不同平台的渲染差异。
- 在app-nvue下，只有``才能包裹文本内容。无法在``组件包裹文本。
- decode 可以解析的有 ` ` `<` `>` `&` `'` ` ` ` `。

```
decode 可以解析的有 &nbsp; &lt; &gt; &amp; &apos; &ensp; &emsp;。
貌似现在平台都支持了，以前是不支持的
```

- 各个操作系统的空格标准并不一致。
- 除了文本节点以外的其他节点都无法长按选中。
- 支持 `\n` 方式换行。
- 如果使用 `` 组件编译时会被转换为 ``。

### view 组件

视图容器。它类似于传统html中的div，用于包裹各种元素内容。

如果使用[nvue](https://uniapp.dcloud.io/use-weex)，则需注意，包裹文字应该使用组件。

**属性说明**

| 属性名                 | 类型    | 默认值 | 说明                                                         |
| :--------------------- | :------ | :----- | :----------------------------------------------------------- |
| hover-class            | String  | none   | 指定按下去的样式类。当 hover-class="none" 时，没有点击态效果 |
| hover-stop-propagation | Boolean | false  | 阻止点击事件的冒泡                                           |
| hover-start-time       | Number  | 50     | 点击事件触发的延迟时间                                       |
| hover-stay-time        | Number  | 400    | 点击事件触发的持续时间                                       |

**Tips**

- 如果使用 `div` ，编译时会被转换为 `view`。

### button组件

**组件的属性**

|  属性名  |  类型   | 默认值  |           说明           |
| :------: | :-----: | :-----: | :----------------------: |
|   size   | String  | default |        按钮的大小        |
|   type   | String  | default |      按钮的样式类型      |
|  plain   | Boolean |  false  | 按钮是否镂空，背景色透明 |
| disabled | Boolean |  false  |         是否按钮         |
| loading  | Boolean |  false  | 名称是否带 loading 图标  |

- `button` 组件默认独占一行，设置 `size` 为 `mini` 时可以在一行显示多个

### image组件

[image](https://uniapp.dcloud.io/component/image?id=image)图片。

| 属性名 | 类型   | 默认值        | 说明                 | 平台差异说明 |
| ------ | ------ | ------------- | -------------------- | ------------ |
| src    | String |               | 图片资源地址         |              |
| mode   | String | 'scaleToFill' | 图片裁剪、缩放的模式 |              |

**Tips**

- `<image>` 组件默认宽度 300px、高度 225px；
- `src` 仅支持相对路径、绝对路径，支持 base64 码；
- 页面结构复杂，css样式太多的情况，使用 image 可能导致样式生效较慢，出现 “闪一下” 的情况，此时设置 `image{will-change: transform}` ,可优化此问题。
- 还有一些啥懒加载，加载动画，加载成功事件 等等

**mode ** 有13种模式，官网都有案例

### 还有其他的组件

#### 视图组件

+ 滚动视图 [scroll-view](https://uniapp.dcloud.io/component/scroll-view?id=scroll-view)
+  轮播图 [swiper](https://uniapp.dcloud.io/component/swiper?id=swiper)
+  可拖动区域组件 [movable-area](https://uniapp.dcloud.io/component/movable-view?id=movable-area)
+  可移动的视图容器 [movable-view](https://uniapp.dcloud.io/component/movable-view?id=movable-view)
+  覆盖在原生组件上的文本视图  [cover-view](https://uniapp.dcloud.io/component/cover-view?id=cover-view)
+  覆盖在原生组件上的图片视图 [cover-image](https://uniapp.dcloud.io/component/cover-view?id=cover-image)

#### 基础内容

+  图标  [icon](https://uniapp.dcloud.io/component/icon?id=icon)
+  富文本 [rich-text](https://uniapp.dcloud.io/component/rich-text?id=rich-text)
+  进度条 [progress](https://uniapp.dcloud.io/component/progress?id=progress)

#### 表单组件

+ 多选框 `checkbox`
+ 单选框 `radio`
+  富文本编辑器 
+ 表单  `form`
+ `input`
+ `label`
+  从底部弹起的滚动选择器  `picker`
+  嵌入页面的滚动选择器  `picker-view`
+ 滑动选择器  `slider`
+ 开关选择器  `switch`
+ 多行输入框  `textarea`

#### 导航

#### 媒体组件

#### 地图

#### 画布

#### 广告

。。。。。妈呀太多了把

## uni-app 样式

[页面样式与布局](https://uniapp.dcloud.io/frame?id=页面样式与布局)

+ rpx 即响应式px，一种根据屏幕宽度自适应的动态单位。以750宽的屏幕为基准，750rpx恰好为屏幕宽度。屏幕变宽，rpx 实际显示效果会等比放大。

+ 使用`@import`语句可以导入外联样式表，`@import`后跟需要导入的外联样式表的相对路径，用`;`表示语句结束

+ 支持基本常用的选择器class、id、element等
+ 在 `uni-app` 中不能使用 `*` 选择器。

+ `page` 相当于 `body` 节点
+ 定义在 App.vue 中的样式为全局样式，作用于每一个页面。在 pages 目录下 的 vue 文件中定义的样式为局部样式，只作用在对应的页面，并会覆盖 App.vue 中相同的选择器。

## 数据绑定

在页面中需要定义数据，和我们之前的`vue一摸一样`，直接在data中定义数据即可

```js
export default {
  data () {
    return {
      msg: 'hello-uni'
    }
  }
}
```

### 插值表达式的使用

+ 利用插值表达式渲染基本数据

  ```html
  <view>{{msg}}</view>
  ```

+ 在插值表达式中使用三元运算

  ```html
  <view>{{ flag ? '我是真的':'我是假的' }}</view>
  ```

+ 基本运算

  ```html
  <view>{{1+1}}</view>
  ```


### v-bind动态绑定属性

在data中定义了一张图片，我们希望把这张图片渲染到页面上

```js
export default {
  data () {
    return {
      img: 'http://destiny001.gitee.io/image/monkey_02.jpg'
    }
  }
}
```

利用v-bind进行渲染

```html
<image v-bind:src="img"></image>
```

还可以缩写成:

```html
<image :src="img"></image>
```

### v-for的使用

data中定以一个数组，最终将数组渲染到页面上

```js
data () {
  return {
    arr: [
      { name: '刘能', age: 29 },
      { name: '赵四', age: 39 },
      { name: '宋小宝', age: 49 },
      { name: '小沈阳', age: 59 }
    ]
  }
}
```

利用v-for进行循环

```js
<view v-for="(item,i) in arr" :key="i">名字：{{item.name}}---年龄：{{item.age}}</view>
```

## 事件

### 事件绑定

在uni中事件绑定和vue中是一样的，通过v-on进行事件的绑定，也可以简写为@

```html
<button @click="tapHandle">点我啊</button>
```

事件函数定义在methods中

```js
methods: {
  tapHandle () {
    console.log('真的点我了')
  }
}
```

### 事件传参

- 默认如果没有传递参数，事件函数第一个形参为事件对象

  ```js
  // template
  <button @click="tapHandle">点我啊</button>
  // script
  methods: {
    tapHandle (e) {
      console.log(e)
    }
  }
  ```

- 如果给事件函数传递参数了，则对应的事件函数形参接收的则是传递过来的数据

  ```js
  // template
  <button @click="tapHandle(1)">点我啊</button>
  // script
  methods: {
    tapHandle (num) {
      console.log(num)
    }
  }
  ```

- 如果获取事件对象也想传递参数

  ```js
  // template
  <button @click="tapHandle(1,$event)">点我啊</button>
  // script
  methods: {
    tapHandle (num,e) {
      console.log(num,e)
    }
  }
  ```

## 生命周期

> 官网链接： https://uniapp.dcloud.io/api/lifecycle 

### 应用的生命周期

>应用生命周期仅可在`App.vue`中监听，在其它页面监听无效。
>
>onlaunch里进行页面跳转，如遇白屏报错，请参考https://ask.dcloud.net.cn/article/35942

 `uni-app` 支持如下应用生命周期函数： 

| 函数名            | 说明                                                         |
| :---------------- | :----------------------------------------------------------- |
| onLaunch          | 当`uni-app` 初始化完成时触发（全局只触发一次）               |
| onShow            | 当 `uni-app` 启动，或从后台进入前台显示                      |
| onHide            | 当 `uni-app` 从前台进入后台                                  |
| onError           | 当 `uni-app` 报错时触发                                      |
| onUniNViewMessage | 对 `nvue` 页面发送的数据进行监听，可参考 [nvue 向 vue 通讯](https://uniapp.dcloud.io/use-weex?id=nvue-向-vue-通讯) |

### 页面的生命周期

| 函数名   | 说明                                                         |
| -------- | ------------------------------------------------------------ |
| onLoad   | 监听页面加载，其参数为上个页面传递的数据，参数类型为Object（用于页面传参），参考[示例](https://uniapp.dcloud.io/api/router?id=navigateto) |
| onShow   | 监听页面显示。页面每次出现在屏幕上都触发，包括从下级页面点返回露出当前页面 |
| onReady  | 监听页面初次渲染完成。                                       |
| onHide   | 监听页面隐藏                                                 |
| onUnload | 监听页面卸载                                                 |

## 下拉刷新

### 通过配置文件开启

需要在 `pages.json` 里，找到的当前页面的pages节点，并在 `style` 选项中开启 `enablePullDownRefresh`

之后就会在页面的 `onPullDownRefresh()` 函数中监听下拉刷新

### 通过调用全局函数开启

通过调用 uni.startPullDownRefresh 方法来开启下拉刷新，一般是用户自己触发了某些事件，我们在对应的自定义函数中使用这个方法。

调用了这个方法默认会触发 `onPullDownRefresh()` 函数。

### 关闭下拉的加载条

调用全局的 `uni.stopPullDownRefresh()` 函数

## 上拉加载

通过在pages.json文件中找到当前页面的pages节点下style中配置`onReachBottomDistance`可以设置距离底部开启加载的距离，默认为50px

触底的时候会触发 `onReachBottom` 函数

## 发送请求

在uni中可以调用 `uni.request` 方法进行请求网络请求

需要注意的是：在小程序中网络相关的 API 在使用前需要配置域名白名单。

官网： https://uniapp.dcloud.io/api/request/request 

```js
apiGet() {
    uni.request({
        url:"http://coderyl.top/node/ip",
        success(res) {
        	console.log(res)
        }
    })
}
```

## storage本地存储

 https://uniapp.dcloud.io/api/storage/storage?id=setstorage 

主要是如果本地没有数据然后去获取的话会成功但是返回值没有。

## 图片展示

## 条件注释

件编译是用特殊的注释作为标记，在编译时根据这些特殊的注释，将注释里面的代码编译到不同平台。

**写法：**以 #ifdef 加平台标识 开头，以 #endif 结尾。

平台标识

| 值         | 平台                                                   | 参考文档                                                     |
| ---------- | ------------------------------------------------------ | ------------------------------------------------------------ |
| APP-PLUS   | 5+App                                                  | [HTML5+ 规范](http://www.html5plus.org/doc/)                 |
| H5         | H5                                                     |                                                              |
| MP-WEIXIN  | 微信小程序                                             | [微信小程序](https://developers.weixin.qq.com/miniprogram/dev/api/) |
| MP-ALIPAY  | 支付宝小程序                                           | [支付宝小程序](https://docs.alipay.com/mini/developer/getting-started) |
| MP-BAIDU   | 百度小程序                                             | [百度小程序](https://smartprogram.baidu.com/docs/develop/tutorial/codedir/) |
| MP-TOUTIAO | 头条小程序                                             | [头条小程序](https://developer.toutiao.com/dev/cn/mini-app/develop/framework/basic-reference/introduction) |
| MP-QQ      | QQ小程序                                               | （目前仅cli版支持）                                          |
| MP         | 微信小程序/支付宝小程序/百度小程序/头条小程序/QQ小程序 |                                                              |

### 组件的条件注释

代码演示

```html
<!-- #ifdef H5 -->
<view>
  h5页面会显示
</view>
<!-- #endif -->
<!-- #ifdef MP-WEIXIN -->
<view>
  微信小程序会显示
</view>
<!-- #endif -->
<!-- #ifdef APP-PLUS -->
<view>
  app会显示
</view>
<!-- #endif -->
```

### api的条件注释

代码演示

```js
onLoad () {
  //#ifdef MP-WEIXIN
  console.log('微信小程序')
  //#endif
  //#ifdef H5
  console.log('h5页面')
  //#endif
}
```

样式的条件注释

代码演示

```css
/* #ifdef H5 */
view{
  height: 100px;
  line-height: 100px;
  background: red;
}
/* #endif */
/* #ifdef MP-WEIXIN */
view{
  height: 100px;
  line-height: 100px;
  background: green;
}
/* #endif */
```

## 导航跳转

### 声明式导航

利用navigator进行跳转

navigator详细文档：[文档地址](https://uniapp.dcloud.io/component/navigator)

| 属性名    | 类型   | 默认值   | 说明                                                         |
| :-------- | :----- | :------- | :----------------------------------------------------------- |
| url       | String |          | 应用内的跳转链接，值为相对路径或绝对路径，如："../first/first"，"/pages/first/first"，注意不能加 `.vue` 后缀 |
| open-type | String | navigate | 跳转方式                                                     |

**open-type 有效值**

| 值        | 说明                       |
| :-------- | :------------------------- |
| navigate  | 对应 uni.navigateTo 的功能 |
| redirect  | 对应 uni.redirectTo 的功能 |
| switchTab | 对应 uni.switchTab 的功能  |

跳转到普通页面用 `navigate`，跳转到导航中的页面用 `switchTab`，用`redirect` 值的时候会触发当前页面卸载的生命周期

### 编程式导航

 https://uniapp.dcloud.io/api/router?id=navigateto 

注意看文档，有的方法跳转的时候会关闭所有其他页面，有的只会关闭当前跳转的页面

### 跳转参数传递

传递参数，类似 `get`请求的 `url` 直接在链接中拼写就行

接收参数，在跳转的页面的 `onLoad`钩子函数中接收

## 组件

### 创建

直接创建  .vue文件就行，在用的时候import导入一下，然后在 components 中注册一下就能使用了

### 生命周期

组件的生命周期函数和 其他的有点不一样，组件的生命周期函数完全和 vue生命周期是一致的

| 函数          | 说明                                                         |
| ------------- | ------------------------------------------------------------ |
| beforeCreate  | 在实例初始化之后被调用。[详见](https://cn.vuejs.org/v2/api/#beforeCreate) |
| created       | 在实例创建完成后被立即调用。[详见](https://cn.vuejs.org/v2/api/#created) |
| beforeMount   | 在挂载开始之前被调用。[详见](https://cn.vuejs.org/v2/api/#beforeMount) |
| mounted       | 挂载到实例上去之后调用。[详见](https://cn.vuejs.org/v2/api/#mounted) 注意：此处并不能确定子组件被全部挂载，如果需要子组件完全挂载之后在执行操作可以使用`$nextTick`[Vue官方文档](https://cn.vuejs.org/v2/api/#Vue-nextTick) |
| beforeUpdate  | 数据更新时调用，发生在虚拟 DOM 打补丁之前。[详见](https://cn.vuejs.org/v2/api/#beforeUpdate) |
| updated       | 由于数据更改导致的虚拟 DOM 重新渲染和打补丁，在这之后会调用该钩子。[详见](https://cn.vuejs.org/v2/api/#updated) |
| beforeDestroy | 实例销毁之前调用。在这一步，实例仍然完全可用。[详见](https://cn.vuejs.org/v2/api/#beforeDestroy) |
| destroyed     | Vue 实例销毁后调用。调用后，Vue 实例指示的所有东西都会解绑定，所有的事件监听器会被移除，所有的子实例也会被销毁。[详见](https://cn.vuejs.org/v2/api/#destroyed) |

### 组件通信

和vue 一样

#### 父向子

父组件通过自定义属性给子组件传值

子组件用 props属性接收传递的参数值

#### 子向父

子组件用  `$emit`触发父组件的自定义事件来修改值

#### 兄弟之间

可以用共同的父组件来作为桥梁进行通信

也可以用 全局的事件来通信

在B组件 created生命周期中定义全局函数

```js
created() {
    uni.$on("updateBNum", (temp) => {
    	this.num += temp	
    })
}
```

在A组件中触发这个全局函数

```js
addBNum() {
	uni.$emit("updateBNum", 5)
}
```

## uni ui

扩展组件：https://uniapp.dcloud.io/component/README?id=uniui 