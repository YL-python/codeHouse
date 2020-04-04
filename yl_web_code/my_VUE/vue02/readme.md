### 什么是vue
前端框架的3马车 
angular  谷歌公司   m(数据)v（视图）c（控制器）   双向数据绑定
react    facebook （非死不可） 视图层的框架view  虚拟dom
vue      尤玉溪  双向数据绑定+虚拟dom
是一套用于构建用户界面的渐进式框架 
入门难度最低
### 为什么要学习vue 
高效 
1.运行效率高 采用虚拟dom 减少真实dom的操作使项目的运行效率大大提高
2.开发效率高 采用了组件化开发 
将开发者的精力从dom操作解放出来，转移到数据操作上

#### 爱上vue 3 5
什么叫做热爱 无时无刻的思念 
写页面使用vue 抛弃原来二阶段的写法（直接操作dom）

### vue的实例化
```
1.下载引入
2.找一个dom元素 这个dom要被vue控制
3.在js中实例化vue
```

### 数据绑定


### 指令 directive 
指令后面跟的都是表达式或者变量 

内置指令 vue内部提供的直接使用
自定义指令 实现自定义某些功能的指令 

条件渲染
 都可以控制一个元素的显示或者隐藏
  v-show  通过样式 display：none 
  v-if    直接控制div元素有还是没有 （v-else  v-elseif）
事件绑定
  使用vue中的事件  
  v-on：事件名（和原生js的事件名一致）:事件的处理函数 
  @事件名:事件处理函数
  事件的处理函数写在实例的配置项 motheds 
  处理函数的默认参数是事件对象
  如果需要传递其他参数 事件对象需要通过`$event 手动传递
属性绑定 
  v-bind
  元素的属性都是跟的固定的值 
  属性绑定可以实现 属性的后方跟变量或者表达式
  v-bind：要绑定的属性名 <img v-bind:src=''>
  :要绑定的属性名  <img :src=''>
列表渲染
v-for 数组 表格 数字  字符串
<td v-for ="(item,index) in/of 数据源"> </td> 
<td v-for ="(value,key,index) in/of 数据源"> </td> 

双向数据绑定 v-model 
v-model 相当于 事件绑定v-on 和属性 v-bind 集合体
将表单元素和data里的数据进行绑定 任何一方发生改变另一方都会跟着变
1. 表单元素可以使用
2. 组件也可用
#### 作业
1. todolist 敲熟
2. 实现一个99乘法表
3. 创建一个表格 
     a.隔行变色
     b.鼠标滑过有特效
     c.写一个下拉菜单 可以控制隔行变色的颜色

v-html 相当于innerhtml
v-text 相当于innerText
#### 自定义指令
全局自定义指令
```
Vue.directive('指令的名字',{
  insterted(el){
    el  自定义指令绑定的元素
  }
})
v-自定义指令的名字
```
局部自定义指定 在哪注册在哪用 
组件和实例都可以注册局部自定义指令
```
new Vue({
  directives:{
    自定义指令的名字:{
      inserted(el){

      }
    }
  }
})
```
#### 组件
1.创建组件 2.注册组件 3.使用组件
局部组件 全局组件 的区分就是注册位置不同
全局的
Vue.component('组件名',{ 组件的配置项})
局部的
new Vue({
  ...
  components:{
    组件名：{
      配置项
    },
    hehe:{
      template:'#hehe',
      components:{
        xixi:{
          template:'#xixi',
          components:{
            ....
          }
        }
      }
    }
  }
})
#### 组件的配置项和实例配置的区别
绑定元素   el       template 
数据      data 对象 data 函数
自定义指令 directive  directive
方法      methods    methods
组件  
计算属性
监听
....

#### 组件通信
在组件和实例中自己的数据只有自己可以控制
1. 父子通信 props
   父组件控制子组件 父组件控制自己的数据变化，将变化后的数据通过props自定属性传子组件
2. 子父通信 $emit 
   子组件控制父组件的数据  父组件控制自己的数据变化，将控制函数通过emit自定义事件传递子组件 供子组件调用 
3. 兄弟通信
   a.状态提升
   b.事件总线
   c.全局状态管理         

### vue的脚手架工具
将npm镜像换成淘宝镜像
npm install  -g @vue/cli
vue -V  出现版本号
新建一个文件 
进入文件目录 执行 
vue create name (名字随便起)
进入项目目录 执行npm run serve