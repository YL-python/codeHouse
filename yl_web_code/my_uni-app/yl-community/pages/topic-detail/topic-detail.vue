<!-- 话题详情页 -->
<template>
	<view>
		<topicInfo :info='info'></topicInfo>
		<divider></divider>
		<!-- 话题置顶帖子 -->
		<block v-for='(item,topListindex) in topList' :key='topListindex'>
			<view class="flex align-center p-2  border-bottom" hover-class="bg-light">
				<text class="iconfont icon-xihuan text-main"></text>
				<text class="font-md text-dark text-ellipsis">
					{{item.title}}
				</text>
			</view>
		</block>
		<divider></divider>
		<!-- 内容区 -->
		<!-- tab -->
		<view class="flex align-center py-2 border-bottom">
			<block v-for='(item,tabBarsindex) in tabBars' :key='tabBarsindex'>
				<view class="flex-1 flex align-center justify-center " @click="tabIndex = tabBarsindex" :class="tabBarsindex === tabIndex?'font-lg font-weight-bold text-main':'font-md'">{{item.name}}</view>
			</block>
		</view>
		<template v-if="tabList.length > 0">
			<!-- 对应内容 -->
			<block v-for='(item,tabListindex) in tabList' :key='tabListindex'>
				<commonList :item="item" :index="tabListindex"></commonList>
				<divider></divider>
			</block>
		</template>
		<template v-else>
			<noThing></noThing>
		</template>
		<loadMore :loadMoreText='loadText'></loadMore>
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
	import topicInfo from '@/components/topic-detail/topic-info.vue'
	import commonList from "@/components/common/common-list.vue"
	export default {
		data() {
			return {
				info: {},
				topList: [{
					title: '【新人必读】uni-app实战教程第二季商城类项目开发'
				}, {
					title: '【新人必读】uni-app实战教程第三季微信项目开发'
				}],
				tabIndex: 0,
				tabBars: [{
					name: '默认'
				}, {
					name: '最新'
				}],
				// 默认数据
				list0: [],
				loadText0: "上拉加载更多",
				// 最新数据
				list1: [],
				loadText1: "上拉加载更多",
			}
		},
		onLoad(e) {
			if (e.detail) {
				this.info = JSON.parse(e.detail)
				this.list0 = mock
			}
		},
		// 触底事件
		onReachBottom() {
			// console.log('shangla ');
			this.loadmore()
		},
		methods: {
			loadmore() {
				let index = this.tabIndex

				if (this['loadText' + index] !== '上拉加载更多') {
					return;
				}

				this['loadText' + index] = '加载中...'
				setTimeout(() => {
					// 加载数据
					this['list' + index] = [...this['list' + index], ...this['list' + index]]
					// 回复加载状态
					this['loadText' + index] = '上拉加载更多'
				}, 2000)
			},
		},
		computed: {
			tabList() {
				// if (this.tabIndex === 0) {
				// 	return this.list0
				// } else {
				// 	return this.list1
				// }
				return this['list' + this.tabIndex]
			},
			loadText() {
				return this['loadText' + this.tabIndex]
			}
		},
		components: {
			topicInfo,
			commonList
		}
	}
</script>

<style>

</style>
