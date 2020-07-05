<template>
	<view class="goods">
		<goods-list :goods='goods' @itemClick='goGoodsDetail'></goods-list>
		<view class="isOver" v-if="isOver">----- 我是有底线的 -----</view>
	</view>
</template>

<script>
	import goodsList from "../../components/goods-list/goods-list.vue";
	export default {
		data() {
			return {
				goods: [],
				pageindex: 1,
				isOver: false
			}
		},
		methods: {
			// 获取热门商品数据
			getGoodsList(calllback) {
				this.$myRequest({
					url: "getgoods?pageindex=" + this.pageindex
				}).then((res) => {
					this.goods = [...this.goods, ...res.message]
				})
				calllback && calllback()
			},
			refresh() {
				this.goods = []
				this.pageindex = 1
				this.isOver = false
				setTimeout(this.getGoodsList(() => {
					uni.stopPullDownRefresh()
				}), 1000)
			},
			// 导航跳转函数
			goGoodsDetail(id) {
				// console.log('goGoodsDetail');
				uni.navigateTo({
					url: '/pages/goods-detail/goods-detail?id=' + id
				})
				// console.log('goGoodsDetail after');
			}
		},
		onLoad() {
			this.getGoodsList()
		},
		onReachBottom() {
			if (this.isOver || this.goods.length < this.pageindex * 10) {
				this.isOver = true
				return;
			}
			this.pageindex++
			this.getGoodsList()

		},
		onPullDownRefresh() {
			this.refresh()
		},
		components: {
			"goods-list": goodsList
		}
	}
</script>

<style>
	.goods {
		background-color: #eee;
		// 解决 margin 传递
		overflow: hidden;
	}

	.isOver {
		width: 100%;
		height: 50px;
		line-height: 50px;
		font-size: 28rpx;
		text-align: center;
	}
</style>
