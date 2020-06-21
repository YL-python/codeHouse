<template>
  <div class="hello">
    <h3>vue 的更新队列</h3>
    {{name}}
    <hehe></hehe>
  </div>
</template>

<script>
export default {
  data() {
    return {
      name: "韩梅梅"
    };
  },
  // created() {
  //   this.name = 1;
  // },
  mounted() {
    this.name = 1;
    this.name = 2;
    this.name = 3;
    // 修改了 3 次 name 但是执行力一次update生命周期
  },
  // updated的之后在数据挂载之后才执行，created声明周期中不会触发这个方法
  updated() {
    // vue 会将一个事件循环中的所有数据操作合并，然后在执行更新
    // 1 2 3 4 5 4 3 2 1  这样的只会更新一次
    console.log("数据更新了");
  }
};
</script>

<style scoped>
</style>
