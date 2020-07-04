<template>
	<view>
		<view>导航跳转</view>
		<navigator url="/pages/detail/detail?id=80&age=19">go 详情</navigator>
		<navigator url="/pages/message/message" open-type="switchTab">go 信息</navigator>
		<navigator url="/pages/detail/detail" open-type="redirect">go 详情</navigator>

		<button @click="goDetail">跳转到详情</button>
		<button @click="goMessage">跳转到信息</button>
		<button @click="goDetail1">跳转到详情并关闭当前页</button>
	</view>
</template>

<script>
	export default {
		data() {
			return {

			}
		},
		methods: {
			goDetail() {
				uni.navigateTo({
					url: "/pages/detail/detail"
				})
			},
			goMessage() {
				uni.switchTab({
					url: "/pages/message/message"
				})
			},
			goDetail1() {
				uni.redirectTo({
					url: "/pages/detail/detail"
				})
			}
		}
	}
</script>

<style>

</style>
