<template>
  <div id="son1">
    <h4>这里是 Son1 组件</h4>
    name: {{this.$store.state.name}}
    age: {{this.$store.state.age}}
    <br>
    <button @click="son1Change">改名</button>
  </div>
</template>

<script>
export default {
  name: "Son1",
  mounted() {
    console.log('Son1组件this：',this);
  },
  methods: {
    son1Change(){
      // 通过 commit方法触发 mutation
      // 参数一是要触发的方法名，参数二是传递的参数
      this.$store.commit('changeName',{name:123,age:456})
    }
  },
};
</script>

<style>
</style>
