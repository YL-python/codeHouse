<template>
  <div id="son2">
    <h4>这里是 Son2 组件</h4>
    name: {{this.$store.state.name}}
    age: {{this.$store.state.age}}
    <br>
    <button @click="son2Change">改年龄</button>
  </div>
</template>

<script>
export default {
  name: 'Son2',
  mounted() {
    console.log('Son2组件this：',this);
  },
  methods: {
    son2Change(){
      // this.$store.commit('changeAge',{name:123,age:456})
      // 用来触发 action函数
      this.$store.dispatch('changeAge',{name:123,age:456})
    }
  },
}
</script>

<style>
</style>
