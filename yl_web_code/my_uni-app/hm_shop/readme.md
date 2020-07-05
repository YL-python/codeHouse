# 黑马商城项目

## 经验总结

+ 总页数和总数据条数关系

```js
// 数据长度 <= 页码 * 每页条数
```

+ 关闭下拉刷新

```js
// 很多时候下拉刷新是要异步操作，关闭下拉刷新要同步操作

// 方案一： async await
// 方案二： 把关闭下拉刷新作为回调函数传入方法中

getGoodsList(calllback) {
	// 异步操作
	calllback && calllback()
},

setTimeout(this.getGoodsList(() => {
	uni.stopPullDownRefresh()
}), 1000)
```

+ vue 中定义 filters过滤器和使用

```js
filters: {
	formatDate(date) {
		let ndate = new Date(date)
		let year = ndate.getFullYear()
		let month = ndate.getMonth().toString().padStart(2, 0)
		let day = ndate.getDate().toString().padStart(2, 0)
		return `${year}-${month}-${day}`
	}
}

{{item.add_time | formatDate}}
```

+ Es7中 字符串的 padStart()方法

```js
let day = date.getDate().toString().padStart(2, 0)
```

+ uni-app中的默认组件 样式应该在 app.vue中覆盖，别的页面覆盖可能不起作用