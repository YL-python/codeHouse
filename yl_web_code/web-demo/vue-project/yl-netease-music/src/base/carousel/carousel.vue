<template>
  <div class="carousel hight500">
    <div class="carousel-item" v-for="(item,index) in images" :key="index">
      <img :src="item" alt />
    </div>
  </div>
</template>
<script>
export default {
  props: {
    images: {
      type: Array
    }
  }
};
</script>
<style scoped>
.hight500 {
  height: 500px;
}
</style>