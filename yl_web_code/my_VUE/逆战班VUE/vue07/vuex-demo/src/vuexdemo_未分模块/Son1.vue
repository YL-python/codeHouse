<template>
  <div id="son1">
    <h4>这里是 Son1 组件</h4>
    name:{{name}}
    age:{{age}}
    <button @click="changeName({name:'son1'})">改名字</button>
  </div>
</template>

<script>
import { mapState, mapMutations } from "vuex";
export default {
  name: "Son1",
  mounted() {
    console.log("Son1组件this：", this);
  },
  methods: {
    ...mapMutations(['changeName']),
  },
  computed: {
    ...mapState(['name','age'])
  },
};
</script>

<style>
</style>
