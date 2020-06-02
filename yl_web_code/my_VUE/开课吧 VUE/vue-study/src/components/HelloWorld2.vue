<template>
  <div class="hello">
    <h1>{{ msg }}</h1>
    <h2>多代传值 -- {{data1}}</h2>
    {{homeThis}}
    <slot></slot>
    <slot name='content'></slot>
  </div>
</template>

<script>
export default {
  inject: ["data1", "homeThis"],
  props: {
    msg: String
  },
  created() {
    // 通过沟通的父组件 监听这个 mua 事件
    this.$parent.$on("mua", () => {
      console.log("helloWorld2 mua");
    });
  }
};
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
h3 {
  margin: 40px 0 0;
}
ul {
  list-style-type: none;
  padding: 0;
}
li {
  display: inline-block;
  margin: 0 10px;
}
a {
  color: #42b983;
}
</style>
