### vue总结

#### vue01 - 基础指令
##### 数据绑定

##### v-if   v-show

##### v-on

  `v-on:click  ===  @click` 

##### 响应式的数据

##### v-bind
  `v-bind:src === :src`

##### v-for
  ```
  <li v-for='循环数据的每一项 in/of 要循环的数据'></li>
  <li v-for='(循环数据的每一项,每一项的下标)in/of 要循环的数据'></li>
  <li v-for="(对象value,对象里的key,下标) in 要循环的对象">{{key}}:{{value}}-{{index}}</li>
  ```

##### v-model  [官网 v-model介绍](https://cn.vuejs.org/v2/guide/forms.html)
  `双向数据绑定，表单绑定`

##### 自定义指令  [官网自定义指令](https://cn.vuejs.org/v2/guide/custom-directive.html#ad)
  `全局，局部`

##### v-html     v-text

#### vue02 - 组件
##### 组件的介绍

  ```
  组件继承于实例，所以实例有的在组件内都有，组件和实例会有差别
  组件的目的是为了实现复用
  // 组件的创建
  let xixi = Vue.extend({template: "<h1>这里是组件</h1>"})
  // 注册一个组件 Vue.component('组件的名字',创建的组件)
  Vue.component('Hehe', xixi)
  // 把组件名当成标签名来使用 组件名不能喝标签名一直
  ```

##### 全局组件和局部组件

##### 组件的配置项
  ```
  template <=> el -> 关联dom元素
  dom结构简单 直接使用字符串 
  dom复杂   template标签 该标签不会真正的渲染 值允许有一个根元素
  data方法返回对象 <=> data对象 -> 定义组件的数据
  data是方法是为了保证每一个组件有单独的作用域，组件只能用自己的数据
  methods <=> methods -> 定义组件的方法
  directives <=> directives -> 定义组件的自定义指令
  components <=> components -> 定义组件的组件，也就是组件嵌套
  ```

##### 父子组件通信

  ```
  父组件可以通过v-bind 动态控制子组件属性的属性值，从而传递数据给子组件
  子组件只能用不能修改
  子组件通过 props 接收属性值
  ```

##### 子父组件通信

  ```
  子组件并不能传递数据给父组件
  父组件可以 v-on传递自己的方法给 子组件自定义事件
  子组件可以通过$emit方法触发这个自定义事件（也就是父组件的事件），通过父组件的事件修改父组件的值
  ```

##### 兄弟组件的通信

  ```
  不能直接通信
  方法一状态提升：兄弟组件通信可以两个操作共有父组件的数据
方法二事件总线：两个多层嵌套组件通信时注册一个空实例（观察者），在一个组件里面把数据和方法绑定到这个观察者上，在另一个组件内使用这个观察者
  ```

#### vue03 - 边边角角和生命周期
##### [过滤器](https://cn.vuejs.org/v2/guide/filters.html#ad)

  用管道符号使用过滤器，用呵呵方法处理time值，呵呵是一个方法，默认参数就是管道符号前面的，当然也可以自定义参数

  ```
  {{time|hehe}}
  {{time|hehe('-')}}
  Vue.filter('hehe', (data, params = '.') => {
      // 对数据做处理
      console.log('需要过滤的数据', data)
      let y = (new Date(data)).getFullYear()
      let m = (new Date(data)).getMonth() + 1
      let d = (new Date(data)).getDate()
      // 一定要返回
      return `${y}${params}${m}${params}${d}`
  })
  ```

#####   监听-watch

```
监听数据的改变，key是数据，value是一个函数，默认有两个参数，一个是改变后的值，一个是改变前的值。
watch监听触发的时候 dom 还没有更新 所以数据是更改之后的但是dom 是更改之前的
```

##### 计算属性-computed

```
与data的数据关联 返回处理过之后的数据，computed的值不可以在data中定义和赋值
```

##### 获取标签-refs

```
通过ref绑定一个dom元素
通过 this.$refs 获取绑定的dom 元素 this 实例对象组件对象
document.getElementById('hehe')
this.$refs.xixi
```
##### 插槽

```
组件标签中的内容不会被渲染
slot 相当于开启一段空间来存放组件标签中的内容
```

##### 轮播图插件-swiper

```
xxx
```

