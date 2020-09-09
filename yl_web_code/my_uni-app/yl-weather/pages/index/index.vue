<template>
	<view class="content">
		<!-- 当前天气实况 -->
		<view class="nowWeather" v-if="nowWeather">
			<view class="city">
				{{chooseLocation.district}}
				<text @click="handleTap('picker')">[切换]</text>
			</view>
			<view class="time" v-if="nowWeather.time">
				<text>{{nowWeather.time.date}}</text>
				<text>{{nowWeather.time.time}}</text>
				<text>数据更新于:{{nowWeather.time.uptime}}</text>
			</view>
			<view class="weather" v-if="nowWeather.weather">
				<image :src="nowWeather.weather.img">
				</image>
				<view class="weather-info">
					<view class="degree">{{nowWeather.weather.degree}}<text>℃</text></view>
					<view class="today">{{nowWeather.weather.text}}</view>
				</view>
			</view>
			<view class="tip" v-if="nowWeather.tips">{{nowWeather.tips[0]}}</view>
			<view class="environment" v-if="nowWeather.environment">
				<view class="air">
					空气:{{nowWeather.environment.aqi.level}} {{nowWeather.environment.aqi.num}}
				</view>
				<view class="humidity">
					湿度:{{nowWeather.environment.humidity.level}}%
				</view>
				<view class="wind">
					{{nowWeather.environment.wind.direction}}:{{nowWeather.environment.wind.level}}级
				</view>
			</view>
		</view>
		<!-- 今明两天的天气数据 -->
		<view class="future2d" v-if="future7d">
			<view class="item" v-if="future7d['1']">
				<view class="top">
					<view class="date">
						今天
					</view>
					<view class="temperature">
						{{future7d['1'].min_degree}}~{{future7d['1'].max_degree}} ℃
					</view>
				</view>
				<view class="bottom">
					<view class="weather">
						{{future7d['1'].day_weather}}转{{future7d['1'].night_weather}}
					</view>
					<!-- <image :src="future7d['1'].day_weather_code"></image> -->
					<view class="img">
						<image :src="future7d['1'].day_weather_code"></image>
						<image :src="future7d['1'].night_weather_code"></image>
					</view>
				</view>
			</view>
			<view class="item" v-if="future7d['2']">
				<view class="top">
					<view class="date">
						明天
					</view>
					<view class="temperature">
						{{future7d['2'].min_degree}}~{{future7d['2'].max_degree}} ℃
					</view>
				</view>
				<view class="bottom">
					<view class="weather">
						{{future7d['2'].day_weather}}转{{future7d['2'].night_weather}}
					</view>
					<view class="img">
						<image :src="future7d['2'].day_weather_code"></image>
						<image :src="future7d['2'].night_weather_code"></image>
					</view>
				</view>
			</view>
		</view>
		<!-- 每小时的天气预报 -->
		<scroll-view class="future48h" scroll-x v-if="future48h">
			<text class="title">逐小时天气：</text>
			<view class="item-wrapper" v-for="(item, index) in future48h" :key="index">
				<view class="item">
					<view class="time">{{item.update_time | formatDate('2')}}</view>
					<image :src="item.weather_code"></image>
					<view class="weather">{{item.degree}}°</view>
				</view>
			</view>
		</scroll-view>
		<!-- 未来7天的天气 -->
		<view class="future7d" scroll-x v-if="future7d">
			<text class="title">近七天天气：</text>
			<view class="item" v-for="(item,index) in future7d" :key="index" :class="index==='0'?'item-first':''">
				<view class="left">
					{{item.time.date}} {{item.time.week}}
				</view>
				<view class="center">
					<image :src="item.day_weather_code"></image>
					<image :src="item.night_weather_code"></image>
				</view>
				<view class="right">
					{{item.min_degree}}~{{item.max_degree}} ℃
				</view>
			</view>
		</view>
		<view class="line"></view>

		<view class="icon">
			<text class="iconfont  icon-shuaxin" @click="refresh()"></text>
			<text class="collection iconfont" :class="isCollection?'icon-shoucang2':'icon-shoucang'" @click="changeLocation(chooseLocation)"></text>
		</view>

		<lb-picker ref="picker" mode="multiSelector" :list="list" :level="3" @confirm="handleConfirm" confirm-color='#1296db'>
		</lb-picker>

	</view>
