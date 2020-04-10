<template>
  <div id="app">
    <!-- <LessDomo></LessDomo> -->
    <Header></Header>
    <Tab></Tab>
    <router-view></router-view>
  </div>
</template>
<script>
// import LessDomo from './demo/less/LessDemo/index'
import Header from './components/Header'
import Tab from './components/Tab'
export default {
  components: {
    // LessDomo
    Header,
    Tab
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
