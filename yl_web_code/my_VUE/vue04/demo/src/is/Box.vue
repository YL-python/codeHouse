<template>
  <div>
    <h4>动态组件</h4>
    <button @click='toggle'>toggle</button>
    <!-- <span class='test' :is='state?"son1":"son2"'></span> -->
    <!-- <component class='test' :is='state?"son1":"son2"'></component> -->
    <component class='test' :is='arr[index]'></component>
  </div>
</template>
<script>
/*
动态组件 is 属性 可以指定渲染某一个组件 
使用is属性的标签不会被渲染
为了语义化 一般使用vue提供的component标签
*/ 
import son1 from './son1'
import son2 from './son2'
export default {
  components:{
    son1,
    son2
  },
  data() {
    return {
      state:true,
      arr:['son1','son2'],
      index:0
    }
  },
  methods: {
    toggle(){
      this.state = !this.state
    }
  },
};
</script>