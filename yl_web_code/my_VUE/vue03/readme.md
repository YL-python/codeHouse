### 过滤器
数据库时间储存格式  时间戳
时间  2007.10.11   2007/01/11  2007年10月11日 
对数据的处理

1. 全局过滤器 Vue.filter(过滤器名,处理函数)
2. 局部过滤器 组件或者实例里的配置项filters:{过滤器名,处理函数} 

### 监听watch 
watch 是配置项的一种 主要功能是监听数据的改变


### 人生
人生如戏 大悲咒
0-1-0
猥琐发育别浪
入世
打怪升级更新自己
在世
离世
回顾一生 寻找遗憾解决遗憾

#### 生命周期
 4（4个阶段） 8（每个阶段2个钩子函数） 2（缓存的钩子） 1（捕获错误的钩子函数）
vue（实例）组件的一生和人生及其想似

beforeCreate
创建 创建虚拟dom create
created
beforeMount
挂载  虚拟dom 变成真实dom 出现在页面上 在世
mounted 
beforeUpdate
更新  更新数据->更新dom元素
updated
beforeDestory
销毁  组件离世的时候
destroyed

常用 
created 网络请求
mounted 网络请求 初始化dom
beforeDestory/destroyed 组件销毁前擦屁股解决遗憾

### eslint
帮助我们代码更加规范 错误非常多
流派 
tab 2空格 4空格
{} 换行流  
function test(){

} 

function test()
{
  
} 
### 脚手架项目的基本目录
src  源码目录
  main.js 入口文件
  xx.vue  单文件组件
public 公有资源
node_module 依赖包
package.json 项目依赖
readme 项目提示

### vue的脚手架工具
将npm镜像换成淘宝镜像
npm install  -g @vue/cli
vue -V  出现版本号
新建一个文件 
进入文件目录 执行 
vue create name (名字随便起)
进入项目目录 执行npm run serve
