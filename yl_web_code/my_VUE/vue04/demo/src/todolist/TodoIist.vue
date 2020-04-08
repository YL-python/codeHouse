<template>
  <div>
    <ul>
      <li v-for="(item,index) in list" :key="index" :class='item.state?"green":"red"'>
        {{item.msg}}
        <button @click="listDel(index)">del</button>
        <span v-show="item.state">已完成</span>
        <button v-show='!item.state' @click="listFinish(index)">未完成</button>
      </li>
    </ul>
  </div>
</template>
<script>
export default {
  props: { list: { type: Array, default: [] } },
  methods: {
    listDel(index){
      this.$emit('del',index)
    },
    listFinish(index){
      this.$emit('update',index)
      // this.list[index].state = true
    }
  }
};
</script>
<style>
  .red{
    background: red;
  }
  .green{
    background: green;
  }
</style>