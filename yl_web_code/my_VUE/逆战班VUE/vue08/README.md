# vue08

## 一些问题
```
1. 路由实现原理是什么?
2. vue中的响应式是什么?响应式原理?
3. vue中数据变页面一定变吗？
4. $set 的功能
```

### 路由实现原理

```
router-link 控制地址栏改变
	window.location.hash = this.to
router-view 根据地址栏的改变来控制组件的切换
	在某个生命周期内通过 hashchange监听地址栏改变
	<component :is="componentId"></component> 根据路由表和地址栏修改动态组件
	
hash 通过 hashchange 监听地址栏的改变
history 通过 popState 监听地址栏的改变
```

### vue中的响应式

```
数据发生改变页面也就改变
https://cn.vuejs.org/v2/guide/reactivity.html
vue 在组件和实例初始化的时候会把data中的数据劫持，使用Object.defineProperty为数据绑定getter/setter属性，修改数据的时候会触发setter，触发底层的watcher监听，通知dom修改刷新，getter在数据使用的时候触发
在vue给data绑定的setter方法在使用watcher 监听数据改变，进行diff算法，判断是否修改dom,如果修改dom就执行真正的修改dom的方法，getter中记录数据改变的路径
```

### vue中数据变页面一定变吗

```
不一定，数据变页面也变是因为在vue初始化的时候劫持了data的数据绑定了 getter/setter属性
	在对象属性的添加，数组长度的改变
着两种方法不会添加 get/set方法，就不会数据便页面也变，
用 $set() 进行处理
```

### $set 的功能

```

```

