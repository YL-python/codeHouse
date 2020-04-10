<template>
  <div>
    <h4>路由 son1 组件</h4>
  </div>
</template>
<script>
export default {
  mounted() {
    console.log('这里是组件一',this.$route);
    
  },
};
</script>