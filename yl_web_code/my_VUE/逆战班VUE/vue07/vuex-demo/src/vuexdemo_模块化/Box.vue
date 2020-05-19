<template>
  <div id="box">
    <h4>这里是 Box 组件</h4>
    <hr />
    <Son1></Son1>
    <hr />
    <Son2></Son2>
  </div>
</template>

<script>
import Son1 from "./Son1";
import Son2 from "./Son2";
export default {
  name: "Box",
  components: {
    Son1,
    Son2
  },
  mounted() {
    console.log(this);
  }
};
</script>

<style>
</style>
