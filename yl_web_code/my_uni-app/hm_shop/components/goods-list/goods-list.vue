<template>
	<view class="goods-list">
		<view v-for="(item,index) in goods" :key="index" class="goods-item" @click="navigator(item.id)">
			<image :src="item.img_url"></image>
			<view class="price">
				<text class="new">￥{{item.sell_price}}</text>
				<text class="old">￥{{item.market_price}}</text>
			</view>
			<view class="name">
				{{item.title}}
			</view>
		</view>
	</view>
</template>

<script>
	export default {
		props: ["goods"],
		methods: {
			navigator(id) {
				this.$emit("itemClick", id)
			}
		}
	}
</script>

<style lang="scss">
	.goods-list {
		padding: 0 15rpx;
		display: flex;
		justify-content: space-between;
		flex-wrap: wrap;

		.goods-item {
			background-color: #fff;
			width: 355rpx;
			margin: 10rpx 0;
			padding: 15rpx;
			box-sizing: border-box;

			image {
				display: block;
				width: 80%;
				height: 150px;
				margin: 0 auto 15rpx;
			}

			.price {
				.new {
					color: $hmshop-main-color;
					font-size: 36rpx;
				}

				.old {
					color: #ccc;
					font-size: 28rpx;
					margin-left: 17rpx;
					text-decoration: line-through;
				}
			}

			.name {
				font-size: 28rpx;
				line-height: 50rpx;
				padding: 10rpx 0 15rpx;
			}
		}
	}
</style>
