<template>
	<view class="collection">
		<view class="location" v-for="(item,index) in wetherList" :key='index' @click="goIndex(item)">
			<view class="name">
				{{item.district}}
			</view>
			<image :src="item.image"></image>
			<view class="weather">
				<view class="num">{{item.degree}} <text>℃</text></view>
				<view class="text">{{item.weather}}</view>
			</view>
		</view>
		<view class="none" v-if="wetherList.length === 0">
			还没有收藏的地址哦，点击加号添加一个吧。
			首页右上角的星号也能添加收藏哦。
		</view>
		<view class="icon-list">
			<view class="icon" @click="refresh()">
				<text class="iconfont  icon-shuaxin"></text>
				<view class="text">刷新</view>
			</view>
			<view class="icon" @click="handleTap('picker')">
				<text class="iconfont  icon-jia"></text>
				<view class="text">添加</view>
			</view>
		</view>


		<lb-picker ref="picker" mode="multiSelector" :list="list" :level="3" @confirm="handleConfirm" confirm-color='#1296db'>
		</lb-picker>
	</view>
</template>

<script>
	import {
		mapState,
		mapActions,
		mapMutations
	} from "vuex";
	import LbPicker from '@/components/lb-picker'
	import areaData from '../../static/js/city.js'
	export default {
		data() {
			return {
				// 城市多级下拉列表数据
				list: areaData,
				wetherList: []
			}
		},
		onLoad() {
			this.getLocationListWeather(this.LocationList)
		},
		methods: {
			handleTap(picker) {
				this.$refs[picker].show()
			},
			handleConfirm(picker) {
				let location = {}
				location.province = picker.item[0].label
				location.city = picker.item[1].label
				location.district = picker.item[2].label
				this.saveLocationList(location)
			},
			getLocationListWeather(locationList) {
				if (!locationList) {
					return
				}
				// uni.showLoading({
				// 	title: '加载中'
				// });
				this.wetherList = []
				let pList = []
				for (let i = 0; i < locationList.length; i++) {
					let location = locationList[i]
					let url =
						`/weather?weather_type=observe&province=${location.province}&city=${location.city}&county=${location.district}`
					let res = this.$myRequest({
						url
					})
					pList.push(res)
				}
				Promise.all(pList).then((res) => {
					for (var i = 0; i < res.length; i++) {
						let data = {}
						data.province = res[i].province
						data.city = res[i].city
						data.district = res[i].county
						data.degree = res[i].data.observe.degree
						data.weather = res[i].data.observe.weather
						data.image = "http://mat1.gtimg.com/pingjs/ext2020/weather/mobile2.0/assets/weather/day/weather_code.svg".replace(
							"weather_code", res[i].data.observe.weather_code)
						this.wetherList.push(data)
					}
					// uni.hideLoading();
				})
			},
			refresh() {
				this.getLocationListWeather(this.LocationList)
			},
			goIndex(data) {
				this.setNowLocation({
					"province": data.province,
					"city": data.city,
					"district": data.district
				})
				uni.switchTab({
					url: '/pages/index/index'
				});
			},
			...mapActions(["saveLocationList", "deleteLocationList"]),
			...mapMutations(['setNowLocation'])
		},
		computed: {
			// 启动时的定位
			...mapState(["nowLocation", "LocationList"])
		},
		watch: {
			LocationList() {
				this.refresh()
			}
		},
		components: {
			LbPicker
		}
	}
</script>

<style lang="scss">
	.collection {
		.none {
			height: 160rpx;
			// line-height: 160rpx;
			background-color: rgb(246, 249, 254);
			border-bottom: 1px solid #e4e4e4;
		}

		.location {
			display: flex;
			justify-content: space-between;
			align-items: center;
			height: 160rpx;
			padding: 20rpx 40rpx;
			background-color: rgb(246, 249, 254);
			border-bottom: 1px solid #e4e4e4;

			.name {
				flex: 0 1 33.3%;
				font-size: 32rpx;
				line-height: 32rpx;
				text-align: center;
			}

			.weather {
				text-align: center;
				font-size: 32rpx;
				line-height: 32rpx;
				flex: 0 1 33.3%;

				.num {
					margin: 10rpx 0;

					text {
						margin: 0 0 0 10rpx;
						font-size: 24rpx;
					}
				}
			}

			image {
				display: block;
				height: 100rpx;
				width: 100rpx;
			}
		}

		.icon-list {
			display: flex;
			justify-content: space-around;
			font-size: 24rpx;
			margin-top: 20rpx;

			.icon {
				text {
					display: block;
					text-align: center;
				}
			}
		}
	}
</style>
