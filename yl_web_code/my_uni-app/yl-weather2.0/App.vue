<script>
	export default {
		onLaunch: function() {
			uni.showLoading({
				title: '加载中',
				mask: true
			})
			uni.getLocation({
				type: 'wgs84',
				success(res) {
					uni.hideLoading();
					console.log('当前位置的经度：' + res.longitude);
					console.log('当前位置的纬度：' + res.latitude);
					uni.setStorageSync('yjtq_location', {
						lat: 39.984154,
						lng: 116.307490
					});
					// uni.request({
					// 	url: `https:coderyl.top/node/address/parse?lat=${res.latitude}&lng=${res.longitude}`,
					// 	success(resp) {
					// 		// console.log(resp);
					// 		let {
					// 			city,
					// 			district,
					// 			province
					// 		} = resp.data.result.ad_info
					// 		uni.setStorageSync('yjtq_nowLocation', {
					// 			province,
					// 			district,
					// 			city
					// 		});
					// 	}
					// })
				},
				fail() {
					uni.hideLoading();
					uni.showToast({
						title: '定位失败，确保手机开启定位功能，使用默认位置',
						icon: "loading",
						duration: 2000
					});
					uni.setStorageSync('yjtq_location', {
						lat: 39.984154,
						lng: 116.307490
					});
				},
				complete() {}
			});
		},
		onShow: function() {
			console.log('App Show')
		},
		onHide: function() {
			console.log('App Hide')
		}
	}
</script>

<style>
	/*每个页面公共css */
	/* 自定义图标库 */
	@import url("./static/css/icon.css");
	/* 动画库 */
	@import url("./static/css/animate.css");
	/* 公共的css */
	@import url("./static/css/free.css");
	/* 本项目 公共的css */
	@import url("./static/css/common.css");
</style>
