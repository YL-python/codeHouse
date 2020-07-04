<template>
	<view>
		<view>网络请求展示页面</view>
		<button @click="apiGet">发送 get 请求</button>
		<button @click="setId">设置 id</button>
		<button @click="getId">获取 id</button>
		<button @click="removeId">删除 id</button>
	</view>
</template>

<script>
	export default {
		data() {
			return {

			}
		},
		methods: {
			apiGet() {
				uni.request({
					url: "http://coderyl.top/node/ip",
					success(res) {
						console.log(res)
					}
				})
			},
			setId() {
				// uni.setStorage({
				// 	key:"id",
				// 	data:80.,
				// 	success() {
				// 		console.log("设置成功")
				// 	}
				// })
				uni.setStorageSync("id", 100)
				console.log("设置成功")
			},
			getId() {
				// uni.getStorage({
				// 	key: "id",
				// 	success(res) {
				// 		console.log("获取成功", res)
				// 	}
				// })
				let id = uni.getStorageSync("id")
				console.log("获取成功", id)
			},
			removeId() {
				// uni.removeStorage({
				// 	key: "id",
				// 	success() {
				// 		console.log("移除成功")
				// 	}
				// })
				uni.removeStorageSync("id")
				console.log("移除成功")
			}
		}
	}
</script>

<style>

</style>
