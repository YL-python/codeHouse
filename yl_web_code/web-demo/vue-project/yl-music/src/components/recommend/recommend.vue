<template>
  <div id="recommend">
    <Scroll ref="scroll" class="recommend-content" :data="discList">
      <div class="content">
        <div v-if="recommends.length" class="slider-wrapper">
          <slider>
            <div v-for="(item,index) in recommends" :key="index">
              <a :href="item.linkUrl">
                <img class="needclick" @load="loadImage" :src="item.picUrl" alt />
              </a>
            </div>
          </slider>
        </div>
        <div class="recommend-list">
          <h1 class="list-title">热门歌单推荐</h1>
          <ul>
            <li v-for="(item,index) in discList" :key="index" class="item">
              <div class="icon">
                <img class="needclick" width="60px" height="60px" v-lazy="item.imgurl" alt />
              </div>
              <div class="text">
                <h2 class="name" v-html="item.creator.name"></h2>
                <p class="desc" v-html="item.dissname"></p>
              </div>
            </li>
          </ul>
        </div>
      </div>
      <div class="loading-container" v-show="!discList.length">
        <Loading title="加载中...等等呀"></Loading>
      </div>
    </Scroll>
  </div>
</template>
<script>
import Loading from "base/loading/loading";
import Scroll from "base/scroll/scroll";
import Slider from "base/slider/slider";
import { getRecommend, getDiscList } from "api/recommend";
import { ERR_OK } from "api/config";
export default {
  created() {
    this._getRecommend();
    this._getDiscList();
  },
  data() {
    return {
      recommends: [],
      discList: []
    };
  },
  methods: {
    _getRecommend() {
      getRecommend().then(res => {
        if (res.data.code === ERR_OK) {
          this.recommends = res.data.data.slider;
        }
      });
    },
    _getDiscList() {
      getDiscList().then(res => {
        if (res.data.code === ERR_OK) {
          this.discList = res.data.data.list;
        }
      });
    },
    loadImage() {
      // 真正达到最终数据的是轮播图和推荐列表都加载完成
      // 轮播图请求数据之后图片的加载也是异步
      // 所以有图片加载的时候我们就调用 batter-scroll 的refresh 方法
      //  但是我们只需要有一个图片加载成功就行，每加载一个图片刷新一次有很大的资源浪费
      // 定义一个变量，一开始是没有的，第一次加载图片的时候创建这个变量
      if (!this.firstLoadImage) {
        this.$refs.scroll.refresh();
        this.firstLoadImage = true;
      }
    }
  },
  components: {
    Slider,
    Scroll,
    Loading
  }
};
</script>
<style scoped lang="stylus" rel="stylesheet/stylus">
@import '~common/stylus/variable';

#recommend {
  position: fixed;
  width: 100%;
  top: 88px;
  bottom: 0;

  .recommend-content {
    height: 100%;
    overflow: hidden;

    .slider-wrapper {
      position: relative;
      width: 100%;
      overflow: hidden;
    }

    .recommend-list {
      .list-title {
        height: 65px;
        line-height: 65px;
        text-align: center;
        font-size: $font-size-medium;
        color: $color-theme;
      }

      .item {
        display: flex;
        box-sizing: border-box;
        align-items: center;
        padding: 0 20px 20px 20px;

        .icon {
          flex: 0 0 60px;
          width: 60px;
          padding-right: 20px;
        }

        .text {
          display: flex;
          flex-direction: column;
          justify-content: center;
          flex: 1;
          line-height: 20px;
          overflow: hidden;
          font-size: $font-size-medium;

          .name {
            margin-bottom: 10px;
            color: $color-text;
          }

          .desc {
            color: $color-text-d;
          }
        }
      }
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