</template>

<script>
	import LbPicker from '@/components/lb-picker'
	import areaData from '../../static/js/city.js'
	import formatData from './formatData.js'
	import {
		mapState,
		mapActions
	} from "vuex";

	export default {
		data() {
			return {
				// 城市多级下拉列表数据
				list: areaData,
				// 用户选择的地理位置
				chooseLocation: {},
				nowWeather: {},
				future7d: {},				
				future48h: {},
				show: true,
				isCollection: false
			}
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
				this.chooseLocation = location
			},
			// 传入一个地方 获取这个地方的天气并更新数据
			getLocationWeather(location) {
				uni.showLoading({
					title: '加载中'
				});
				this.nowWeather = {}
				this.future48h = {}
				this.future7d = {}
				// console.log('获取位置天气 ', location.province, location.city, location.district);
				let url =
					`/weather?weather_type=observe|air|forecast_24h|forecast_1h|tips&province=${location.province}&city=${location.city}&county=${location.district}`
				this.$myRequest({
					url
				}).then((res) => {
					this.handleData(res.data)
					uni.hideLoading();
				})
			},
			handleData(data) {
				let {
					nowWeather,
					future48h,
					future7d
				} = formatData(data)
				this.nowWeather = nowWeather
				this.future48h = future48h
				this.future7d = future7d
				// console.log('this.future7d', this.future7d);
			},
			refresh() {
				this.getLocationWeather(this.chooseLocation)
			},
			changeLocation(Location) {
				if (this.isCollection) {
					this.deleteLocationList(Location)
					this.isCollection = false
					uni.showToast({
						title: "移除收藏",
						duration: 500
					})
				} else {
					this.saveLocationList(Location)
					this.isCollection = true
					uni.showToast({
						title: "加入收藏",
						duration: 500
					})
				}
			},
			...mapActions(["saveLocationList", "deleteLocationList"]),
		},
		onLoad() {
			this.chooseLocation = this.nowLocation
			// this.getLocationWeather(this.chooseLocation)
		},
		computed: {
			// 启动时的定位
			...mapState(["nowLocation", "LocationList"])
		},
		watch: {
			chooseLocation(newLocation) {
				// 每当用户选择地理位置之后就发送请求获取数据
				this.getLocationWeather(newLocation)
				// 判断这个 地方用户有没有收藏
				this.isCollection = false
				this.LocationList.forEach((item) => {
					if (item.province === newLocation.province && item.city === newLocation.city && item.district === newLocation.district) {
						this.isCollection = true
					}
				})
			},
			nowLocation(newLocation) {
				this.chooseLocation = this.nowLocation
			}
		},
		components: {
			LbPicker
		}
	}
</script>

