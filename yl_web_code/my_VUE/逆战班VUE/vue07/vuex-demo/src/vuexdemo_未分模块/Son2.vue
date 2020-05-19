<template>
  <div id="son2">
    <h4>这里是 Son2 组件</h4>
    name:{{name}}
    age:{{age}}
    <button @click="changeAge({age:1234})">改年龄</button>
  </div>
</template>

<script>
import { mapState, mapMutations } from "vuex";
export default {
  name: "Son2",
  mounted() {
    console.log("Son2组件this：", this);
  },
  methods: {
    ...mapMutations(['changeAge']),
  },
  computed: {
    ...mapState(['name','age'])
  },
};
</script>

<style>
</style>
