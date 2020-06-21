<template>
  <div>
    <h3>vue 组件的 v-model 使用</h3>
    <son v-model="name"></son>
  </div>
</template>
<script>
import son from "./son";
export default {
  data() {
    return {
      name: "韩梅梅"
    };
  },
  methods: {},
  components: {
    son
  }
};
</script>
<style scoped>
</style>