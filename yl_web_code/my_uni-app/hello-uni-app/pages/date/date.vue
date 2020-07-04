<template>
	<view>
		<view> 数据绑定 事件 案例 </view>
		<view>msg:{{msg}}</view>
		<view>三元运算:{{flag?"真的":"假的"}}</view>
		<view>数学运算:{{1+1}}</view>
		<image :src="img"></image>
		<view v-for="(item,i) in arr" :key="i">名字：{{item.name}}---年龄：{{item.age}}</view>
		<button @click="clickHandle1">点我啊</button>
		<button @click="clickHandle2(100)">点我啊</button>
		<button @click="clickHandle3(100,$event)">点我啊</button>
	</view>
</template>

<script>
	export default {
		data() {
			return {
				msg: '信息 msg 内容',
				flag: false,
				img: 'http://destiny001.gitee.io/image/monkey_02.jpg',
				arr: [{
						name: '刘能',
						age: 29
					},
					{
						name: '赵四',
						age: 39
					},
					{
						name: '宋小宝',
						age: 49
					},
					{
						name: '小沈阳',
						age: 59
					}
				]
			}
		},
		methods: {
			clickHandle1(e) {
				console.log(e)
			},
			clickHandle2(num) {
				console.log(num)
			},
			clickHandle3(num,e) {
				console.log(num,e)
			}
		}
	}
</script>

<style>

</style>
