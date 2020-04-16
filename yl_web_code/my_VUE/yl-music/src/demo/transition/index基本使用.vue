<template>
  <div class="transition">
    <h3>动画案例</h3>
    <button @click="change">show</button>
    <transition name="hehe">
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
.test {
  width: 100px;
  height: 100px;
  background: red;
}
/*
transition：只能有一个元素，多个元素用transition-group，且每一个元素需要有key值
hehe-enter：hehe组件进入前的状态
hehe-enter-to：hehe组件进入后的状态
hehe-enter-active：hehe组件进入的过程
hehe-leave：hehe组件离开前的状态
hehe-leave-to：hehe组件离开后的状态
hehe-leave-active：hehe组件离开的过程
*/
.hehe-enter {
  opacity: 0;
}
.hehe-enter-to {
  opacity: 1;
}
.hehe-enter-active {
  transition: all 5s;
}
.hehe-leave {
  opacity: 1;
}
.hehe-leave-to {
  opacity: 0;
}
.hehe-leave-active {
  transition: all 10s;
}
</style>
