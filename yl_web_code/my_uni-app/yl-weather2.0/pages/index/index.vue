<template>
	<view class="content text-white">
		<!-- 今天天气情况 -->
		<view class="main-info">

			<!-- 导航栏 -->
			<view class="title flex align-center justify-center font  font-weight-bolder my-5">
				<text class="iconfont icon-weibiaoti-"></text>
				当前定位
			</view>

			<!-- 预警信息 -->
			<view class="alarm font">
				<view class="warning level01">
					高温预警
				</view>
				<view class="warning level02">
					高温预警
				</view>
				<view class="warning level02">
					高温预警
				</view>
			</view>

			<!-- 预警信息 -->
			<view class="pub-time font-sm mr-2">
				<view class="">数据更新于:</view>
				<view class="my-1">2020-08-01 17:59</view>
			</view>


			<!-- 当天信息 -->
			<view class="observe flex align-center justify-center">
				<image src="//mat1.gtimg.com/pingjs/ext2020/weather/mobile2.0/assets/weather/day/01.svg" class="mr-2"></image>
				<view class="ml-2 weather flex flex-column justify-center">
					<view class="degree flex-1">
						30
						<text class="font-md ml-1">℃</text>
					</view>
					<view class="text text-white flex-1">雨夹雪大冰雹</view>
				</view>
			</view>

			<!-- 三个情况 -->
			<view class=" mt-2 flex align-center justify-center font-sm">
				<view class="mx-1">
					<text class="iconfont icon-app_icons-- mr-1"></text>
					空气优 45
				</view>
				<view class="mx-1">
					<text class="iconfont icon-shidu mr-1"></text>
					湿度 72%
				</view>
				<view class="mx-1">
					<text class="iconfont icon-fengliyucefangan mr-1"></text>
					东南风 1级
				</view>
			</view>

			<!-- 友好的提示 -->
			<view class="flex align-center justify-center font-md mt-5 "> 天太热了，吃个西瓜~ </view>

		</view>
		<divider></divider>
		<!-- 今明两天天气情况 -->
		<view class="tomorrow text-dark flex">
			<view class="flex-1 px-4">
				<view class="item">
					<view class="mb-1">今天</view>
					<view class="">34~27°</view>
				</view>
				<view class="item">
					<view class="mb-1">多云</view>
					<image src="//mat1.gtimg.com/pingjs/ext2020/weather/mobile2.0/assets/weather/day/01.svg" style="width: 44rpx; height: 44rpx;"></image>
				</view>
			</view>
			<view class="flex-1 px-4">
				<view class="item">
					<view class="mb-1">今天</view>
					<view class="">34~27°</view>
				</view>
				<view class="item">
					<view class="mb-1">多云</view>
					<image src="//mat1.gtimg.com/pingjs/ext2020/weather/mobile2.0/assets/weather/day/01.svg" style="width: 44rpx; height: 44rpx;"></image>
				</view>
			</view>
		</view>
		<divider></divider>
		<!-- 每小时的天气预报 -->
		<scroll-view class="hours scroll-row font" scroll-x>
			<view class="scroll-row-item item" style="color: #999;" v-for="i in 24" :key="i">
				<view class="mt-4 font-sm">21:00</view>
				<image class="my-2" src="//mat1.gtimg.com/pingjs/ext2020/weather/mobile2.0/assets/weather/day/01.svg" style="width: 48rpx; height: 48rpx;"></image>
				<view class="mb-4 text-dark">14°</view>
			</view>
		</scroll-view>
		<divider></divider>
		<!-- 最近几天的天气 -->
		<scroll-view class="days scroll-row font text-dark" scroll-x>
			<view class="scroll-row-item item" v-for="i in 8" hover-class="change">
				<view class="font-sm mt-4">
					<view class="">今天</view>
					<view class="" style="color: #999;">07-31</view>
				</view>
				<view class="my-4">晴</view>
				<image class="" src="//mat1.gtimg.com/pingjs/ext2020/weather/mobile2.0/assets/weather/day/01.svg" style="width: 48rpx; height: 48rpx;"></image>
				<view class="font-sm my-4">
					14°~18°
				</view>
				<view class="font-sm mb-4">
					<view class="">南风</view>
					<view class="">3级</view>
				</view>
			</view>
		</scroll-view>
		<divider></divider>
		<swiper class="living text-dark" :current='0'>
			<swiper-item class="swiper-item flex flex-wrap">
				<view class="item flex flex-column align-center">
					<view class="icon icon_diaoyu my-2"></view>
					<view class="font">不宜</view>
					<view class="font-sm text-muted my-1">钓鱼</view>
				</view>
				<view class="item flex flex-column align-center">
					<view class="icon icon_diaoyu my-2"></view>
					<view class="font">不宜</view>
					<view class="font-sm text-muted my-1">钓鱼</view>
				</view>
				<view class="item flex flex-column align-center">
					<view class="icon icon_diaoyu my-2"></view>
					<view class="font">不宜</view>
					<view class="font-sm text-muted my-1">钓鱼</view>
				</view>
				<view class="item flex flex-column align-center">
					<view class="icon icon_diaoyu my-2"></view>
					<view class="font">不宜</view>
					<view class="font-sm text-muted my-1">钓鱼</view>
				</view>
				<view class="item flex flex-column align-center">
					<view class="icon icon_diaoyu my-2"></view>
					<view class="font">不宜</view>
					<view class="font-sm text-muted my-1">钓鱼</view>
				</view>
				<view class="item flex flex-column align-center">
					<view class="icon icon_diaoyu my-2"></view>
					<view class="font">不宜</view>
					<view class="font-sm text-muted my-1">钓鱼</view>
				</view>
				<view class="item flex flex-column align-center">
					<view class="icon icon_diaoyu my-2"></view>
					<view class="font">不宜</view>
					<view class="font-sm text-muted my-1">钓鱼</view>
				</view>
				<view class="item flex flex-column align-center">
					<view class="icon icon_diaoyu my-2"></view>
					<view class="font">不宜</view>
					<view class="font-sm text-muted my-1">钓鱼</view>
				</view>
			</swiper-item>
			<swiper-item class="flex flex-wrap">
				<view class="item flex flex-column align-center">
					<view class="icon icon_diaoyu my-2"></view>
					<view class="font">不宜</view>
					<view class="font-sm text-muted my-1">钓鱼</view>
				</view>
				<view class="item flex flex-column align-center">
					<view class="icon icon_diaoyu my-2"></view>
					<view class="font">不宜</view>
					<view class="font-sm text-muted my-1">钓鱼</view>
				</view>
				<view class="item flex flex-column align-center">
					<view class="icon icon_diaoyu my-2"></view>
					<view class="font">不宜</view>
					<view class="font-sm text-muted my-1">钓鱼</view>
				</view>
				<view class="item flex flex-column align-center">
					<view class="icon icon_diaoyu my-2"></view>
					<view class="font">不宜</view>
					<view class="font-sm text-muted my-1">钓鱼</view>
				</view>
				<view class="item flex flex-column align-center">
					<view class="icon icon_diaoyu my-2"></view>
					<view class="font">不宜</view>
					<view class="font-sm text-muted my-1">钓鱼</view>
				</view>
				<view class="item flex flex-column align-center">
					<view class="icon icon_diaoyu my-2"></view>
					<view class="font">不宜</view>
					<view class="font-sm text-muted my-1">钓鱼</view>
				</view>
				<view class="item flex flex-column align-center">
					<view class="icon icon_diaoyu my-2"></view>
					<view class="font">不宜</view>
					<view class="font-sm text-muted my-1">钓鱼</view>
				</view>
				<view class="item flex flex-column align-center">
					<view class="icon icon_diaoyu my-2"></view>
					<view class="font">不宜</view>
					<view class="font-sm text-muted my-1">钓鱼</view>
				</view>
			</swiper-item>

		</swiper>
		<divider></divider>
		<view class="living-tab flex justify-center align-center">
			<view class="current mx-1"></view>
			<view class="mx-1"></view>
		</view>
		<divider></divider>
		<view class="footyer overflow-hidden">
			<view class="text-center font my-1">数据来源于中国天气网</view>
			<view class="mb-4 text-center font">
				<text>遇到问题</text>
				<text class="mx-2">|</text>
				<text>联系我</text>
				<text class="mx-2">|</text>
				<text>个人主页 </text>
			</view>
		</view>
	</view>
