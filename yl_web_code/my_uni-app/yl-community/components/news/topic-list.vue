<template>
	<view class="flex align-center px-2 pb-2" @click="open()">
		<image :src="item.cover" class="rounded mr-2 flex-1" style="width: 150rpx; height: 150rpx;"></image>
		<view class="flex flex-column  flex-4 text-ellipsis">
			<view class="font-md text-dark">#{{item.title}}#</view>
			<view class="font text-secondary text-ellipsis">{{item.desc}}</view>
			<view class="flex align-center font text-secondary">
				<text class="mr-2">动态 {{item.news_count}}</text>
				<text>今日 {{item.today_count}}</text>
			</view>
		</view>
	</view>
</template>

<script>
	export default {
		props: {
			item: Object,
			index: Number
		},
		methods: {
			open() {
				uni.navigateTo({
					url: '../../pages/topic-detail/topic-detail?detail=' + JSON.stringify(this.item)
				})
			}
		}
	}
</script>

<style>
</style>
