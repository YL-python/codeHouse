<template>
  <div id="son1">
    <h4>这里是 Son1 组件</h4>
    name:{{this.$store.state.name}}
    <br>
    mapState:{{name}},{{age}},{{sex}}
    <hr />
    getters:{{this.$store.getters.double}}
    <br>
    mapGetters:{{double}}
    <br>
    <button @click="son1Change">son1 改名</button>
  </div>
</template>

<script>
import { mapState, mapGetters } from "vuex";
export default {
  name: "Son1",
  mounted() {
    console.log("Son1组件this：", this);
  },
  methods: {
    son1Change() {
      // setTimeout(() => {
      //   this.$store.commit("changeName", { name: "son1" });
      // }, 1000);
      this.$store.dispatch('changeNameAction',{ name: "son1" })
    }
  },
  // 通过计算属性绑定state值
  computed: {
    localComputed() {
      /* ... */
    },
    ...mapState(["name", "age", "sex"]),
    ...mapGetters(['double'])

    /*
    ...mapState(["name"])
    
    ...mapState({
      hehe:(state)=>{
        return state.name
      }
    })

    ...mapState({
      hehe:state=>state.name
    })
    */

    /*
    ...mapGetters(['double'])

    ...mapGetters({
      hehe:'double'
    })
    剩下两个的写法和 getters写法一直
    */
  }
};
</script>

<style>
</style>
