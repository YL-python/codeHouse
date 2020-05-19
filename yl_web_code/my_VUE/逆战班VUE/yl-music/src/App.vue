<template>
  <div id="app">
    <!-- <LessDomo></LessDomo> -->
    <Header></Header>
    <Tab></Tab>
    <router-view></router-view>
    <!-- 音乐播放器组件 -->
    <Player></Player>
  </div>
</template>
<script>
// import LessDomo from './demo/less/LessDemo/index'
import Header from './components/Header'
import Tab from './components/Tab'
import Player from './components/Player'
export default {
  components: {
    // LessDomo
    Header,
    Tab,
    Player
  }
}
</script>
<style lang="less" scoped>
@import './style/index.less';
#app{
  background: @black2;
  .w(375);
  height: 100vh;
}
</style>
