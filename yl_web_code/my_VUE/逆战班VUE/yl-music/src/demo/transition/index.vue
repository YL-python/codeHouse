<template>
  <div class="transition">
    <h3>动画案例</h3>
    <button @click="change">show</button>
    <transition
      enter-active-class="animated tada"
      leave-active-class="animated bounceOutRight">
      <div class="test" v-if="show"></div>
    </transition>
  </div>
</template>
<script>
export default {
  data () {
    return {
      show: true
    }
  },
  methods: {
    change () {
      this.show = !this.show
    }
  }
}
</script>

<style>
@import '~animate.css/animate.css';
/*
这里是局部引入
也可以在main.js里面全局引入
  import 'animate.css/animate.css'  // 全局引入写法
使用：添加类名  XXX是插件的动画类名
  enter-active-class="animated XXX"
  leave-active-class="animated XXX"
*/
.test {
  width: 100px;
  height: 100px;
  background: red;
}
</style>
