<template>
  <div class="tab">
    <router-link to="/recommend" tag="div" active-class="sel">
      <span>推荐</span>
    </router-link>
    <router-link to="/singer" tag="div" active-class="sel">
      <span>歌手</span>
    </router-link>
    <router-link to="/rank" tag="div" active-class="sel">
      <span>排行</span>
    </router-link>
    <router-link to="/my" tag="div" active-class="sel">
      <span>我的</span>
    </router-link>
  </div>
</template>
<script>
export default {}
</script>
<style lang="less" scoped>
@import "../../style/index.less";
.tab {
  .w(375);
  height: 44px;
  display: flex;
  div {
    text-align: center;
    width: 25%;
    font-size: @fs-s;
    color: rgba(255, 255, 255, 0.5);
    line-height: 44px;
    cursor:pointer;
    span {
      display: inline-block;
      height: 38px;
      border-bottom: 1px solid @black2;
    }
  }
  .sel {
    color: @yellow;
    span {
      display: inline-block;
      height: 38px;
      border-bottom: 1px solid @yellow;
    }
  }
}
</style>
