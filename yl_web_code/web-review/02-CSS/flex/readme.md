# flex

> 来自阮一峰教程
>
> 语法介绍：http://www.ruanyifeng.com/blog/2015/07/flex-grammar.html
>
> 实例：http://www.ruanyifeng.com/blog/2015/07/flex-examples.html

## 基本概念
![基本概念](./2基本概念.png)

## 容器的属性

### 修改主轴方向

![flex-direction属性](D:\CodeHouse\yl_web_code\web-review\02-CSS\flex\flex-direction.png)

### 修改项目排列方式

![flex-wrap属性](D:\CodeHouse\yl_web_code\web-review\02-CSS\flex\flex-wrap.png)

###  flex-flow

```
flex-flow属性是flex-direction属性和flex-wrap属性的简写形式，默认值为row nowrap。

.box {
  flex-flow: <flex-direction> || <flex-wrap>;
}
```

### 修改主轴上的对齐方式

![justify-content属性](D:\CodeHouse\yl_web_code\web-review\02-CSS\flex\justify-content.png)

### 修改交叉轴对齐方式

![align-items](D:\CodeHouse\yl_web_code\web-review\02-CSS\flex\align-items.png)

### 修改多轴线对齐方式

> 容器有多行的时候才会起作用

![align-content属性](D:\CodeHouse\yl_web_code\web-review\02-CSS\flex\align-content.png)

## 项目的属性

### 修改项目的排列顺序

![order属性](D:\CodeHouse\yl_web_code\web-review\02-CSS\flex\order.png)

### 修改项目的大小

> flex-shrink/flex-grow是设置一个比例值，flex-basis是设置一个具体值

![flex-grow](D:\CodeHouse\yl_web_code\web-review\02-CSS\flex\flex-grow.png)

![flex-shrink](D:\CodeHouse\yl_web_code\web-review\02-CSS\flex\flex-shrink.png)

![](D:\CodeHouse\yl_web_code\web-review\02-CSS\flex\flex-basis.png)

### 修改项目的对齐方式

![align-self](D:\CodeHouse\yl_web_code\web-review\02-CSS\flex\align-self.png)