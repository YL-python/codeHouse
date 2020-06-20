<template>
  <div class="recommend">
    recommend
    <carousel :images='bannerList'></carousel>
  </div>
</template>
<script>
import carousel from "../../base/carousel/carousel";
import { getBannerData } from "../../common/js/recommend";
export default {
  created() {
    this._getBannerData();
  },
  data() {
    return {
      bannerList: []
    };
  },
  methods: {
    _getBannerData() {
      getBannerData().then(({banners}) => {
        this.bannerList = banners.map((item)=>{
          return item.pic
        })
      });
    }
  },
  components: {
    carousel
  }
};
</script>
<style scoped>
</style>