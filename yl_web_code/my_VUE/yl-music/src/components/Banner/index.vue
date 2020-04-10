<template>
  <div class="banner">
    <div class="swiper-container">
      <div class="swiper-wrapper">
        <div class="swiper-slide" v-for="(item,index) in banners" :key="index">
          <img :src="item.picUrl" alt />
        </div>
      </div>
    </div>
  </div>
</template>
<script>
import Swiper from 'swiper'
export default {
  methods: {
    initBanner () {
      /* eslint-disable no-new */
      new Swiper('.swiper-container', { loop: true })
    }
  },
  // mounted () {
  //   this.initBanner()
  // },
  watch: {
    // 外面穿过来的数据,数据改变才初始化轮播图
    banners () {
      // banners 改变,网络请求成功
      this.$nextTick(() => {
        this.initBanner()
      })
    }
  },
  props: {
    banners: {
      type: Array,
      // default: () => [] // es6的箭头函数
      default: function () { return [] }
    }
  }
}
</script>>
<style lang="less" scoped>
@import "../../style/index.less";
@import "~swiper/css/swiper.min.css";
.swiper-container {
  .w(375);
  .h(150);
  img {
    .w(375);
    .h(150);
  }
}
</style>
