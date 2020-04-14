<template>
  <div id="todo-input">
    <input type="text" placeholder="请输入待办事项" v-model="userInput" />
    <button @click="add">add</button>
  </div>
</template>

<script>
import { mapMutations } from "vuex";
export default {
  name: "input",
  data() {
    return {
      userInput: ""
    };
  },
  methods: {
    ...mapMutations(["todolist/addList"]),
    add() {
      this["todolist/addList"]({ msg: this.userInput });
    }
  }
};
</script>

<style>
</style>
