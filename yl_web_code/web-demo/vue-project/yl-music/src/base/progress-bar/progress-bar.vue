<template>
  <div class="progress-bar" ref="progressBar" @click="progressClick">
    <div class="bar-inner">
      <div class="progress" ref="progress"></div>
      <div class="progress-btn-wrapper" ref="progressBtn"
          @touchstart.prevent="progressTouchStart"
          @touchmove.prevent="progressTouchMove"
          @touchend="progressTouchEnd"
      >
        <div class="progress-btn"></div>
      </div>
    </div>
  </div>
</template>

<script type="text/ecmascript-6">
  // 按钮的宽度
  const progressBtnWidth = 16

  export default {
    props: {
      // 进度条显示的百分比
      percent: {  
        type: Number,
        default: 0
      }
    },
    created() {
      // 对一些touch事件 之间进行数据共享的对象
      this.touch = {}
    },
    methods: {
      // 拖动开始事件
      progressTouchStart(e) {
        // 表示 初始化
        this.touch.initiated = true
        // 记录点击起始的 x 坐标
        this.touch.startX = e.touches[0].pageX
        // 当前按钮在的位置
        this.touch.left = this.$refs.progress.clientWidth
      },
      // 拖动移动事件
      progressTouchMove(e) {
        // 处理之前一定要初始化
        if (!this.touch.initiated) {
          return
        }
        // 移动的 偏移量
        const deltaX = e.touches[0].pageX - this.touch.startX
        // 小于 0 大于最大值
        const offsetWidth = Math.min(this.$refs.progressBar.clientWidth - progressBtnWidth, Math.max(0, this.touch.left + deltaX))
        this._offset(offsetWidth)
      },
      // 拖动结束事件
      progressTouchEnd() {
        this.touch.initiated = false
        this._triggerPercent()
      },
      progressClick(e) {
        const rect = this.$refs.progressBar.getBoundingClientRect()
        const offsetWidth = e.pageX - rect.left
        this._offset(offsetWidth)
        // 这里当我们点击 progressBtn 的时候，e.offsetX 获取不对
        // this._offset(e.offsetX)
        this._triggerPercent()
      },
      // 和父组件通信，拖动完成之后告诉父组件
      _triggerPercent() {
        // 在通信之前获取百分比，点击和拖动事件只是改变样式
        const barWidth = this.$refs.progressBar.clientWidth - progressBtnWidth
        const percent = this.$refs.progress.clientWidth / barWidth
        this.$emit('percentChange', percent)
      },
      // 根据宽度 设置进度条的显示和小球的偏移
      _offset(offsetWidth) {
        this.$refs.progress.style.width = `${offsetWidth}px`
        this.$refs.progressBtn.style["transform"] = `translate3d(${offsetWidth}px,0,0)`
      }
    },
    watch: {
      // 监听百分比的变化，最终修改样式
      percent(newPercent) {
        // 在拖动的时候不监听，拖动的权重大
        if (newPercent >= 0 && !this.touch.initiated) {
          const barWidth = this.$refs.progressBar.clientWidth - progressBtnWidth
          // 百分比 乘 总宽度
          const offsetWidth = newPercent * barWidth
          this._offset(offsetWidth)
        }
      }
    }
  }
</script>

<style scoped lang="stylus" rel="stylesheet/stylus">
  @import "~common/stylus/variable"

  .progress-bar
    height: 30px
    .bar-inner
      position: relative
      top: 13px
      height: 4px
      background: rgba(0, 0, 0, 0.3)
      .progress
        position: absolute
        height: 100%
        background: $color-theme
      .progress-btn-wrapper
        position: absolute
        left: -8px
        top: -13px
        width: 30px
        height: 30px
        .progress-btn
          position: relative
          top: 7px
          left: 7px
          box-sizing: border-box
          width: 16px
          height: 16px
          border: 3px solid $color-text
          border-radius: 50%
          background: $color-theme
</style>