</template>

<script>
	// import day7Line from "../../components/day7-line.vue"

	export default {
		data() {
			return {
				"day7data": {
					max_degree: [34, 29, 36, 36, 36, 36, 33, 32],
					min_degree: [27, 28, 27, 28, 28, 27, 26, 27]
				},
				"index": {
					"airconditioner": {
						"detail": "天气热，同时湿度很大，建议您大部分时间都要开启制冷空调，来降温除湿，免受闷热之苦。",
						"info": "长时间开启",
						"name": "空调开启"
					},
					"allergy": {
						"detail": "天气条件较易诱发过敏，宜穿长衣长裤，远离过敏源，适当佩戴眼镜和口罩。",
						"info": "较易发",
						"name": "过敏"
					},
					"carwash": {
						"detail": "适宜洗车，未来持续两天无雨天气较好，适合擦洗汽车，蓝天白云、风和日丽将伴您的车子连日洁净。",
						"info": "适宜",
						"name": "洗车"
					},
					"chill": {
						"detail": "温度未达到风寒所需的低温，稍作防寒准备即可。",
						"info": "无",
						"name": "风寒"
					},
					"clothes": {
						"detail": "天气炎热，建议着短衫、短裙、短裤、薄型T恤衫等清凉夏季服装。",
						"info": "炎热",
						"name": "穿衣"
					},
					"cold": {
						"detail": "各项气象条件适宜，发生感冒机率较低。但请避免长期处于空调房间中，以防感冒。",
						"info": "少发",
						"name": "感冒"
					},
					"comfort": {
						"detail": "白天天气晴好，并且空气湿度偏大，在这种天气条件下，您会感到有些闷热，不很舒适。",
						"info": "较不舒适",
						"name": "舒适度"
					},
					"diffusion": {
						"detail": "气象条件对空气污染物稀释、扩散和清除无明显影响。",
						"info": "中",
						"name": "空气污染扩散条件"
					},
					"dry": {
						"detail": "天气较好，路面比较干燥，路况较好，不过天气有点热，定期让车辆休息。",
						"info": "干燥",
						"name": "路况"
					},
					"drying": {
						"detail": "天气不错，极适宜晾晒。",
						"info": "极适宜",
						"name": "晾晒"
					},
					"fish": {
						"detail": "较适合垂钓，但风力稍大，会对垂钓产生一定的影响。",
						"info": "较适宜",
						"name": "钓鱼"
					},
					"heatstroke": {
						"detail": "使人汗流浃背的桑拿天来了，要注意随时补充水分~",
						"info": "较易发",
						"name": "中暑"
					},
					"makeup": {
						"detail": "天气炎热，用防脱水防晒指数高的化妆品，少用粉底，常补粉。",
						"info": "防脱水防晒",
						"name": "化妆"
					},
					"mood": {
						"detail": "烈日炎炎，气温很高，心情易躁易怒，爱发脾气，注意消夏降温，提防“情绪中暑”。",
						"info": "差",
						"name": "心情"
					},
					"morning": {
						"detail": "早晨气象条件较适宜晨练，但风力稍大，晨练时请注意选择避风的地点，避免迎风锻炼。",
						"info": "较适宜",
						"name": "晨练"
					},
					"sports": {
						"detail": "天气较好，无雨水困扰，但考虑气温很高，请注意适当减少运动时间并降低运动强度，运动后及时补充水分。",
						"info": "较不宜",
						"name": "运动"
					},
					"sunglasses": {
						"detail": "白天太阳辐射强烈，容易对眼睛造成伤害，强烈建议佩戴透射比3级且标注100%UV吸收的遮阳镜",
						"info": "非常必要",
						"name": "太阳镜"
					},
					"sunscreen": {
						"detail": "紫外辐射极强，应特别加强防护，建议涂擦SPF20以上，PA++的防晒护肤品，并随时补涂。",
						"info": "极强",
						"name": "防晒"
					},
					"time": "20200802",
					"tourism": {
						"detail": "天气较好，同时又有微风伴您一路同行，但是比较热，外出旅游请注意防晒，并注意防暑降温。",
						"info": "一般",
						"name": "旅游"
					},
					"traffic": {
						"detail": "天气较好，路面干燥，交通气象条件良好，车辆可以正常行驶。",
						"info": "良好",
						"name": "交通"
					},
					"ultraviolet": {
						"detail": "紫外线辐射极强，建议涂擦SPF20以上、PA++的防晒护肤品，尽量避免暴露于日光下。",
						"info": "很强",
						"name": "紫外线强度"
					},
					"umbrella": {
						"detail": "天气较好，您在出门的时候无须带雨伞。",
						"info": "不带伞",
						"name": "雨伞"
					}
				},
			}
		},
		onLoad() {
			let lcation = uni.getStorageSync('yjtq_location');
			console.log("yjtq_location:", lcation);
		},
		methods: {},
		components: {
			// day7Line
		}
	}
</script>

<style lang="scss">
	.main-info {
		position: relative;
		overflow: hidden;
		width: 750rpx;
		height: 730rpx;
		background-image: url(../../static/img/bg.jpg);
		background-repeat: no-repeat;
		background-size: cover;

		.observe {
			margin-top: 200rpx;

			image {
				width: 200rpx;
				height: 200rpx;
			}

			.weather {
				line-height: 1;

				.degree {
					height: 100rpx;
					font-size: 88rpx;
				}

				.text {
					height: 100rpx;
					font-size: 48rpx;
				}
			}
		}
	}

	.living-tab {
		background-color: #f0f0f0;

		view {
			height: 6rpx;
			width: 20rpx;
			background-color: #e3e3e3;
		}

		.current {
			background-color: #cecece;
		}
	}

	.living {
		background-color: #f0f0f0;
	}

	.living .swiper-item {
		border-left: 1px solid #e6e6e6;
		border-top: 1px solid #e6e6e6;
	}
</style>
