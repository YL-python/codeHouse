<!-- 发布内容页面 -->
<template>
	<view>
		<!-- 自定义导航 -->
		<uni-nav-bar left-icon="back" statusBar :border="false" @clickLeft="back" :shadow="true">
			<view class="flex align-center justify-center w-100">
				所有人可见 <text class="iconfont icon-shezhi"></text>
			</view>
		</uni-nav-bar>

		<!-- 文本域 -->
		<textarea v-model="nuiTextarea" placeholder="说一句话吧~" class="w-100 p-2"></textarea>

		<!-- 多图上传 -->
		<upload-image :show='show' ref='uploadImage' :list='imageList' @change='changeImage'></upload-image>

		<!-- 底部操作条 -->
		<view class="fixed-bottom bg-white flex align-center " style="height: 86rpx;">
			<view class="iconfont icon-caidan footer-btn animated " hover-class="jello"></view>
			<view class="iconfont icon-huati footer-btn animated" hover-class="jello"></view>
			<view class="iconfont icon-tupian footer-btn animated" hover-class="jello" @click="iconClickEvent('tupian')"></view>
			<view class="bg-main text-white ml-auto flex align-center justify-center rounded mr-2 animated" hover-class="jello"
			 style="width: 140rpx; height: 60rpx;">发布</view>
		</view>
	</view>
</template>

<script>
	import uniNavBar from "@/components/uni-ui/uni-nav-bar/uni-nav-bar.vue"
	import uploadImage from '@/components/common/upload-image.vue'
	export default {
		data() {
			return {
				nuiTextarea: "",
				imageList: [],
				flag: false // 是否显示了一次保存草稿
			}
		},
		onLoad() {
			this.flag = false
			let article = uni.getStorageSync('__add-input-article');
			if (article) {
				let {
					nuiTextarea,
					imageList
				} = JSON.parse(article)
				this.nuiTextarea = nuiTextarea
				// console.log('uni-add 读取内存了');
				this.imageList = imageList
			}
		},
		methods: {
			// 图标点击事件
			iconClickEvent(type) {
				switch (type) {
					case 'tupian':
						this.$refs.uploadImage.chooseImage()
						break;
				}
			},
			changeImage(imageList) {
				this.imageList = imageList
			},
			back() {
				uni.navigateBack({
					delta: 1
				})
			},
			// 保存道本地
			saveArticle() {
				let article = {
					nuiTextarea: this.nuiTextarea,
					imageList: this.imageList
				}
				uni.setStorageSync('__add-input-article', JSON.stringify(article))
			}
		},
		// 监听返回
		onBackPress() {
			//如果文本框没有值
			if (!this.nuiTextarea && this.imageList.length < 1) {
				return;
			}
			if (!this.flag) {
				uni.showModal({
					content: '是否保存为草稿',
					cancelText: '不保存',
					confirmText: '保存',
					success: (res) => {
						if (res.confirm) {
							//保存到草稿
							this.saveArticle()
						} else {
							//不保存清除缓存
							uni.removeStorageSync('__add-input-article')
						}
						this.flag = true;
						this.back()
					}
				})
				return true;
			}
		},
		computed: {
			show() {
				return this.imageList.length > 0
			}
		},
		components: {
			uniNavBar,
			uploadImage
		}
	}
</script>

<style>
	.footer-btn {
		width: 86rpx;
		height: 86rpx;
		display: flex;
		justify-content: center;
		align-items: center;
		font-size: 50rpx;
	}
</style>
