<template>
<!-- $parent.$emit('mua') 通过共同的父组件派发一个 mua事件 -->
  <div class="hello" @click="$parent.$emit('mua')">
    <h1 @click="$emit('foo','参数一','参数2')">{{ msg }}</h1>
    {{foo}}
  </div>
</template>

<script>
export default {
  name: "HelloWorld",
  props: {
    msg: String
  },
  data() {
    return {
      foo: "hello"
    };
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
