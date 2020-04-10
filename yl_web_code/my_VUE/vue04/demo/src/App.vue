<template>
  <div id="app">
    <router-link to="/recommend" active-class="hehe" tag="span">推荐</router-link>
    <router-link to="/singer" active-class="hehe" tag="span">歌手</router-link>
    <router-link to="/my" active-class="hehe" tag="span">我的</router-link>
    <!-- 只能显示一级路由 -->
    <router-view></router-view>
  </div>
</template>

<script>
export default {
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
