<template>
	<view class="flex align-center justify-center py-3">
		<text class="font text-light-muted">{{loadMoreText}}</text>
	</view>
</template>

<script>
	export default {
		props: {
			// 上拉加载更多   加载中...   没有更多了
			loadMoreText: String
		},
		methods: {
			// 加载更多
			loadmore(index) {
				let list = this.newsList[index]
				// 判断当前 是否是可加载的
				if (list.loadmore !== '上拉加载更多') {
					return
				}
				list.loadmore = '加载中...'
				setTimeout(() => {
					// 加载数据
					list.tabList = [...list.tabList, ...list.tabList]
					// 回复加载状态
					list.loadmore = '上拉加载更多'
				}, 2000)
			},
		}
	}
</script>

<style>
</style>
