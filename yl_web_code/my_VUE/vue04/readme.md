#### 项目分类
1. spa single page web application 单页面应用  只有一个html
   a.seo优化不好 
   b.首屏加载过慢 首屏白屏
   c.页面切换的用户体验好
2. mpa 多页面应用  多个html

#### 组件切换1 动态组件
<div is = 'hehe'></div> 
is 可以指定渲染的组件名
div 渲染成一个叫呵呵的组件
推荐与component 标签一起使用

#### 组件切换2 路由
监听地址栏的改变 根据改变渲染不同的组件

基本使用
1. 下载安装路由  npm install vue-router
2. 创建路由表  
    a. 引入vue 和vue-router 
    b. 在vue中使用vue-router 
    c. 创建路由实例 确定路径和组件的对应关系
    d. 抛出路由实例
3. 在main.js 注册路由
4. 就可以使用2个组件
 <router-link to  tag  active-class >  
 控制地址栏改变 
 <router-view>  开启一片空间渲染指定的组件

 路由的模式 mode 哈希 和历史
 通过路由表里 mode 设置 
 hash 路由 地址栏中有# 
 history 路由 没有# 和正常使用的类似
 命名路由
 命名视图
 重定向
 声明式导航 和编程式导航
  <a href='www.baidu.com'/>
  window.location.href='www.baidu.com'
  
  <router-link > 进行组件切换叫做 声明式导航
  通过路由对象下的api 进行切换叫做编程式导航
  vm.$router  push  replace go back forward
  push 会将组件加入到缓存栈  可以一级一级返回
  replace  没有加入缓存栈   回到最初的起点

#### 路由传参 切换组件的时候给目标组件传一个参数 
1. 切换的时候传递参数
2. 切换完毕 在目标组件接受参数

动态路由   
路由的路径中的有1项或者几项是变量可以变化
在目标组件 通过 $route.params 来接受数据
routes:[
  {
    path:'/login/:hehe/:xixi'
  }
]
query传参 
  相当于get 传递参数 数据会出现在地址栏上 缺少安全性 有数据长度限制
  this.$router.push('/name?us=123$ps=123')
  this.$router.push({path:'/name',query:{us:123,ps:123}})
  在目标组件里通过this.$route.query()进行接受
params传参
  不会出现在地址栏上 没有长度限制问题
  不能和path一起使用
  this.$router.push({name:"hehe",params:{us:123,ps:123}})
  在目标组件里通过  this.$route.param()接受

#### 嵌套路由 (子路由)
1. 路由表形成嵌套 子路由路径不加/
routes:[
  {
    path:"/my",
    component:My,
    children:[
      {path:'userInfo',component:UserInfo}
    ]
  }
]
2. 在目标组件里 在嵌套一个router-view

#### 路由守卫 （拦截器）
1. 某些页面登录之后才能访问 没有登录不等访问 

#### 作业
http://ustbhuangyi.com/music/#/recommend 
参考网站 实现 一级路由的切换
实现推荐页面的布局 数据本地写死就行