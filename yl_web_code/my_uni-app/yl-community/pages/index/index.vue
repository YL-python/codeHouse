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
							<commonList :item="list" :index="index2" @follow='follow' @doSupport='doSupport'></commonList>
							<divider></divider>
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
		// 监听导航栏搜索框的点击
		onNavigationBarSearchInputClicked() {
			uni.navigateTo({
				url: "../search/search"
			})
		},
		// 导航栏按钮点击事件
		onNavigationBarButtonTap(obj) {
			// index 是按钮的索引，可能存在多个按钮
			if (obj.index === 0) {
				uni.navigateTo({
					url: "../add-input/add-input"
				})
			}
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
			},
			// 关注
			follow(index) {
				this.newsList[this.tabIndex].tabList[index].isFollow = true
				uni.showToast({
					title: "关注成功"
				})
			},
			// 顶踩
			doSupport(e) {
				let item = this.newsList[this.tabIndex].tabList[e.index].support
				if (item.type === '') {
					item.type = e.type
					item[e.type + '_count']++
				} else if (item.type === 'support' && e.type === 'unsupport') {
					item.type = e.type
					item['support_count']--
					item['unsupport_count']++
				} else if (item.type === 'unsupport' && e.type === 'support') {
					item.type = e.type
					item['support_count']++
					item['unsupport_count']--
				} else if (item.type === 'support' && e.type === 'support') {
					item.type = ''
					item['support_count']--
				} else if (item.type === 'unsupport' && e.type === 'unsupport') {
					item.type = ''
					item['unsupport_count']--
				}
			}
		},
		components: {
			commonList
		}
	}
</script>

<style>

</style>
