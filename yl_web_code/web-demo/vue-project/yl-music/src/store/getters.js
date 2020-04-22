// 歌手信息，歌手列表切换到歌手详情的时候作为一个参数使用
export const singer = state => state.singer

// 是否在播放
export const playing = state => state.playing

// 是否是大屏
export const fullScreen = state => state.fullScreen

// 播放列表
export const playList = state => state.playList

// 顺序歌曲列表
export const sequenceList = state => state.sequenceList

// 播放模式
export const mode = state => state.mode

// 当前播放的歌曲下标
export const currentIndex = state => state.currentIndex

// 当前播放的歌曲
export const currentSong = (state) => {
  return state.playList[state.currentIndex] || {}
}

// 推荐歌单
export const disc = state => state.disc

// 排行榜
export const topList = state => state.topList