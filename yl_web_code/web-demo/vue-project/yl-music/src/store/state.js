import {playMode} from '../common/js/config'
import {loadSearch, loadPlay, loadFavorite} from 'common/js/cache'

// 定义一些属性是值的时候一般是全局属性
// 定义一些属性是对象的时候一般是子路由跳转的参数

const state = {
  singer:{},
  playing:false,  // 播放器是否播放
  fullScreen:true,  // 全屏 小屏
  playList:[],  // 播放歌曲列表
  sequenceList:[],  // 顺序播放时的列表
  mode: playMode.sequence,  // 播放方式  顺序，循环，随机
  currentIndex:-1,  // 播放的索引
  disc: {},  // 推荐歌单
  topList:{},  // 排行榜
  searchHistory: loadSearch(),  // 搜索历史
  playHistory: loadPlay(),  // 播放历史
  favoriteList: loadFavorite()  // 喜欢历史
}

export default state