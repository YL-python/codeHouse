<template>
  <div id="app">
    <v-header :seller="seller"></v-header>
    <div class="tab border-1px">
      <router-link tag="div" class="tab-item" to="/goods" active-class>商品</router-link>
      <router-link tag="div" class="tab-item" to="/ratings" active-class>评价</router-link>
      <router-link tag="div" class="tab-item" to="/seller" active-class>商家</router-link>
    </div>
    <keep-alive>
      <router-view :seller="seller"></router-view>
    </keep-alive>
  </div>
</template>

<script>
import header from "views/header/header";
import { getSeller } from "api/api.js";
const STATUS = 0;

export default {
  created() {
    this._getSeller();
  },
  data() {
    return {
      // 商家对象
      seller: {}
    };
  },
  methods: {
    _getSeller() {
      getSeller().then(res => {
        if (res.status === STATUS) {
          this.seller = res.data;
        }
      });
    }
  },
  components: {
    "v-header": header
  }
};
</script>

<style scoped lang='stylus'>
@import 'common/stylus/mixin.styl';

#app {
  .tab {
    display: flex;
    justify-content: space-around;
    align-items: center;
    height: 40px;
    font-size: 14px;
    color: rgb(77, 85, 93);
    border-1px(rgba(7, 17, 27, 0.1));

    .active {
      color: rgb(240, 22, 22);
    }
  }
}
</style>