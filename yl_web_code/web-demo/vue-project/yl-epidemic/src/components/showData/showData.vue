<template>
  <div class="show-data">
    <h3 class="title">{{title}}</h3>
    <p class="data" :style="{ color: dataColor}">{{data}}</p>
    <p class="sub-data">
      昨日
      <span :style="{ color: dataColor}">+{{subData}}</span>
    </p>
  </div>
</template>
<script>
import colorObj from "./color";
export default {
  props: {
    title: {
      type: String,
      default: "标题",
      required: true
    },
    data: {
      type: String,
      default: "0",
      required: true
    },
    subData: {
      type: String,
      default: "0",
      required: true
    }
  },
  computed: {
    dataColor() {
      if (colorObj[this.title]) {
        return colorObj[this.title];
      } else {
        return "#000";
      }
    }
  }
};
</script>
<style scoped lang='less'>
.show-data {
  display: flex;
  flex-direction: column;
  justify-content: space-around;
  .title {
    font-size: 16px;
    align-self: center;
    margin-bottom: 0.625rem;
  }
  .data {
    font-size: 22px;
    font-weight: 700;
    align-self: center;
  }
  .sub-data {
    margin-top: 0.375rem;
    font-size: 12px;
    align-self: center;
  }
}
</style>