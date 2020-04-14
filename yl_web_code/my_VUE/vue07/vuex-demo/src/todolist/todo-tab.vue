<template>
  <div id="todo-tab">
    <span @click="change(0)">全部</span>
    <span @click="change(2)">未完成</span>
    <span @click="change(1)">已完成</span>
  </div>
</template>

<script>
import { mapMutations } from 'vuex';
export default {
  name: "tab",
  methods: {
    ...mapMutations(['todolist/changeAll']),
    change(code){
      this['todolist/changeAll'](code)
    }
  },
};
</script>

<style>
</style>
