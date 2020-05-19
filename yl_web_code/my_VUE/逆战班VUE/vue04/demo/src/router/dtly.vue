<template>
  <div>
    <h4>路由 动态 组件</h4>
  </div>
</template>
<script>
export default {
  mounted() {
    console.log('params',this.$route.params);
  },
};
</script>