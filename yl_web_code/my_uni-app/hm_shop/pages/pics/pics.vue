<template>
	<view class="pics">
		<scroll-view class="left" scroll-y>
			<view :class="activeIndex===index?'active':''" v-for="(item,index) in cases" :key="index" @click="leftClick(index,item.id)">{{item.title}}</view>
		</scroll-view>

		<scroll-view class="right" scroll-y>
			<view class="item" v-for="(item,index) in secoundData" :key="index">
				<image @click="previewImg(item.img_url)" :src="item.img_url"></image>
				<text>{{item.title}}</text>
			</view>
			<text v-if="secoundData.length === 0">暂无数据</text>
		</scroll-view>
	</view>
</template>

<script>
	export default {
		data() {
			return {
				cases: [],
				activeIndex: 0,
				secoundData: []
			}
		},
		methods: {
			async getPicsCase() {
				const res = await this.$myRequest({
					url: "getimgcategory"
				})
				this.cases = res.message
				// console.log(this.cases);
				this.leftClick(0, this.cases[0].id)
			},
			async leftClick(index, id) {
				this.activeIndex = index
				// 获取右侧数据
				const res = await this.$myRequest({
					url: "getimages/" + id
				})
				this.secoundData = res.message
				// console.log('', this.secoundData);
			},
			previewImg(current) {
				let urls = this.secoundData.map((item) => {
					return item.img_url
				})
				uni.previewImage({
					current,
					urls
				})
			}
		},
		onLoad() {
			this.getPicsCase()
		}
	}
</script>

<style lang="scss">
	page {
		height: 100%;
	}

	.pics {
		height: 100%;
		display: flex;
		overflow: hidden;

		.left {
			width: 200rpx;
			height: 100%;
			border-right: 1px solid #eee;

			view {
				height: 120rpx;
				line-height: 120rpx;
				text-align: center;
				color: #333;
				font-size: 30rpx;
				border-top: 1px solid #eee;
			}

			.active {
				background-color: $hmshop-main-color;
				color: #fff;
			}
		}

		.right {
			width: 520rpx;
			height: 100%;
			margin: 10rpx auto;

			.item {
				image {
					width: 520rpx;
					height: 520rpx;
					border-radius: 5px;
				}

				text {
					font-size: 32rpx;
					line-height: 64rpx;
				}
			}
		}

	}
</style>
