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