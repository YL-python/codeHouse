<template>
  <div id="son2">
    <h4>这里是 Son2 组件</h4>
    name:{{this.$store.state.name}}
    <button @click="son2Change">son2 改名</button>
  </div>
</template>

<script>
import { mapActions, mapMutations } from "vuex";
export default {
  name: "Son2",
  mounted() {
    console.log("Son2组件this：", this);
  },
  methods: {
    ...mapActions(["changeNameAction"]),
    ...mapMutations(['changeName']),
    son2Change() {
      // setTimeout(() => {
      //   this.$store.commit("changeName", { name: "son2" });
      // }, 1000);
      // 完整写法
      // this.$store.dispatch('changeNameAction',{ name: "son2" })
      // mapActions 辅助函数
      this.changeNameAction({ name: "son2" });
      // mapMutations 辅助函数
      this.changeName({ name: "son2" });
    }
  }
};
</script>

<style>
</style>
