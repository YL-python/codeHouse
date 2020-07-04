<script>
	export default {
		onLaunch: function() {
			console.log('小程序加载完成')
		},
		onShow: function() {
			console.log('小程序 显示')
			// 制造一个异常，一个不存在的变量，会被 onError 捕获到
			// console.log(a)
		},
		onHide: function() {
			console.log('小程序 隐藏')
		},
		onError: function(err) {
			console.log("出现异常了", err)
		}
	}
</script>

<style>
	/*每个页面公共css */
	@import url("./static/fonts/iconfont.css");
</style>
