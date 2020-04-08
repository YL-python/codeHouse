<template>
  <div id="app">
    <button @click='back'>回退</button>
    <span @click="jump('/son1')">son1</span>
    <span @click="jump('/son2')">son2</span>
    <span @click="jump('/recommend')">推荐</span>
    <span @click="jump('/dtly')">动态路由</span>
    <button @click='forward'>前进</button>
    <router-view></router-view>
  </div>
</template>

<script>

export default {
  methods: {
    jump(path){
      console.log(this);
      // push 
      // this.$router.push(path)
      // this.$router.push({name:"路由命名"})
      // this.$router.push({path:path})
      // replace 
      // this.$router.replace(path)
      // this.$router.replace({name:"路由命名"})
      this.$router.replace({path:path})
      // go  go(-1)  go(1)
      // back forward

      // push  a->b->c->d  每一次 吧页面加入 页面栈
      // replace 没有页面栈
    },
    back(){
      this.$router.back()
      // this.$router.go(-1)
    },
    forward(){
      this.$router.forward()
      // this.$router.go(1)
    }
  },
};
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
.hehe{
  color:lightgreen;
}
span{
  margin:5px
}
</style>
