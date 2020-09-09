<!-- 话题的摘要 -->
<template>
	<view>
		<!-- 模糊背景 -->
		<view class="position-relative">
			<image src="/static/demo/topicpic/1.jpeg" class="w-100 filter" style="height: 300rpx;" mode="aspectFill"></image>
		</view>

		<!-- 简单摘要 -->
		<view class="position-relative bg-white px-2 pb-2" style="z-index: 10;">
			<view class="flex">
				<image :src="info.cover" class="rounded mr-2" style="width: 150rpx; height: 150rpx;margin-top: -75rpx;"></image>
				<text class="font-md">#{{info.title}}#</text>
			</view>
			<view class="flex align-center font text-secondary mt-1">
				<text class="mr-2">动态: {{info.news_count}}</text>
				<text>今日: {{info.today_count}}</text>
			</view>
			<view class=" font-md text-secondary">{{info.desc}}</view>
		</view>
	</view>
</template>

<script>
	export default {
		props: ['info']
	}
</script>

<style>
	.filter {
		filter: blur(10rpx)
	}
</style>
