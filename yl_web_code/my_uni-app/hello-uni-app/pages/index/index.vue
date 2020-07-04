<template>
	<view class="content">
		<test v-if="flag" :title="title" @myEvent="getNum"></test>
		<button @click="flag = !flag">销毁text组件</button>

		<test-a></test-a>
		<test-b></test-b>

		<uni-calendar :insert="true" :lunar="true" :start-date="'2019-3-2'" :end-date="'2019-5-20'" @change="change" />
	</view>
</template>

<script>
	import test from "../../components/test.vue"
	import testA from "../../components/a.vue"
	import testB from "../../components/b.vue"
	import uniCalendar from '@/components/uni-calendar/uni-calendar.vue'
	export default {
		data() {
			return {
				title: 'Hello',
				flag: true
			}
		},
		// 在上一个页面跳转过来的时候可以传递参数 
		onLoad(options) {
			console.log("index 页面加载", options)
		},
		onShow() {
			console.log("index 页面显示了")
		},
		onReady() {
			console.log("index 页面第一次加载完成")
		},
		onHide() {
			console.log("index 页面隐藏了")
		},
		onUnload() {
			console.log("index 页面被卸载了")
		},
		methods: {
			getNum(num) {
				console.log('子组件的 num值', num);
			},
			change(e) {
				console.log(e);
			}
		},
		components: {
			test,
			"test-a": testA,
			"test-b": testB,
			uniCalendar
		}
	}
</script>

<style>
	.content {
		display: flex;
		flex-direction: column;
		align-items: center;
		justify-content: center;
	}
</style>
