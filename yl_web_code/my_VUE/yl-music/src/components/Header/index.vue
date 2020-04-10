<template>
  <div class="header">
    <img src="/favicon.ico" alt />
    <span>YL-music</span>
  </div>
</template>
<script>
export default {}
</script>
<style lang="less" scoped>
@import "../../style/index.less";
.header {
  color: @yellow;
  font-size: @fs-l;
  display: flex;
  justify-content: center;
  align-items: center;
  .w(375);
  height: 44px;
  img {
    width: 18px;
    height: 18px;
    margin-right: 5px;
  }
}
</style>
