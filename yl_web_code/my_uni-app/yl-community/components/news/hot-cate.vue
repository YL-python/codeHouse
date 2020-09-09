<template>
	<view>
		<view class="flex align-center justify-between px-2">
			<text class="font-md">热门</text>
			<view class="flex align-center font text-secondary animated" hover-class="jello" @click="openMore">
				更多
				<text class="iconfont icon-jinru"></text>
			</view>
		</view>
		<view class="flex align-center py-2 px-2 border-bottom">
			<block v-for="(item,index) in hotCate" :key='index'>
				<view class="border rounded bg-light mx-1 px-1 animated " hover-class="jello" @click='openDetail(item)'>{{item.name}}</view>
			</block>
		</view>
	</view>
</template>

<script>
	export default {
		props: ['hotCate'],
		data() {
			return {

			}
		},
		methods: {
			openMore() {
				// console.log('打开更多');
				uni.navigateTo({
					url:'../../pages/topic-nav/topic-nav'
				})
			},
			openDetail(item) {
				console.log('打开话题分类：', item);
			}
		}
	}
</script>

<style>

</style>
