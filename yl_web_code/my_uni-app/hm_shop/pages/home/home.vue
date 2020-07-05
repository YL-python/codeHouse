<template>
	<view class="home">
		<!-- 首页轮播图 区域 -->
		<swiper indicator-dots circular autoplay>
			<swiper-item v-for="(item,index) in Swipers" :key="index">
				<image :src="item.img"></image>
			</swiper-item>
		</swiper>

		<!-- 首页导航 区域 -->
		<view class="nav">
			<view v-for="(item,index) in navList" :key="index" class="nav-item" @click="goPage(item.url)">
				<view :class="item.icon"></view>
				<view class="nav-text">{{item.title}}</view>
			</view>
		</view>

		<!-- 推荐商品 区域 -->
		<view class="recommend-goods">
			<view class="title">热门商品</view>
			<goods-list :goods='hotGoodsList' @itemClick='goGoodsDetail'></goods-list>
		</view>

	</view>
</template>

<script>
	import goodsList from "../../components/goods-list/goods-list.vue";
	export default {
		data() {
			return {
				Swipers: [],
				hotGoodsList: [],
				navList: [{
					"icon": "iconfont icon-shangpingguanli",
					"title": "黑马超市",
					"url": "/pages/goods/goods"
				}, {
					"icon": "iconfont icon-info",
					"title": "联系我们",
					"url": "/pages/contact/contact"
				}, {
					"icon": "iconfont icon-tupian",
					"title": "社区图片",
					"url": "/pages/pics/pics"
				}, {
					"icon": "iconfont icon-shiping",
					"title": "学习视频",
					"url": "/pages/videos/videos"
				}]
			}
		},
		onLoad() {
			this.getSwipers()
			this.getHotGoodsList()
		},
		methods: {
			// 获取轮播图数据
			async getSwipers() {
				// console.log('index.vue getlunbo');
				const res = await this.$myRequest({
					url: "getlunbo"
				})
				this.Swipers = res.message
			},
			// 获取热门商品数据
			getHotGoodsList() {
				this.$myRequest({
					url: "getgoods?pageindex=1"
				}).then((res) => {
					this.hotGoodsList = res.message
				})
			},
			// 导航跳转函数
			goPage(url) {
				// console.log(url);
				uni.navigateTo({
					url
				})
			},
			// 导航跳转函数
			goGoodsDetail(id) {
				uni.navigateTo({
					url: '/pages/goods-detail/goods-detail?id=' + id
				})
			}
		},
		components: {
			"goods-list": goodsList
		}
	}
</script>

<style lang="scss">
	// 轮播图 区域样式
	.home {
		swiper {
			width: 750rpx;
			height: 258.5rpx;

			image {
				width: 100%;
				height: 100%;
			}
		}
	}

	// 导航 区域样式
	.nav {
		display: flex;

		.nav-item {
			width: 25%;
			text-align: center;

			.iconfont {
				width: 120rpx;
				height: 120rpx;
				margin: 10px auto;
				background-color: $hmshop-main-color;
				border-radius: 50%;
				line-height: 120rpx;
				color: #fff;
				font-size: 50rpx;
			}

			.nav-text {
				font-size: 36rpx;
			}
		}
	}

	// 推荐商品 区域样式
	.recommend-goods {
		background-color: #eee;
		// 解决 margin 传递
		overflow: hidden;
		margin-top: 10px;

		.title {
			height: 50px;
			line-height: 50px;
			color: $hmshop-main-color;
			text-align: center;
			letter-spacing: 20px;
			margin: 7rpx 0;
			background-color: #fff;
		}
	}
</style>
