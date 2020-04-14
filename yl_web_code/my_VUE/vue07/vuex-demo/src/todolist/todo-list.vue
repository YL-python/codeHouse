<template>
  <div id="todo-list">
    <ul>
      <li :class="item.finish?'green':'red'" v-for="(item,index) in showList" :key="index">
        {{item.msg}}
        <button @click="del(index)">删除</button>
        <span v-if="item.finish">已完成</span>
        <button v-else @click="finish(index)">完成</button>
      </li>
    </ul>
  </div>
</template>

<script>
import { mapState, mapMutations, mapGetters } from "vuex";
export default {
  name: "list",
  components: {},
  computed: {
    ...mapState({
      list: state => state.todolist.list
    }),
    ...mapGetters({
      showList:"todolist/showList"
    })
  },
  methods: {
    ...mapMutations(["todolist/delList", "todolist/finishList"]),
    del(index) {
      this["todolist/delList"](index);
    },
    finish(index) {
      this["todolist/finishList"](index);
    }
  }
};
</script>
<style>
.green {
  background: rgb(110, 255, 110);
}
.red {
  background: rgb(241, 56, 56);
}
</style>
