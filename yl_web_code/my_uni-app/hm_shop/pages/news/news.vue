<template>
	<view class="news">
		<news-item :list="newsList" @itemClick="goDetail"></news-item>
	</view>
</template>

<script>
	import newsItem from "../../components/news-item/news-item.vue";
	export default {
		data() {
			return {
				newsList: []
			}
		},
		methods: {
			async getNewList() {
				console.log('index.vue getlunbo');
				const res = await this.$myRequest({
					url: "getnewslist"
				})
				this.newsList = res.message
				// console.log(this.newsList);
			},
			goDetail(id) {
				// console.log(id);
				uni.navigateTo({
					url: "/pages/news-detail/news-detail?id=" + id
				})
			}
		},
		onLoad() {
			this.getNewList()
		},
		components: {
			"news-item": newsItem
		}
	}
</script>

<style lang="scss">
</style>
