<template>
  <div>
    <!-- 自定义 input组件要实现 v-model 需要 自己实现 value绑定个input事件监听 -->
    <!-- $attrs 会存储 props和class和style属性 以外 的所有属性 -->
    <input :value="value" @input="opInput" v-bind="$attrs">
  </div>
</template>
<script>
export default {
  // 顶层容器不继承属性
  inheritAttrs:false,
  props:{
    value:{
      type: String,
      default: ''
    }
  },
  methods: {
    opInput(e){
      this.$emit('input',e.target.value)
      // 输入的时候让父组件进行校验
      this.$parent.$emit('validate')
    }
  },
}
</script>
<style scoped>
  
</style>