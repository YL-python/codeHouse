<template>
	<view>
		<view> 这是 a 组件</view>
		<button @click="addBNum"> 修改 b 组件的值</button>
	</view>
</template>

<script>
	export default {
		data() {
			return {

			};
		},
		methods: {
			addBNum() {
				uni.$emit("updateBNum", 5)
			}
		}
	}
</script>

<style>

</style>
