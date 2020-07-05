<template>
	<view class="goods-detail">
		<swiper indicator-dots autoplay>
			<swiper-item v-for="(item,index) in Swipers" :key="index">
				<image :src="item.src"></image>
			</swiper-item>
		</swiper>
		<view class="price">
			<text class="new">￥{{detail.sell_price}}</text>
			<text class="old">￥{{detail.market_price}}</text>
		</view>
		<view class="goods-name">
			{{detail.title}}
		</view>
		<view class="line"></view>
		<view class="goods_no">
			<view>货号：{{detail.goods_no}}</view>
			<view>库存：{{detail.stock_quantity}}</view>
		</view>
		<view class="line"></view>
		<view class="detail">
			<view class="title">商品详情</view>
			<rich-text class="content" :nodes='content'></rich-text>
		</view>

		<view class="goods-nav">
			<uni-goods-nav :fill="true" :options="options" :buttonGroup="buttonGroup" @click="onClick" @buttonClick="buttonClick" />
		</view>
	</view>
</template>

<script>
	import uniGoodsNav from '@/components/uni-goods-nav/uni-goods-nav.vue'
	export default {
		data() {
			return {
				id: 0,
				Swipers: [],
				detail: {},
				content: '',
				options: [{
					icon: 'headphones',
					text: '客服'
				}, {
					icon: 'shop',
					text: '店铺',
					info: 2,
					infoBackgroundColor: '#007aff',
					infoColor: "red"
				}, {
					icon: 'cart',
					text: '购物车',
					info: 2
				}],
				buttonGroup: [{
						text: '加入购物车',
						backgroundColor: '#ff0000',
						color: '#fff'
					},
					{
						text: '立即购买',
						backgroundColor: '#ffa200',
						color: '#fff'
					}
				]
			}
		},
		methods: {
			// 获取轮播图数据
			async getSwipers() {
				const res = await this.$myRequest({
					url: "getthumimages/" + this.id
				})
				// console.log(res);
				this.Swipers = res.message
			},
			async getGoodsDetail() {
				const res = await this.$myRequest({
					url: "goods/getinfo/" + this.id
				})
				// console.log(res);
				this.detail = res.message[0]
			},
			async getGoodsContent() {
				const res = await this.$myRequest({
					url: "goods/getdesc/" + this.id
				})
				// console.log(res);
				this.content = res.message[0].content
			},
			onClick(e) {
				uni.showToast({
					title: `点击${e.content.text}`,
					icon: 'none'
				})
				// console.log(e);
			},
			buttonClick(e) {
				// console.log(e)
				this.options[2].info++
			}
		},
		onLoad(op) {
			this.id = op.id
			this.getSwipers()
			this.getGoodsDetail()
			this.getGoodsContent()
		},
		components: {
			uniGoodsNav
		}
	}
</script>

<style lang="scss">
	.goods-detail {
		swiper {
			width: 750rpx;
			height: 700rpx;

			image {
				width: 100%;
				height: 100%;
			}
		}

		.price {
			padding: 10px;
			line-height: 80rpx;

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

		.goods-name {
			padding: 10px;
			font-size: 32rpx;
			line-height: 60rpx;
		}

		.goods_no {
			padding: 0 10px;
			font-size: 32rpx;
			line-height: 60rpx;
		}

		.detail {
			padding-bottom: 50px;

			.title {
				font-size: 32rpx;
				padding-left: 10px;
				border-bottom: 1px solid #eee;
				line-height: 70rpx;
			}

			.content {
				font-size: 28rpx;
				padding: 10px;
				color: #333;
				line-height: 50rpx;
			}
		}
	}

	.goods-nav {
		position: fixed;
		bottom: 0;
		width: 100%;
	}

	.line {
		width: 7560rpx;
		height: 10rpx;
		background-color: #eee;
	}
</style>
s
