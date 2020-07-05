<template>
	<view class="news-detail">
		<view class="title">{{detail.title}}</view>

		<view class="info">
			<text>发表时间：{{detail.add_time | formatDate}}</text>
			<text>浏览：{{detail.click}}</text>
		</view>

		<view class="content">
			<rich-text :nodes='detail.content'></rich-text>
		</view>
	</view>
</template>

<script>
	export default {
		data() {
			return {
				id: 0,
				detail: {}
			}
		},
		methods: {
			async getNewsDetail() {
				const res = await this.$myRequest({
					url: "getnew/" + this.id
				})
				// console.log(res);
				this.detail = res.message[0]
			},
		},
		onLoad(options) {
			this.id = options.id
			this.getNewsDetail(0)
		}
	}
</script>

<style lang="scss">
	.news-detail {
		font-size: 32rpx;
		padding: 0 20rpx;

		.title {
			margin: 20rpx;
			text-align: center;
		}

		.info {
			display: flex;
			justify-content: space-between;
		}
	}
</style>
