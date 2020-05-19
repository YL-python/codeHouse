<template>
  <div class="detail">
    <div class="back">
      <span @click="back">&lt;</span>
    </div>
    <div class="title">{{name}}</div>
    <div class="avator" :style="{'background-image':`url(${avator})`}" ref="img">
      <div class="filter"></div>
    </div>
    <div class="songlist" ref="songlist">
      <div class="content">
        <ul>
          <li v-for="(item,index) in list" :key="index" @click="openPlayer(index)">
            <h2>{{item.songname}}</h2>
            <p>{{name}}-{{item.albumname}}</p>
          </li>
        </ul>
      </div>
    </div>
  </div>
</template>
<script>
/*
1.显示歌手名 v
2.显示歌手图片 v
3.显示歌单 v
4.返回 v
5.下拉头像放大 v
6.上滑遮住头像 v
7.随机播放
8.点击跳转到播放器页面
*/
import { getSongByMid } from '../../api/api'
import BS from 'better-scroll'
import { mapMutations } from 'vuex'
export default {
  data () {
    return {
      list: [],
      name: '加载中',
      avator: ''
    }
  },
  methods: {
    ...mapMutations(['addSongList', 'changeCurrentIndex', 'changeScreen']),
    openPlayer (index) {
      // 点击歌的li显示歌播放器
      this.addSongList(this.list)
      // 确定点击的是哪一首歌
      this.changeCurrentIndex(index)
      // 点击之后屏幕变大
      this.changeScreen(true)
    },
    back () {
      this.$router.go(-1)
    },
    initBS () {
      const img = this.$refs.img
      const imgH = img.clientHeight
      /* eslint-disable no-new */
      this.Bs = new BS(this.$refs.songlist, { probeType: 3, click: true })
      // 监听滚动
      this.Bs.on('scroll', ({ y }) => {
        // 获取图片的元素和高度
        if (y >= 0) {
          // 下拉放大
          const precent = 1 + y / imgH
          img.style.transform = `scale(${precent})`
          img.style.zIndex = 1
        } else {
          // 向上滚动
          // 没有到顶部 滚动层的层级高
          // 到达顶部额时候 图片的层级高
          if (Math.abs(y) > imgH - 40) {
            img.style.zIndex = 1
            img.style.paddingTop = '0%'
            img.style.height = '40px'
          } else {
            img.style.zIndex = -1
            img.style.paddingTop = '70%'
            img.style.height = 0
          }
        }
      })
    },
    handleList (list) {
      let result = []
      result = list.map((item, index) => {
        const { albummid, albumname, singer, songmid, songname } = item.musicData
        const albumUrl = `https://y.gtimg.cn/music/photo_new/T002R300x300M000${albummid}.jpg?max_age=2592000`
        return { albummid, albumname, singer, songmid, songname, albumUrl }
      })
      return result
    }
  },
  created () {
    // console.log(this.$route)
    const { singermid } = this.$route.params
    getSongByMid(singermid).then(res => {
      // console.log(res)
      this.list = this.handleList(res.data.list)
      this.name = res.data.singer_name
      this.avator = `https://y.gtimg.cn/music/photo_new/T001R300x300M000${singermid}.jpg?max_age=2592000`
      this.$nextTick(() => [this.initBS()])
    })
  }
}
</script>
<style lang="less" scoped>
@import "../../style/index.less";
.detail {
  position: fixed;
  top: 0px;
  right: 0px;
  left: 0px;
  bottom: 0px;
  background: #222;
  .back {
    width: 40px;
    height: 40px;
    color: #ffcd32;
    font-size: 32px;
    line-height: 40px;
    text-align: center;
    position: absolute;
    top: 0px;
    left: 6px;
    z-index: 50;
  }
  // 头部
  .title {
    height: 40px;
    color: #fff;
    text-align: center;
    line-height: 40px;
    font-size: 18px;
    width: 80%;
    position: absolute;
    top: 0;
    left: 10%;
    z-index: 40;
  }
  // 图片
  .avator {
    position: absolute;
    width: 100%;
    padding-top: 70%;
    background-size: cover;
    top: 0px;
    z-index: -1;
    .filter {
      position: absolute;
      top: 0;
      left: 0;
      width: 100%;
      height: 100%;
      background: rgba(7, 17, 27, 0.4);
    }
  }
  // 列表
  .songlist {
    position: fixed;
    background: #222;
    // overflow: hidden;
    top: 270px;
    bottom: 0px;
    left: 0px;
    right: 0px;
    .content {
      padding: 10px 30px;
      background: #222;
      li {
        font-size: @fs-s;
        height: 64px;
        color: #fff;
        box-sizing: border-box;
        h2 {
          font-size: @fs-s;
          height: 20px;
          overflow: hidden;
        }
        p {
          height: 20px;
          margin-top: 4px;
          color: hsla(0, 0%, 100%, 0.3);
          overflow: hidden;
          border-bottom: hsla(0, 0%, 100%, 0.3) 1px solid;
        }
      }
    }
  }
}
</style>
