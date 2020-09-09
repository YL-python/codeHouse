<template>
	<view>
		<template v-if="serachList.length === 0">
			<!-- 搜索历史 -->
			<view class="py-2 font-md px-2">搜索历史</view>
			<view class="flex flex-wrap">
				<view class="border rounded font mx-2 my-1 px-2" hover-class="bg-light" @click="searchHistoryEvent(item)" v-for="(item,index) in historyList"
				 :key='index'>{{item}}</view>
			</view>
		</template>
		<!-- 搜索结果 -->
		<template v-else>
			<block v-for="(item,index) in serachList" :key='index'>
				<commonList :item="item" :index="index"></commonList>
			</block>
		</template>

	</view>
</template>

<script>
	const mock = [{
		username: '昵称',
		userpic: '/static/default.jpg',
		newstime: '2019-10-20 下午 04:03',
		isFollow: false,
		title: '我是标题',
		titlepic: "",
		support: {
			type: "support",
			support_count: 1,
			unsupport_count: 1
		},
		comment_count: 2,
		share_num: 2
	}, {
		username: '昵称',
		userpic: '/static/default.jpg',
		newstime: '2019-10-20 下午 04:03',
		isFollow: false,
		title: '我是标题',
		titlepic: "/static/demo/datapic/2.jpg",
		support: {
			type: "unsupport",
			support_count: 1,
			unsupport_count: 1
		},
		comment_count: 2,
		share_num: 2
	}, {
		username: '昵称',
		userpic: '/static/default.jpg',
		newstime: '2019-10-20 下午 04:03',
		isFollow: false,
		title: '我是标题',
		titlepic: "/static/demo/datapic/2.jpg",
		support: {
			type: "",
			support_count: 1,
			unsupport_count: 1
		},
		comment_count: 0,
		share_num: 0
	}]
	import commonList from "@/components/common/common-list.vue"
	export default {
		data() {
			return {
				historyList: ['uni-app 第二季商城实战开发', '第三季 仿微信', '社区交友', '小小'],
				searchText: '',
				// 模拟搜索结果数据
				serachList: []
			}
		},
		// 输入框改变事件
		onNavigationBarSearchInputChanged(obj) {
			console.log('onNavigationBarSearchInputChanged', obj);
			this.searchText = obj.text
		},
		// 输入框提交时间，用户按回车时触发
		onNavigationBarSearchInputConfirmed(obj) {
			console.log('onNavigationBarSearchInputConfirmed', obj);
			this.searchEvent()
		},
		// 导航栏按钮点击事件
		onNavigationBarButtonTap(obj) {
			console.log('onNavigationBarButtonTap', obj);
			// index 是按钮的索引，可能存在多个按钮
			if (obj.index === 0) {
				this.searchEvent()
			}
		},
		methods: {
			// 点击搜索历史事件
			searchHistoryEvent(text) {
				this.searchText = text
				this.searchEvent()
			},
			// 搜索事件
			searchEvent() {
				// 收起键盘
				uni.hideKeyboard()
				// 加载状态
				uni.showLoading({
					title: "加载中",
					mask: false
				})
				// 请求搜索
				setTimeout(() => {
					this.serachList = mock
					uni.hideLoading()
				}, 1000)
			}
		},
		components: {
			commonList
		}
	}
</script>

<style>

</style>