<style lang="scss">
	.content {
		position: relative;

		// 今天天气
		.nowWeather {
			position: relative;
			overflow: hidden;
			width: 750rpx;
			height: 595rpx;
			background-image: url(http://coderyl.top/static/images/blue-weather-bg.jpg);
			background-repeat: no-repeat;
			background-size: cover;

			.city {
				margin: 40rpx 0 20rpx;
				text-align: center;
				font-size: 48rpx;
				color: #fff;

				text {
					font-size: 28rpx;
					margin-left: 24rpx;
				}
			}

			.time {
				font-size: 20rpx;
				color: #fff;
				text-align: center;

				text {
					margin: 0 24rpx;
				}
			}

			.weather {
				display: flex;
				margin: 40rpx 0 0;
				padding: 0 0 0 36rpx;

				image {
					display: block;
					width: 220rpx;
					height: 220rpx;
				}

				.weather-info {
					margin: 20rpx auto 0;

					.degree {
						text-align: center;
						font-size: 80rpx;
						color: #fff;

						text {
							font-size: 50rpx;
						}
					}

					.today {
						margin: 10rpx 0 0 0;
						font-size: 36rpx;
						color: rgba(255, 255, 255, 0.8);
					}
				}
			}

			.tip {
				text-align: center;
				color: #fff;
			}

			.environment {
				position: absolute;
				bottom: 0;
				padding: 0;
				display: flex;
				text-align: center;
				width: 100%;
				font-size: 28rpx;
				margin: 24rpx 0;

				.humidity {
					border-left: 1px solid #d1d1d1;
					border-right: 1px solid #d1d1d1
				}

				view {
					width: 33.3%;
				}
			}
		}

		.future2d {
			display: flex;
			padding-top: 52rpx;
			position: relative;
			height: 206rpx;
			box-sizing: border-box;
			background-color: #F6F9FE;
			border-bottom: 1px solid #e4e4e4;
			border-top: 1px solid #e4e4e4;

			.item {
				width: 50%;

				font-size: 28rpx;
				color: #434343;
				line-height: 28rpx;
				padding: 0 20px;
				overflow: hidden;

				.top,
				.bottom {
					margin: 0 0 26rpx 0;
					display: flex;
					justify-content: space-between;

					.img {
						display: flex;
					}
				}
			}

			image {
				display: block;
				width: 44rpx;
				height: 44rpx;
			}

			&:after {
				content: "";
				position: absolute;
				width: 1px;
				height: 52px;
				background-color: #d1d1d1;
				left: 50%;
				top: 26px;
			}
		}

		.future48h {
			height: 270rpx;
			padding: 20rpx 0;
			background-color: rgb(244, 244, 244);
			white-space: nowrap;
			position: relative;

			.title {
				font-size: 24rpx;
				top: 20rpx;
				left: 28rpx;
				position: absolute;
			}

			.item-wrapper {
				display: inline-block;
				box-sizing: border-box;
				border-top: 1px solid #e4e4e4;
				border-bottom: 1px solid #e4e4e4;

				.item {
					width: 116rpx;
					background-color: #F6F9FE;
					padding: 60rpx 0;
					height: 148rpx;
					display: flex;
					flex-direction: column;
					justify-content: space-between;
					align-items: center;

					.time {
						font-size: 24rpx;
						line-height: 24rpx;
						color: #999;
					}

					.weather {
						font-size: 28rpx;
						line-height: 28rpx;
						color: #434343;
					}
				}
			}

			image {
				display: block;
				width: 48rpx;
				height: 48rpx;
			}
		}

		.future7d {
			position: relative;
			background-color: rgb(246, 249, 254);
			font-size: 28rpx;
			color: #434343;
			line-height: 28rpx;
			padding-top: 50rpx;

			.item-first {
				border-top: 1px solid rgb(240, 240, 240);
			}

			.item {
				display: flex;
				justify-content: space-between;
				align-items: center;
				height: 88rpx;
				border-bottom: 1px solid rgb(240, 240, 240);

				.left {
					margin-left: 28rpx;
				}

				.center {
					display: flex;
				}

				.right {
					margin-right: 28rpx;
				}
			}

			image {
				display: block;
				width: 48rpx;
				height: 48rpx;
			}

			.title {
				font-size: 24rpx;
				color: #434343;
				top: 20rpx;
				left: 28rpx;
				position: absolute;
			}
		}

		.line {
			margin-bottom: 20rpx;
		}

		.icon {
			position: absolute;
			top: 36rpx;
			right: 46rpx;
			color: #fff;

			.icon-shuaxin {
				font-size: 44rpx;
				margin-right: 20rpx;
			}

			.icon-shoucang {
				font-size: 44rpx;
			}

			.icon-shoucang2 {
				font-size: 44rpx;
				color: rgb(255, 213, 79);
			}
		}
	}
</style>
