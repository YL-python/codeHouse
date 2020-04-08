<template>
  <div id="app">
    这里是 app 跟组件
    <banner></banner>
    <hr>
    <box></box>
    <br>
    <!-- 控制地址栏改变
    默认渲染成 a标签，
    to 表示地址栏改变
    tag 控制渲染成啥标签
    active-class 激活状态的类名
    -->
    <router-link to="/son1" tag='span' active-class='hehe'>son1</router-link>
    <router-link to="/son2" tag='span' active-class='hehe'>son2</router-link>
    <!-- <router-link :to="{path:'/recommend'}" tag='span' active-class='hehe'>推荐</router-link> -->
    <router-link :to="{name:'hehe'}" tag='span' active-class='hehe'>推荐</router-link>
    <router-link to="/namerouter" tag='span' active-class='hehe'>命名视图</router-link>
    <hr>
    <!-- 占位作用，根据地址栏渲染不同组件 -->
    <!-- 命名视图，给视图取名字 -->
    <router-view></router-view>
    <router-view name='a'></router-view>
    <router-view name='b'></router-view>
  </div>
</template>

<script>
// 引入一个组件 .vue后缀名可以不写
import banner from "./Banner"
// import box from './todolist/Box'
import box from './is/Box'
export default {
  name: "App",
  components: {
    banner: banner, // 注册组件
    box
  }
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
</style>
