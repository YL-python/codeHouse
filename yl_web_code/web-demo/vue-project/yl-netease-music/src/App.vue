<template>
  <div id="app">
    <div class="aside">
      <div class="logo">
        <a href>
          <img src="./assets/logo.png" width="80px" height="80px" alt />
        </a>
        <h1 class="describe">仿网易云的音乐网站</h1>
      </div>
      <div class="nav">
        <div class="nav-item title">
          <i class="iconfont icon-liebiao"></i>
          功能列表
        </div>
        <router-link to="/recommend" tag="div" class="nav-item" active-class="active">
          <i class="iconfont icon-tuijian"></i>
          推荐
        </router-link>
        <router-link to="/toplist" tag="div" class="nav-item" active-class="active">
          <i class="iconfont icon-paihang"></i>
          排行
        </router-link>
        <router-link to="/artlist" tag="div" class="nav-item" active-class="active">
          <i class="iconfont icon-ren"></i>
          歌手
        </router-link>
        <router-link to="/search" tag="div" class="nav-item" active-class="active">
          <i class="iconfont icon-sousuo"></i>
          搜索
        </router-link>
        <router-link to="/mylike" tag="div" class="nav-item" active-class="active">
          <i class="iconfont icon-xihuan"></i>
          我喜欢
        </router-link>
        <router-link to="/playhistory" tag="div" class="nav-item" active-class="active">
          <i class="iconfont icon-lishi"></i>
          播放历史
        </router-link>
      </div>
    </div>

    <div class="main">
      <div class="content">
        <keep-alive>
          <router-view></router-view>
        </keep-alive>
      </div>
    </div>
  </div>
</template>

<style lang="less" scoped >
@import url("//at.alicdn.com/t/font_1833482_z4746juwfb.css");
#app {
  color: #2c3e50;
  display: flex;
  justify-content: space-between;
  height: 100%;
}
.aside {
  flex: 0 0 200px;
  height: 100vh;
  background: #f5f5f7;
  .logo {
    padding-top: 30px;
    padding-bottom: 50px;
    .describe {
      padding-top: 10px;
      font-size: 14px;
    }
  }
  .nav {
    display: flex;
    flex-direction: column;
    .nav-item {
      width: 90%;
      margin: 0 auto;
      padding: 7px 0;
      cursor: pointer;
      display: flex;
      flex-direction: column;
    }
    .active {
      background-color: #e6e7ea;
      border-left: 5px solid #25c37a;
    }
    .title {
      background-color: #e3e3e5;
      margin: 5px auto;
      width: 100%;
    }
  }
}

.main {
  flex: 1;
  background: #fff;
  min-width: 1000px;
  .content {
    width: 90%;
    border: 1px red solid;
    margin: 0 auto;
  }
}
</style>
