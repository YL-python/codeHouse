<template>
  <div id="app">
    <demo />
    <hehe></hehe>
    <hr />
    <fa></fa>
    <hr />
    <event></event>
  </div>
</template>

<script>
import demo from "./components/demo.vue";
import fa from "./components/model/fa";
import event from "./components/event/demo";

export default {
  name: "App",
  components: {
    demo,
    fa,
    event
  }
};
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
