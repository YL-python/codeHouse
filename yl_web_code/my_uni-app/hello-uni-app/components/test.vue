<template>
	<view id="test">
		<view> 这是 test 组件 {{ num }} {{ title}}</view>
		<button @click="sendMsg">test组件向父组件通信</button>
	</view>
</template>

<script>
	export default {
		props: ["title"],
		data() {
			return {
				num: 100
			};
		},
		methods: {
			sendMsg() {
				this.$emit("myEvent", this.num)
			}
		},
		beforeCreate() {
			console.log('实例 开始 初始化');
			console.log('num数据：', this.num);
		},
		created() {
			console.log('实例 初始化 完成');
			console.log('num数据：', this.num);
		},
		beforeMount() {
			console.log('实例 开始 挂载');
			console.log('dom数据：', document.getElementById("test"));
		},
		mounted() {
			console.log('实例 挂载 完成');
			console.log('dom数据：', document.getElementById("test"));
		},
		destroyed() {
			console.log('实例 被销毁');
		}
	}
</script>

<style>

</style>
