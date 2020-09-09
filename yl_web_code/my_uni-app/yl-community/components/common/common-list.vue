<template>
	<view class="p-2">
		<!-- 头像 昵称  |  关注 -->
		<view class="flex justify-between align-center ml-2">
			<view class="flex align-center ">
				<image class="userpic" :src="item.userpic" lazy-load @click="openSpace"></image>
				<view class="ml-2 ">
					<view class="lh-5 font">{{item.username}}</view>
					<view class="lh-5 font-sm text-light-muted">{{item.newstime}}</view>
				</view>
			</view>
			<view class="follow bg-main mr-2 rounded text-white animated faster" hover-class="jello" @click="follow(index)" v-if="!item.isFollow">关注</view>
		</view>
		<!-- 标题 -->
		<view class="font-md" @click="openDetail">{{item.title}}</view>
		<!-- 图片 -->
		<image v-if="item.titlepic" class="titlepic rounded" lazy-load :src="item.titlepic" @click="openDetail"></image>
		<!-- 图标按钮 -->
		<view class="flex align-center mt-2 pt-2 border-top">
			<view class="flex-1 flex justify-center animated faster" hover-class="jello" @click="doSupport('support',index)"
			 :class="item.support.type === 'support'?'support-active':''">
				<text class="iconfont icon-dianzan2 mr-2 "></text>
				<text>{{item.support.support_count > 0 ? item.support.support_count : '赞'}}</text>
			</view>
			<view class="flex-1 flex justify-center animated faster" hover-class="jello" @click="doSupport('unsupport',index)"
			 :class="item.support.type === 'unsupport'?'support-active':''">
				<text class="iconfont icon-cai mr-2"></text>
				<text>{{item.support.unsupport_count> 0 ? item.support.unsupport_count : '踩'}}</text>
			</view>
			<view class="flex-1 flex justify-center animated faster" hover-class="jello" @click="openDetail">
				<text class="iconfont icon-pinglun2 mr-2"></text>
				<text>{{item.comment_count> 0 ? item.comment_count : '抢首评'}}</text>
			</view>
			<view class="flex-1 flex justify-center animated faster" hover-class="jello" @click="openDetail">
				<text class="iconfont icon-fenxiang mr-2"></text>
				<text>{{item.share_num >= 0 ? item.share_num : ''}}</text>
			</view>
		</view>
	</view>
</template>

<script>
	export default {
		props: {
			item: Object,
			index: Number
		},
		methods: {
			// 点击头像打开个人空间
			openSpace() {

			},
			// 关注方法
			follow(index) {
				this.$emit("follow", index)
			},
			// 进入详情
			openDetail() {

			},
			// 顶踩操作
			doSupport(type, index) {
				this.$emit("doSupport", {
					type,
					index
				})
			}
		}
	}
</script>

<style>
	.userpic {
		width: 65rpx;
		height: 65rpx;
		display: block;
	}

	.titlepic {
		width: 100%;
		height: 350rpx;
		display: block;
	}

	.follow {
		width: 90rpx;
		height: 50rpx;
		text-align: center;
	}

	.support-active {
		color: #FF4A6A;
	}
</style>
