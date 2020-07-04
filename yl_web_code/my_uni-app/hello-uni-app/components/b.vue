<template>
	<view>
		<view> 这是 b 组件</view>
		<view> b组件 num： {{num}}</view>
	</view>
</template>

<script>
	export default {
		data() {
			return {
				num: 100
			};
		},
		created() {
			uni.$on("updateBNum", (temp) => {
				this.num += temp
			})
		}
	}
</script>

<style>

</style>
