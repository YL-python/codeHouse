<template>
  <div class="title">
    <h3>{{title}}</h3>
    <p>数据上一次更新时间：{{updataTime}}</p>
  </div>
</template>
<script>
export default {
  props: {
    // 检测类型
    title: {
      type: String,
      required: true
    },
    // 检测类型 + 其他验证
    updataTime: {
      type: String,
      default: "1970-00-00",
      required: true
    }
  }
};
</script>
<style scoped lang='less'>
.title {
  padding-top: 12px;
  padding-bottom: 12px;
  h3 {
    color: #000;
    font-size: 16px;
    font-weight: 700;
    margin-bottom: 10px;
  }
  p {
    color: #999;
    font-size: 12px;
  }
}
</style>