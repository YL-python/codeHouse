import Vue from 'vue'
import Vuex from 'vuex'

Vue.use(Vuex)

const store = new Vuex.Store({
  state: {
    // 歌曲列表
    songList: [],
    // 大屏播放器
    fullScreen: true,
    currentIndex: -1 // 表示当前正在播放哪一首歌
  },
  mutations: {
    // 控制大小屏切换
    changeScreen (state, screenState) {
      state.fullScreen = screenState
    },
    // 把歌手页的所有歌曲信息添加过来
    addSongList (state, params) {
      state.songList = params
    },
    // 改变下标，表示我选择了哪一首歌
    changeCurrentIndex (state, index) {
      state.currentIndex = index
    }
  },
  getters: {
    // 通过歌曲信息列表和下标，获得当前的歌曲信息
    currentSong (state) {
      return state.songList[state.currentIndex] || null
    }
  }
})

export default store
