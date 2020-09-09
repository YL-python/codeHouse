<template>
	<view>
		<view class="qiun-bg-white qiun-title-bar qiun-common-mt">
			<view class="qiun-title-dot-light">折线图一（可横向拖拽带滚动条）</view>
		</view>
		<view class="qiun-charts">
			<canvas canvas-id="canvasLineA" id="canvasLineA" class="charts" :width="cWidth*pixelRatio" :height="cHeight*pixelRatio"
			 :style="{'width':cWidth+'px','height':cHeight+'px'}" disable-scroll=true @touchstart="touchLineA" @touchmove="moveLineA"
			 @touchend="touchEndLineA"></canvas>
		</view>
	</view>
</template>

<script>
	import uCharts from './u-charts/u-charts.js';
	var canvasObj = null;

	export default {
		props: ['data'],
		data() {
			return {
				cWidth: '',
				cHeight: '',
				pixelRatio: 1,
				serverData: '',
				itemCount: 30
			}
		},
		created() {
			this.cWidth = uni.upx2px(750);
			this.cHeight = uni.upx2px(272);
			this.fillData();
		},
		methods: {
			fillData() {
				let series = [{
						"data": this.data.max_degree,
						format(item) {
							return item + '°'
						},
						textSize: 14
					},
					{
						"data": this.data.min_degree,
						format(item, category) {
							return item + '°'
						},
						textSize: 14
					}
				]
				this.showLineA("canvasLineA", series);
			},
			showLineA(canvasId, series) {
				canvasObj = new uCharts({
					$this: this,
					canvasId: canvasId,
					type: 'line',
					fontSize: 11,
					legend: {
						show: false
					},
					colors: ['#FFB74D', '#4FC3F7'],
					background: '#FFFFFF',
					pixelRatio: this.pixelRatio,
					categories: ["昨天", "今天", "明天", "1", "1", "1", "1", "1"],
					series: series,
					animation: false,
					enableScroll: true, //开启图表拖拽功能,
					width: this.cWidth * this.pixelRatio,
					height: this.cHeight * this.pixelRatio,
					dataLabel: true,
					dataPointShape: true,
					// 直线还是曲线
					extra: {
						line: {
							type: 'curve'
						},
						tooltip: {
							showBox: false, //是否显示半透明黑色的提示区域
							bgColor: '#000000', //主体背景颜色
							bgOpacity: 0.7, //背景颜色透明度
							gridType: 'dash', //辅助线类型（虚线）
							dashLength: 5, //虚线单段长度
							gridColor: '#1890ff', //辅助线颜色
							fontColor: '#FFFFFF', //主体文字颜色
							horizentalLine: true, //是否显示横向辅助线
							xAxisLabel: true, //是否显示X轴辅助标签
							yAxisLabel: true, //是否显示Y轴辅助标签
							labelBgColor: '#DFE8FF', //标签背景颜色
							labelBgOpacity: 0.95, //背景颜色透明度
							labelFontColor: '#666666' //标签文字颜色
						}
					},
					xAxis: {
						disableGrid: true,
						disabled: true,
						itemCount: 6,

					},
					yAxis: {
						disableGrid: true,
						disabled: true
					}
				});
			},
			touchLineA(e) {
				canvasObj.scrollStart(e);
			},
			moveLineA(e) {
				canvasObj.scroll(e);
			},
			touchEndLineA(e) {
				canvasObj.scrollEnd(e);
			}
		}
	}
</script>

<style>
</style>
