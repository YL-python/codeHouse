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