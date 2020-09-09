<script>
	import {
		mapMutations
	} from "vuex";
	export default {
		onLaunch: function() {
			// console.log('onLaunch')
			this.$myRequest({
				url: 'ip'
			}).then(res => {
				let flag = false
				let {
					province,
					city,
					district
				} = res.result.ad_info
				if (res.status === 0 && district && city && province) {
					flag = true
				}
				if (flag) {
					this.setNowLocation({
						province,
						city,
						district
					});
				} else {
					setTimeout(() => {
						uni.showToast({
							title: '定位失败使用默认位置',
							icon: "none",
						});
						setTimeout(() => {
							uni.hideToast();
						}, 2000)
					}, 0);
					this.setNowLocation({
						province: '北京市',
						city: '北京市',
						district: '东城区'
					});
				}
			})
		},
		// http://coderyl.top/node/weather?weather_type=observe&province=北京市&city=北京城区&county=东城区
		methods: {
			...mapMutations(['setNowLocation'])
		}
	}
</script>

<style>
	/*每个页面公共css */

	/* 图标 css */
	@import url('./static/css/icon.css');
	/* @import 'https://at.alicdn.com/t/font_1924410_c3x9gxui3gp.css'; */

	body,
	html {
		font: Simsun, Helvetica, Arial, sans-serif;
		background-color: #F4F4F4;
	}
</style>
