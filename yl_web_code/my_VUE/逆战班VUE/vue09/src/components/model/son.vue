<template>
  <div>
    <h3>这里是子组件</h3>
    values:{{value}}
    <button @click="changeName">改名</button>

    <input type="text" :value="value" @input="$emit('input',$event.target.value)" />
  </div>
</template>
<script>
export default {
  props: ["value"],
  methods: {
    changeName() {
      // 触发自定义事件
      this.$emit("input", "李雷雷");
    }
  }
};
</script>
<style scoped>
</style>