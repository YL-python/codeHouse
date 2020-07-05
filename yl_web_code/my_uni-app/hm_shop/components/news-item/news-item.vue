<template>
	<view>
		<view class="news-item" v-for="(item,index) in list" :key="index" @click="navigator(item.id)">
			<image :src="item.img_url"></image>
			<view class="content">
				<view class="title">{{item.title}}</view>
				<view class="info">
					<text>发表时间：{{item.add_time | formatDate}}</text>
					<text>浏览：{{item.click}}</text>
				</view>
			</view>
		</view>
	</view>
</template>

<script>
	export default {
		props: ['list'],
		filters: {
			formatDate(date) {
				let ndate = new Date(date)
				let year = ndate.getFullYear()
				let month = ndate.getMonth().toString().padStart(2, 0)
				let day = ndate.getDate().toString().padStart(2, 0)
				return `${year}-${month}-${day}`
			}
		},
		methods: {
			navigator(id) {
				this.$emit("itemClick", id)
			}
		}
	}
</script>

<style lang="scss">
	.news-item {
		display: flex;
		padding: 10rpx 20rpx;
		border-bottom: 1px solid $hmshop-main-color;

		image {
			min-width: 200rpx;
			max-width: 200rpx;
			height: 150rpx;
		}

		.content {
			display: flex;
			flex-direction: column;
			justify-content: space-between;
			padding: 0 0 0 30rpx;

			.title {
				font-size: 30rpx;
			}

			.info {
				font-size: 24rpx;

				text:nth-child(2) {
					margin-left: 30rpx;
				}
			}
		}
	}
</style>
