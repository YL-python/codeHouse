<template>
  <div class="player" v-if="songList.length">
    <div v-if="fullScreen" class="bigScreen">
      <!-- 头部 -->
      <div class="top">
        <span @click="changeScreen(false)">V</span>
        {{currentSong.songname}}
      </div>
      <!-- 背景 -->
      <div class="bg">
        <img :src="currentSong.albumUrl" alt />
      </div>
      <!-- 歌手 -->
      <p class="name">{{currentSong.singer[0].name}}</p>
      <!-- 专辑图片 -->
      <div class="img">
        <img :class="cd" :src="currentSong.albumUrl" alt />
      </div>
      <!-- 播放 -->
      <!-- <span @click="changeLoop">{{loops[loop]}}</span> -->
      <!-- <button @click="prev">上一曲</button> -->
      <button @click="togglePlay">播放</button>
      <!-- <span class="iconfont" @click="next">&#xe606;</span> -->
      <!-- 播放器 -->
      <audio ref='audio'
            @ended='ended'
            @canplay='canplay'
            @timeupdate="timeupdate"
            :src='currentSong.audioUrl'></audio>
    </div>
    </div>
    <div v-else class="smallScreen" @click="changeScreen(true)">小屏</div>
  </div>
</template>
<script>
/*
1.处理数据
2.显示数据渲染界面 name 歌手 专辑图片
3.专辑图片能动
4.显示歌词
5.控制器 前一曲 后一曲
  循环模式
    单曲循环  播完后在来一遍
    列表循环  播完之后播下个
    随机循环  播完之后随机放一个

6.进度条
  a.随着时间动
  b.可以点击控制歌曲播放
  c.可以拖动控制歌曲的播放
*/
import { mapState, mapMutations, mapGetters } from 'vuex'
export default {
  data () {
    return {
      startTime: 0,
      endTime: 0,
      loops: ['不循环', '单曲循环', '列表循环', '随机循环'],
      play: false,
      seekTime: 0
    }
  },
  computed: {
    ...mapState(['fullScreen', 'songList']),
    ...mapGetters(['currentSong']),
    cd () {
      return this.play ? 'cd' : 'cd paused'
    }
  },
  methods: {
    ...mapMutations(['changeScreen']),
    togglePlay () {
      this.play = !this.play
    }
  }
}
</script>
<style lang="less" scoped>
@import "../../style/index.less";
.player {
  color: #fff;
  .bigScreen {
    position: fixed;
    top: 0px;
    bottom: 0px;
    left: 0px;
    right: 0px;
    background: #222;
    .top{
      font-size: @fs-l;
      text-align: center
    }
    .name{
      font-size: @fs-s;
      text-align: center;
      padding: 10px;
    }
    .bg {
      position: absolute;
      z-index: -9;
      top: 0px;
      width: 100%;
      height: 100%;
      filter: blur(15px);
      img {
        width: 100%;
        height: 100%;
      }
    }
    .img {
      .w(375);
      .h(300);
      text-align: center;
      img {
        width: 75%;
        border-radius: 50%;
        border: 10px solid #ccc;
      }
      & .cd {
        animation: rotate 20s linear infinite;
      }
      & .paused {
        animation-play-state: paused;
      }
    }
  }
  .smallScreen {
    height: 60px;
    position: fixed;
    bottom: 0px;
    left: 0px;
    right: 0px;
    background: #333;
  }
  @keyframes rotate {
    0% {
      transform: rotate(0deg);
    }
    100% {
      transform: rotate(360deg);
    }
  }
}
</style>
