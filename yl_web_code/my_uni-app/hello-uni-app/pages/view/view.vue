<template>
	<view>
		<view class="box2" hover-class="box2-hover">
			<!-- 阻止点击事件冒泡 -->
			<view class="box1" hover-class="box1-hover" hover-stop-propagation :hover-start-time="2000" :hover-stay-time='2000'>
				我是view标签内容
			</view>
		</view>
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

<style>
	.box2 {
		width: 200px;
		height: 200px;
		background-color: green;
	}

	.box2-hover {
		background-color: pink;
	}

	.box1 {
		width: 100px;
		height: 100px;
		background-color: #007AFF;
	}

	.box1-hover {
		background-color: #4CD964;
	}
</style>
