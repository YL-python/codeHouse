# 社区交友

PHP： https://www.bilibili.com/video/BV1ct411S7nj?from=search&seid=16143128944707147642 

## 调试

推荐最先使用手机端真机调试，之后再用一些小程序，H5平台调试。

## 项目进展

### 前期准备

+ 引入官网css样式

+ 引入阿里巴巴图标

```
@font-face {
	font-family: "iconfont";
	src: url('data:application/x-font-woff2;...') format('woff2');
}
只要引入这两个就够了  啥ttf  woff文件不需要引入
```

+ 引入animate动画库

```
// 点击效果
<view class="animated" hover-class="fadeIn">点击效果</view>
// v-if
// 列表渲染
```

+ 全局配置

+ 基础介绍

```
view 组件
hover-class 指定按下去的样式，hover也能实现，但是hover在手机上就会出现松手之后不消失
hover-start-time，hover-stay-time，按下去多久出现样式，松手后样式保留多久

text组件
selectable 传值是布尔值，给字符串不管是啥都是true，可以用v-bind绑定一下。
:selectable='false'

class 和 style 的动态绑定

// 常用事件
点击事件 移动端推荐使用tap，其他的推荐使用 click
.stop阻止事件冒泡

// template 和 block 标签
https://uniapp.dcloud.io/frame?id=template-block
```

## 项目总结

### scroll-view 横向滚动样式需求

```
scroll-view 样式需是 width: 100%; white-space: nowrap;
内部 view 需要是 display: inline-block !important;
```

### 导航栏页面联动效果

顶部横向导航栏，下面内容区域，点导航栏切换对应的内容，内容页面可以左右滑动也切换导航栏

```
顶部导航栏用 scroll-view 没啥问题
内容区域要换成 swiper
两个的联动-- scroll-view有个scroll-into-view属性，swiper监听 @change 事件就能获取到轮播图下标，用current属性就能指定显示那个页面， data中用个数据连接把这两个属性连接起来

swiper内容要能滚动又要用 scroll-view 组件包裹，但是swiper 有固定的高度，我们就要自己计算出来高度，然后在设置

// 减 顶部导航栏的高度
this.scrollH = uni.getSystemInfoSync().windowHeight - uni.upx2px(101)

然后 swiper标签和 是wiper内部的 scroll-view 标签都需要设置这个高度
```

### flex布局 

```
flex布局 父容器内部四个子容器，其中三个要在左边，一个要在右边
给右边的加 margin-left: auto; 就能实现这个样式
```

### 图片上传功能

```
改的官方组件，上传功能就把 接收到的图片列表 通过emit通知父组件就好了
右上角的 删除功能，样式就定位，实现就是对 imageList数组删除一个然后通知父组件发生了改变
```

### 图片

```
最好固定大小
一般是高度给固定值，宽度是100%
或者宽高都是固定值
```

### 文字益处隐藏

```css
.text-ellipsis {
	overflow: hidden;
	text-overflow: ellipsis;
	white-space: nowrap;
	lines: 1;
}
```

