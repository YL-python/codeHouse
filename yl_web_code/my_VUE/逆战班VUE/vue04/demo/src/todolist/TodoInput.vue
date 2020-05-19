<template>
  <div>
    <input v-model="inputValue" type="text" />
    <button @click="inputAdd">add</button>
  </div>
</template>
<script>
export default {
  data() {
    return {
      inputValue: ""
    };
  },
  methods: {
    inputAdd() {
      // 触发自定义事件
      this.$emit("add", this.inputValue);
    }
  }
};
</script>