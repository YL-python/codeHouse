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
   a.状态提升  父子和子父结合 --- 亲兄弟
   b.事件总线 eventbus --- 远亲状态 
   c.全局状态管理          
