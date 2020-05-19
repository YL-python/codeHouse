<template>
  <div id="todo">
    <h4>这里是 todo 组件</h4>
    <todoInput></todoInput>
    <todo-list></todo-list>
    <todo-tab></todo-tab>
  </div>
</template>

<script>
import TodoInput from "./todo-input";
import TodoList from "./todo-list";
import TodoTab from "./todo-tab";
export default {
  name: "todo",
  components: {
    TodoInput,
    TodoTab,
    TodoList
  },
  mounted() {
    console.log("todo:", this);
  }
};
</script>

<style>
</style>
