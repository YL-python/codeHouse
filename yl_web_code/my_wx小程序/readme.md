# 微信小程序

https://mp.weixin.qq.com/  官网注册账号

https://developers.weixin.qq.com/miniprogram/dev/devtools/stable.html  开发工具下载



开发者工具新建项目，就最基本项目，不要云不要插件模板。

AppId：wxddafcc971f5e7e8b

## demo介绍

生成的文件中

json结尾文件一般是配置文件

js结尾文件写js业务逻辑

wxml 结尾文件是 wxhtml 用的是wx内置的组件 

wxss 结尾文件是 wxcss 微信的样式

一开始sitemap.json文件就是配置可以忽略。project.config.json也是配置文件，不过找个文件里面配置了 AppId，使用别人的代码的时候需要修改 AppId 代码才能跑起来

小程序都需要一个app实例 （根实例）包含了若干个页面（实例）

app.js  小程序的实例 小程序的入口文件
app.json 小程序的全局配置
app.wxss  小程序的全局样式
pages  小程序里的页面
-home   home页面
  |   
  home.js home页面实例
  home.json  home页面的配置文件
  home.wxss  home页面的样式
  home.wxml  home的页面骨架
-my     我的页面
 ....



## app.jsop

### pages配置

路径数组，且第一项就是要展示的页面

### 样式

全局样式和局部样式，采用就近原则

正常写css  就行

响应式：

平时的rem在小程序中没有

小程序中有rpx，且小程序中不管什么手机宽度恒定为750rpx，小程序的设计稿一般是750*1136

或者使用vw   vh

无法直接使用预处理语言

### 骨架 -- xx.wxml文件

不能使用html元素，只能使用小程序内置的组件标签

详情见文档https://developers.weixin.qq.com/miniprogram/dev/component/view.html

### 配置

#### app.json 全局配置

https://developers.weixin.qq.com/miniprogram/dev/reference/configuration/app.html

#### xxx.json 局部配置

冲突的时候就近原则

### 小程序逻辑

https://developers.weixin.qq.com/miniprogram/dev/reference/api/App.html

小程序第一次启动

小程序隐藏

小程序显示



页面渲染功能相关

页面加载

只有页面重新加载会触发，tabbar上的页面会被缓存，不会被销毁



事件：

[https://developers.weixin.qq.com/miniprogram/dev/framework/view/wxml/event.html#%E4%BA%8B%E4%BB%B6%E7%9A%84%E4%BD%BF%E7%94%A8%E6%96%B9%E5%BC%8F](https://developers.weixin.qq.com/miniprogram/dev/framework/view/wxml/event.html#事件的使用方式)

绑定函数

参数传递

```html
<!-- 传参需要用data-变量名  然后在定义的方法内用事件对象接收
传递对象数据的时候要用插值法 不加空格识别不出来你敢信 -->
<button bindtap="changeName"
  data-hehe="xx123" data-xixi="123456"
  data-arr="{{[1,2,3,4]}}"
  data-obj="{{ {us:123,ps:456} }}"
>改名</button>
<!-- <button bind:tap="changeName">改名</button> -->
```

### 指令

https://developers.weixin.qq.com/miniprogram/dev/reference/wxml/list.html

wx:for

wx:if

