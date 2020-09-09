<template>
	<view class="">
		<!-- 顶部选项卡 -->
		<scroll-view scroll-x class="scroll-row border-bottom border-light-secondary" :scroll-into-view="scrollInto"
		 scroll-with-animation style="height: 100rpx;">
			<view class="scroll-row-item px-3 py-2 font-md" v-for="(item, index) in tabBars" :key="index" :id="'tab'+index"
			 :class="tabIndex === index ? 'font-lg  text-main font-weight-bold' : ''" @click="changeTab(index)">{{item.name}}</view>
		</scroll-view>

		<!-- 内容区域 -->
		<swiper :duration="150" :current="tabIndex" @change="onChangeTab" :style="'height:'+scrollH+'px'">
			<swiper-item v-for="(news, index1) in newsList" :key="index1">
				<scroll-view scroll-y="true" :style="'height:'+scrollH+'px'" @scrolltolower="loadmore(index1)">

					<template v-if="news.tabList.length > 0">
						<!-- 列表样式 -->
						<block v-for="(list,index2) in news.tabList" :key="index2">
							<topicList :item="list" :index="index2"></topicList>
						</block>

						<!-- 上拉加载 -->
						<load-more :loadMoreText="news.loadmore"> </load-more>
					</template>

					<!-- 无数据样式 -->
					<template v-else>
						<no-thing></no-thing>
					</template>

				</scroll-view>
			</swiper-item>
		</swiper>

	</view>
</template>

<script>
	const mock = [{
		cover: '/static/demo/topicpic/1.jpeg',
		title: "话题标题",
		desc: "话题描述啦啦啦啦啦啦啦啦啦",
		today_count: 8,
		news_count: 10
	}, {
		cover: '/static/demo/topicpic/1.jpeg',
		title: "话题标题",
		desc: "话题描述啦啦啦啦啦啦啦啦啦",
		today_count: 8,
		news_count: 10
	}, {
		cover: '/static/demo/topicpic/1.jpeg',
		title: "话题标题",
		desc: "话题描述啦啦啦啦啦啦啦啦啦",
		today_count: 8,
		news_count: 10
	}, {
		cover: '/static/demo/topicpic/1.jpeg',
		title: "话题标题",
		desc: "话题描述啦啦啦啦啦啦啦啦啦",
		today_count: 8,
		news_count: 10
	}, {
		cover: '/static/demo/topicpic/1.jpeg',
		title: "话题标题",
		desc: "话题描述啦啦啦啦啦啦啦啦啦",
		today_count: 8,
		news_count: 10
	}, {
		cover: '/static/demo/topicpic/1.jpeg',
		title: "话题标题",
		desc: "话题描述啦啦啦啦啦啦啦啦啦",
		today_count: 8,
		news_count: 10
	}, {
		cover: '/static/demo/topicpic/1.jpeg',
		title: "话题标题",
		desc: "话题描述啦啦啦啦啦啦啦啦啦",
		today_count: 8,
		news_count: 10
	}, {
		cover: '/static/demo/topicpic/1.jpeg',
		title: "话题标题",
		desc: "话题描述啦啦啦啦啦啦啦啦啦",
		today_count: 8,
		news_count: 10
	}]

	import topicList from "@/components/news/topic-list.vue"
	export default {
		data() {
			return {
				tabIndex: 0,
				scrollH: 600,
				scrollInto: '',
				// 顶部选项卡
				tabBars: [{
						name: "关注"
					}, {
						name: "推荐"
					},
					{
						name: "热点"
					},
					{
						name: "体育"
					},
					{
						name: "财经"
					},
					{
						name: "娱乐"
					},
					{
						name: "军事"
					},
					{
						name: "历史"
					}
				],
				// 首页动态数据
				newsList: []
			}
		},
		onLoad() {
			let res = uni.getSystemInfoSync()
			this.scrollH = res.windowHeight - uni.upx2px(102)
			this.getListData()
		},
		methods: {
			// 加载更多
			loadmore(index) {
				let list = this.newsList[index]
				if (list.loadmore !== '上拉加载更多') {
					return
				}

				list.loadmore = '加载中...'
				setTimeout(() => {
					// 加载数据
					list.tabList = [...list.tabList, ...list.tabList]
					// 回复加载状态
					list.loadmore = '上拉加载更多'
				}, 2000)
			},
			getListData() {
				let arr = []
				for (var i = 0; i < this.tabBars.length; i++) {
					let obj = {
						// 三种状态，加载中...，上拉加载更多，没有更多了
						loadmore: "上拉加载更多",
						tabList: []
					}
					if (i < 3) {
						obj.tabList = mock
					}
					arr.push(obj)
				}
				this.newsList = arr
			},
			// 监听滑动
			onChangeTab(e) {
				this.changeTab(e.detail.current)
			},
			// 切换选项卡
			changeTab(index) {
				if (this.tabIndex === index) {
					return
				}
				this.tabIndex = index
				this.scrollInto = 'tab' + index
			}
		},
		components: {
			topicList
		}
	}
</script>

<style>

</style>
