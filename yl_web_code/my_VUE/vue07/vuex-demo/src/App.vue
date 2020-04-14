<template>
  <div id="app">
    <h3>根组件</h3>
    <!-- <Box></Box> -->
    <Todo></Todo>
  </div>
</template>

<script>
// import Box from './vuexdemo/Box'
import Todo from './todolist/todo'
export default {
  name: 'App',
  components:{
    // Box
    Todo
  }
}
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>