##### 生命周期
```
4个阶段，每个阶段两个钩子函数，另外有两个缓存的钩子函数，以及一个捕获错误的钩子函数
创建：创建VUE虚拟dom对象
	beforeCreate()
		创建之前执行，没有数据，没有dom
	created()
		创建结束执行，有数据，没有dom
		可以用来做数据的初始化
挂载：将虚拟odm对象渲染到页面上
	beforeMount()
		挂载之前执行，有数据，没有dom
	mounted()
		挂载结束执行，有数据，有dom
		经常用来做一些初始化
更新：虚拟dom渲染到页面之后会时时监听数据会不会发生改变 ！
    beforeUpdate()
    	数据变化之前执行，虚拟dom数据更新了，页面上没有更新
    updated()
    	数据变化之后执行，虚拟dom数据更新了，页面上更新了
    	在这个方法内严禁修改数据，不然会发生死循环
销毁：虚拟dom存在，页面渲染数据丢失，通常用来做一些擦屁股操作
    beforeDestroy()
    	销毁之前发生，虚拟dom数据和页面渲染数据都有
    destroyed()
    	销毁之后发生，虚拟dom数据有，页面渲染数据丢失
```

#### vue04 - 脚手架以及路由
##### 一个轮播图，一个todolist例子

##### 单页面开发

##### 动态组件

```
动态组件 is 属性 可以指定渲染某一个组件 
使用is属性的标签不会被渲染
为了语义化 一般使用vue提供的component标签
```
##### 路由

```
下载--创建路由表--注册路由
<router-link to  tag  active-class >
<router-view> 
路由模式： hash， history
命名路由，命名视图，重定向，声明式导航和编程式导航
```

##### 路由传参

```
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
```

##### 嵌套路由 (子路由)

```
1. 路由表形成嵌套 子路由路径不加/
2. 在目标组件里 在嵌套一个router-view
```

##### 路由守卫 （拦截器）[官网](https://router.vuejs.org/zh/guide/advanced/navigation-guards.html#%E5%85%A8%E5%B1%80%E5%89%8D%E7%BD%AE%E5%AE%88%E5%8D%AB)

```
前置守卫，后置守卫，独享守卫
```

#### vue07 - vuex
##### 简介

```
全局状态管理
1. 多组件共享状态 多个组件使用同一个数据
2. 任何一个组件发生改变 其他的组件也要跟着发生相应的变化
```

##### 核心

```
state
	存放全局状态数据
	this.$store.state.XXX  使用XXX属性
mutation
	规定只有mutation才能修改state 组件中通过commit方法触发
	this.$store.commit('changeName',{name:123})
action
	可以放异步操作 触发mutation,组件中通过dispatch触发
	this.$store.dispatch('changeAge',{name:123,age:456})
	在action内定义的函数通过commit触发mutation
getter
	vuex里的计算属性 和state值进行关联
	组件内：this.$store.getters.XXX 使用XXX属性
```

##### 一般流程

```
0. store内定义全局变量方法等
1. 组件里通过 this.$store.state.XXX 获取全局状态数据进行渲染
2. 组件里通过  this.$store.dispatch('方法名',参数)方法 触发action里的方法
3. action内的方法通过commit触发mutation进行修改全局状态值
```

##### 辅助函数

```
我们发现使用vuex内的值还是要写一大推，就推出了辅助函数简化
值类型向计算属性映射，（State，Getters）=> computed
mapState: 将全局状态管理的state值映射到 组件的计算属性
	computed: {
    	...mapState(["name", "age", "sex"])
  	}  或者
  	computed: {
    	...mapState({
    		XXX:state=>state.YYY
    	})
  	}
 mapGetters: 将全局状态管理的getters值映射到使用组价的计算属性
 	computed: {
    	...mapGetters(["name", "age", "sex"])
  	}  或者
  	computed: {
    	...mapGetters({
    		XXX:'YYY'  // 把YYY Getters属性在组件内取名为XXX
    	})
  	}
函数类型向methods进行映射，（State，Getters）=> computed
mapMutations: 将mutation的值映射到方法里,**使用的时候  this.方法名**
	methods: {
    	...mapMutations(["changeName"])
  	}  或者
  	methods: {
    	...mapMutations({
    		XXX:"YYY"  // 把YYY方法注册为XXX
    	})
  	}
mapActions：将actions里的值映射到方法
	methods: {
    	...mapActions(["changeNameAction"])
  	}  或者
  	methods: {
    	...mapActions({
    		XXX:"YYY"  // 把YYY方法注册为XXX
    	})
  	}
```

##### 模块化

```
1.模块化之后state的取值需要添加一级模块名 其他的三个核心不变
2.可以在模块里添加命名空间  namespaced:true
	作用就是在 mutation getters actions的名字前面 添加模块名
	用处就是防止名字冲突
```

