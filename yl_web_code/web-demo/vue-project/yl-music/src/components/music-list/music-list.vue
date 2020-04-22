<template>
  <div class="music-list">
    <div class="back" @click="back">
      <i class="icon-back"></i>
    </div>
    <h1 class="title" v-html="title"></h1>
    <div class="bg-image" ref="bgImage" :style="bgStyle">
      <div class="play-wrapper">
        <div ref="playBtn" v-show="songs.length>0" class="play" @click="random">
          <i class="icon-play"></i>
          <span class="text">随机播放全部</span>
        </div>
      </div>
      <!-- 蒙版 -->
      <div class="filter" ref="filter"></div>
    </div>
    <!-- 向上滑动的时候用 这个块 来做一个背景 -->
    <div class="bg-layer" ref="layer"></div>
    <scroll
      :data="songs"
      @scroll="scroll"
      :listen-scroll="listenScroll"
      :probe-type="probeType"
      class="list"
      ref="list"
    >
      <div class="song-list-wrapper">
        <song-list :songs="songs" :rank="rank" @select="selectItem"></song-list>
      </div>
      <div v-show="!songs.length" class="loading-container">
        <loading></loading>
      </div>
    </scroll>
  </div>
</template>

<script type="text/ecmascript-6">
import Scroll from "base/scroll/scroll";
import Loading from "base/loading/loading";
import SongList from "base/song-list/song-list";
import { mapActions } from "vuex";
import { playlistMixin } from "common/js/mixin";
// import { prefixStyle } from "common/js/dom";

// 预留的高度，计算向上滚动的时候用到
const RESERVED_HEIGHT = 40;
// const transform = prefixStyle("transform");
// 这里有个bug， backdropFilter属性 加前缀的没有，不加前缀的就有
// const backdrop = prefixStyle("backdropFilter");

export default {
  mixins: [playlistMixin],
  props: {
    bgImage: {
      // 背景图
      type: String,
      default: ""
    },
    songs: {
      // 歌曲列表
      type: Array,
      default: null
    },
    title: {
      // 标题
      type: String,
      default: ""
    },
    rank: {
      // 有没有排行图标
      type: Boolean,
      default: false
    }
  },
  computed: {
    bgStyle() {
      return `background-image:url(${this.bgImage})`;
    }
  },
  created() {
    this.probeType = 3;
    this.listenScroll = true;
    // 获取背景图的高度，在初始化滚动列表的时候设置滚动区域的高度
    this.imageHeight = 0;
  },
  mounted() {
    // 获取背景图的高度，在初始化滚动列表的时候设置滚动区域的高度
    this.imageHeight = this.$refs.bgImage.clientHeight;
    this.$refs.list.$el.style.top = `${this.imageHeight}px`;
    // layer块能滚动的距离  向上滚是 负值
    this.minTransalteY = -this.imageHeight + RESERVED_HEIGHT;
  },
  data() {
    return {
      scrollY: -1 // 纵向滚动的值
    };
  },
  methods: {
    back() {
      this.$router.back();
    },
    scroll(pos) {
      this.scrollY = pos.y;
    },
    selectItem(item, index) {
      this.selectPlay({
        list: this.songs,
        index
      });
    },
    // 随机播放功能
    random() {
      this.randomPlay({
        list: this.songs
      });
    },
    handlePlaylist(playList) {
      const bottom = playList.length > 0 ? "60px" : "";
      this.$refs.list.$el.style.bottom = bottom;
      this.$refs.list.refresh();
    },
    ...mapActions(["selectPlay", "randomPlay"])
  },

  watch: {
    scrollY(newVal) {
      // console.log(newVal);  // 向上滚是 负值
      // 监听滚动，让 layer块滚动
      let translateY = Math.max(this.minTransalteY, newVal);
      let zIndex = 0; // 图片的 z-index
      let scale = 1; // 图片的放大倍率
      let blur = 0; // 图片的模糊
      const percent = Math.abs(newVal / this.imageHeight);
      if (newVal > 0) {
        // 向下滚动的逻辑
        scale = 1 + percent;
        zIndex = 10; // layer会遮住图片，修改z-index
      } else {
        blur = Math.min(20, percent * 10);
      }

      this.$refs.layer.style["transform"] = `translate3d(0,${translateY}px,0)`;
      this.$refs.filter.style["backdrop-filter"] = `blur(${blur}px)`;
      if (newVal < this.minTransalteY) {
        // 滚动到最顶部，修改图片的z-index以及高度
        zIndex = 10;
        // 修改paddingTop 是因为一开始图片没加载出来的时候也需要高度 设置滚动区域距离顶部的高度
        // 我们就用paddingTop=70% height=0 来设置高度
        // 现在就需要设置真正高度，就需要吧 paddingTop = 0
        this.$refs.bgImage.style.paddingTop = 0;
        this.$refs.bgImage.style.height = `${RESERVED_HEIGHT}px`;
        this.$refs.playBtn.style.display = "none";
      } else {
        this.$refs.bgImage.style.paddingTop = "70%";
        this.$refs.bgImage.style.height = 0;
        this.$refs.playBtn.style.display = "";
      }
      this.$refs.bgImage.style["transform"] = `scale(${scale})`;
      this.$refs.bgImage.style.zIndex = zIndex;
    }
  },
  components: {
    Scroll,
    Loading,
    SongList
  }
};
</script>

<style scoped lang="stylus" rel="stylesheet/stylus">
@import '~common/stylus/variable';
@import '~common/stylus/mixin';

.music-list {
  position: fixed;
  z-index: 100;
  top: 0;
  left: 0;
  bottom: 0;
  right: 0;
  background: $color-background;

  .back {
    position: absolute;
    top: 0;
    left: 6px;
    z-index: 50;

    .icon-back {
      display: block;
      padding: 10px;
      font-size: $font-size-large-x;
      color: $color-theme;
    }
  }

  .title {
    position: absolute;
    top: 0;
    left: 10%;
    z-index: 40;
    width: 80%;
    no-wrap();
    text-align: center;
    line-height: 40px;
    font-size: $font-size-large;
    color: $color-text;
  }

  .bg-image {
    position: relative;
    width: 100%;
    height: 0;
    padding-top: 70%;
    transform-origin: top;
    background-size: cover;

    .play-wrapper {
      position: absolute;
      bottom: 20px;
      z-index: 50;
      width: 100%;

      .play {
        box-sizing: border-box;
        width: 135px;
        padding: 7px 0;
        margin: 0 auto;
        text-align: center;
        border: 1px solid $color-theme;
        color: $color-theme;
        border-radius: 100px;
        font-size: 0;

        .icon-play {
          display: inline-block;
          vertical-align: middle;
          margin-right: 6px;
          font-size: $font-size-medium-x;
        }

        .text {
          display: inline-block;
          vertical-align: middle;
          font-size: $font-size-small;
        }
      }
    }

    .filter {
      position: absolute;
      top: 0;
      left: 0;
      width: 100%;
      height: 100%;
      background: rgba(7, 17, 27, 0.4);
    }
  }

  .bg-layer {
    position: relative;
    height: 100%;
    background: $color-background;
  }

  .list {
    position: fixed;
    top: 0;
    bottom: 0;
    width: 100%;
    background: $color-background;

    .song-list-wrapper {
      padding: 20px 30px;
    }

    .loading-container {
      position: absolute;
      width: 100%;
      top: 50%;
      transform: translateY(-50%);
    }
  }
}
</style>