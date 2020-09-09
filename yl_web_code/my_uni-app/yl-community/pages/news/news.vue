<!-- 动态页 -->
<template>
	<view>
		<!-- 自定义导航栏 -->
		<uni-nav-bar :shadow='false' fixed statusBar @clickRight="openAddInput">
			<view class="flex align-center justify-center font-weight-bold w-100">
				<text class="font-md mx-1" :class="index === tabIndex ?'text-main font-lg':'text-light-muted font-md'" v-for="(item,index) in tabBars"
				 :key='index' @click="changeTab(index)">{{item.name}}</text>
			</view>
			<view slot='right' class="iconfont icon-fatie_icon"></view>
		</uni-nav-bar>

		<!-- 内容页 -->
		<swiper :duration="150" :style="'height:'+scrollH+'px'" :current="tabIndex" @change="onChangeTab">
			<!-- 关注 -->
			<swiper-item>
				<scroll-view scroll-y="true" :style="'height:'+scrollH+'px'" @scrolltolower="loadmoreEvent()">
					<block v-for="(list,index) in list" :key="index" @follow='follow' @doSupport='doSupport'>
						<commonList :item="list" :index="index" @follow='follow' @doSupport='doSupport'></commonList>
						<divider></divider>
					</block>
					<!-- 上拉加载 -->
					<load-more :loadMoreText="loadmore"> </load-more>
				</scroll-view>
			</swiper-item>
			<!-- 话题 -->
			<swiper-item>
				<scroll-view scroll-y="true" :style="'height:'+scrollH+'px'">
					<!-- 热门分类 -->
					<hot-cate :hotCate='hotCate'></hot-cate>
					<!-- 搜索框 -->
					<view class="p-2">
						<view class="bg-light rounded flex align-center justify-center py-2 text-secondary">
							<text class="iconfont icon-sousuo"></text>
							<text class="ml-2">搜索更多</text>
						</view>
					</view>
					<!-- 轮播图 -->
					<swiper indicator-dots autoplay circular :interval="3000" :duration="1000" class="px-2 pb-2">
						<swiper-item>
							<image src="/static/demo/banner1.jpg" style="height: 300rpx;" class="w-100 rounded"></image>
						</swiper-item>
						<swiper-item>
							<image src="/static/demo/banner2.jpg" style="height: 300rpx;" class="w-100 rounded"></image>
						</swiper-item>
						<swiper-item>
							<image src="/static/demo/banner3.jpg" style="height: 300rpx;" class="w-100 rounded"></image>
						</swiper-item>
					</swiper>
					<divider></divider>

					<!-- 最近更新 -->
					<view class="p-2 font-md">最近更新</view>
					<!-- 话题列表 -->
					<block v-for='(item,index) in topicList' :key='index'>
						<topic-list :item='item' :index='index'></topic-list>
					</block>
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
		isFollow: true,
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
		isFollow: true,
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
		isFollow: true,
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
	import uniNavBar from "@/components/uni-ui/uni-nav-bar/uni-nav-bar.vue"
	import commonList from "@/components/common/common-list.vue"
	import hotCate from "@/components/news/hot-cate.vue"
	import topicList from "@/components/news/topic-list.vue"
	export default {
		data() {
			return {
				scrollH: "",
				tabIndex: 0,
				tabBars: [{
					name: "关注"
				}, {
					name: "话题"
				}],
				// 关注列表数据
				list: [],
				// 三种状态，加载中...，上拉加载更多，没有更多了
				loadmore: "上拉加载更多",
				// 热门分类
				hotCate: [{
					name: '关注'
				}, {
					name: '推荐'
				}, {
					name: '体育'
				}, {
					name: '热点'
				}, {
					name: '财经'
				}, {
					name: '娱乐'
				}],
				// 话题列表数据
				topicList: [{
					cover: '/static/demo/topicpic/1.jpeg',
					title: "话题标题",
					desc: "话题描述啦啦啦啦啦啦啦啦啦话题描述啦啦啦啦啦啦啦啦啦话题描述啦啦啦啦啦啦啦啦啦话题描述啦啦啦啦啦啦啦啦啦话题描述啦啦啦啦啦啦啦啦啦",
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
			};
		},
		onLoad() {
			let res = uni.getSystemInfoSync()
			// 44 是导航栏源码内设置的高度
			this.scrollH = res.windowHeight - res.statusBarHeight - 44
			this.list = mock
		},
		methods: {
			// 导航栏点击事件，切换选项卡
			changeTab(index) {
				this.tabIndex = index
			},
			// 跳转到发布页
			openAddInput() {
				uni.navigateTo({
					url: '../add-input/add-input'
				})
			},
			// 轮播图切换触发事件
			onChangeTab(e) {
				this.tabIndex = e.detail.current
			},
			// 顶踩
			doSupport(e) {
				let item = this.list[e.index].support
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
			},
			// 上拉加载更多
			loadmoreEvent() {
				// 验证当前的状态是否是可加载状态
				if (this.loadmore !== '上拉加载更多') {
					return
				}
				this.loadmore = '加载中...'
				setTimeout(() => {
					// 加载数据
					this.list = [...this.list, ...this.list]
					// 回复加载状态
					this.loadmore = '上拉加载更多'
				}, 2000)
			},
		},
		components: {
			uniNavBar,
			commonList,
			hotCate,
			topicList
		}
	}
</script>

<style lang="scss">

</style>
