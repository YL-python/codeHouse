<template>
	<view>
		样式学习
		<view class="box">box
			<text>scss 测试</text>
		</view>
		<view class="iconfont icon-tupian"></view>
	</view>
</template>

<script>
	export default {
		data() {
			return {

			}
		},
		methods: {

		}
	}
</script>

<style lang="scss">
	@import url("./a.css");

	.box {
		width: 375rpx;
		height: 375rpx;
		background-color: $uni-color-primary;
		color: #fff;

		text {
			color: pink;
		}
	}
</style>
