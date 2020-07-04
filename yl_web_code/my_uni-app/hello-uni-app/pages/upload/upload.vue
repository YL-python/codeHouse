<template>
	<view>
		<view> upload </view>
		<button type="default" @click="chooseImg">上传图片</button>
		<image v-for="(item ,index) in imgArr" :key="index" :src="item" @click="preViewImg(item)"></image>
	</view>
</template>

<script>
	export default {
		data() {
			return {
				imgArr: []
			}
		},
		methods: {
			chooseImg() {
				console.log('chooseImg 方法被调用');
				uni.chooseImage({
					// 存在 this 指向问题
					success: (res) => {
						console.log(res);
						this.imgArr = res.tempFilePaths
					}
				})
			},
			preViewImg(current) {
				console.log("img 被点击");
				uni.previewImage({
					current,
					urls: this.imgArr
				})
				
			}
		}
	}
</script>

<style>

</style>
