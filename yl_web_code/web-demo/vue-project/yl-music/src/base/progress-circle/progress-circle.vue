<template>
  <div class="progress-circle">
    <!-- viewBox 视口的位置，左上角0，0  宽高100，100 -->
    <svg :width="radius" :height="radius" viewBox="0 0 100 100" version="1.1" xmlns="http://www.w3.org/2000/svg">
      <!-- r="50" cx="50" cy="50" 半径大小以及圆形坐标 -->
      <circle class="progress-background" r="50" cx="50" cy="50" fill="transparent"/>
      <circle class="progress-bar" r="50" cx="50" cy="50" fill="transparent" :stroke-dasharray="dashArray"
              :stroke-dashoffset="dashOffset"/>
              <!--
                stroke-dasharray 描边周长，一个圆环就是一整个圆周长  2*PI*R
                stroke-dashoffset 描了多少
              -->
    </svg>
    <slot></slot>
  </div>
</template>

<script type="text/ecmascript-6">
  export default {
    props: {
      // 圆环大小
      radius: {  
        type: Number,
        default: 100
      },
      // 百分比
      percent: {
        type: Number,
        default: 0
      }
    },
    data() {
      return {
        // 50 是半径 ，计算周长
        dashArray: Math.PI * 2 * 50
      }
    },
    computed: {
      dashOffset() {
        return (1 - this.percent) * this.dashArray
      }
    }
  }
</script>

<style scoped lang="stylus" rel="stylesheet/stylus">
  @import "~common/stylus/variable"

  .progress-circle
    position: relative
    circle
      stroke-width: 8px
      transform-origin: center
      &.progress-background
        transform: scale(0.9)
        stroke: $color-theme-d
      &.progress-bar
        transform: scale(0.9) rotate(-90deg)
        stroke: $color-theme
</style>