<template>
	<view>
		<view> 这是列表页</view>
		<button @click="pullDown">按钮</button>
		<view class="list-item" v-for="(item, index) in arr" :key='index'>
			{{item}}
		</view>
	</view>
</template>

<script>
	export default {
		data() {
			return {
				arr: ['前端', 'java', 'ui', '大数据', "测试"]
			}
		},
		onPullDownRefresh() {
			console.log('触发下拉刷新了')
			this.arr = ['java', 'ui', '前端', '大数据', "测试"]
			// 结束加载
			uni.stopPullDownRefresh()
		},
		onReachBottom() {
			console.log('页面触底了')
			this.arr = [...this.arr, ...['java', 'ui', '前端', '大数据', "测试"]]
		},
		methods: {
			pullDown() {
				uni.startPullDownRefresh()
				this.arr = [...this.arr, ...['java', 'ui', '前端', '大数据', "测试"]]
				uni.stopPullDownRefresh()
			}
		}
	}
</script>

<style>
	.list-item {
		height: 200px;
		line-height: 200px;
	}
</style>
