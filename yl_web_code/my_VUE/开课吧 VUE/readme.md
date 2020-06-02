# 开课吧 Vue

# 组件传值，通信

### 父组件=>子组件

+ **方法一**

```js
// child
props: { msg: String }

// parent
<HelloWorld msg="Welcome to Your Vue.js App"/>
```

父组件通过标签定义属性给子组件传递值，子组件在使用props接收值

+ **方法二**

```js
// parent
<HelloWorld ref="hw"/>

this.$refs.hw.xx = 'xxx'
```

通过给标签添加ref属性，父组件 就能通过 `this.$refs.hw.xx` 获取到子组件data 内的 xx值，不过要找 mounted()生命周期之后。父组件会比子组件先挂载

+ **方法三**

```js
// parent
this.$children[0].xx = 'xx
```

父组件通过 $children 可以获取到所有的子组件，是一个数组。

官方文档说了，子元素的顺序不能被保证

### 子组件 => 父组件 

+ **方法一**

```js
// child
this.$emit('add', good)

// parent
<Cart @add="cartAdd($event)"></
```

通过自定义事件来通信

看上去是子组件派发事件，父组件监听事件，观察者模式

实际上派发者和监听者都是父组件

### 兄弟组件通信

```js
// brother1
this.$parent.$emit('foo')

// brother2
this.$parent.$on('foo', handle)
```

兄弟一通过父组件派发一个 foo 事件

兄弟二在created()声明周期通过父组件监听 foo 事件

### 跨多代传参

+ **方法一**

> provide/inject：能够实现祖先给后代传值, 是vue提供的API,平时少用,组件开发人员用的多

```js
// 祖先
provide() {
	return {foo: 'foo'}
}

// 后代
inject: ['foo']
```

祖先使用 provide 注册一些数据

后代用 inject 取出来使用

看官方文档,这个属性传递的数据不是动态的,除非是传递了 动态的数据

+ **方法二**

>  事件总线：创建一个Bus类负责事件派发、监听和回调管理

```js
// Bus：事件派发、监听和回调管理
class Bus{
    constructor(){
        // {
        // eventName1:[fn1,fn2],
        // eventName2:[fn3,fn4],
        // }
        this.callbacks = {}
    }
    $on(name, fn){
        this.callbacks[name] = this.callbacks[name] || []
        this.callbacks[name].push(fn)
    }
    $emit(name, args){
        if(this.callbacks[name]){
        	this.callbacks[name].forEach(cb => cb(args))
        }
    }
}
// main.js
Vue.prototype.$bus = new Bus()
// child1
this.$bus.$on('foo', handle)
// child2
this.$bus.$emit('foo')
```

创建一个新的bus 类,专门来 派发事件和监听事件

当然可以直接 `Vue.prototype.$bus = new Vue()`

和兄弟组件传值的方法一是一样的道理,只不过用了一个全新的对象来管理 事件

## 插槽 slot

### 匿名插槽

```html
// comp1
<div>
	<slot></slot>
</div>

// parent
<comp>hello</comp>
```

父组件在子组件标签内写的内容会被子组件的 `slot` 标签 替换

### 具名插槽

```html
// comp2
<div>
    <slot></slot>
    <slot name="content"></slot>
</div>
// parent
<Comp2>
    <!-- 默认插槽用default做参数 -->
    <template v-slot:default>默认插槽</template>
    <!-- 具名插槽用插槽名做参数 -->
    <template v-slot:content>具名插槽</template>
</Comp2>
```

具名插槽是2.6版本推出的,可以给`solt`标签取名字,在夫组件内具体使用的时候,用template 标签包裹插槽内容,用`v-solt`指令指定插槽的名字

### 作用域插槽

```html
// comp3
<div>
	<slot :foo="foo"></slot>
</div>

// parent
<Comp3>
    <!-- 把v-slot的值指定为作用域上下文对象 -->
    <template v-slot:default="ctx">
    	来自子组件数据：{{ctx.foo}}
    </template>
</Comp3>

```

有点晕,貌似就是可以传递数据的写法, 然后就是 v-solt 可以简写成一个 # 

> 官方插槽介绍文档: https://cn.vuejs.org/v2/guide/components-slots.html