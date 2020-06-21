<template>
  <div>
    <h3>事件修饰符</h3>
    <div class="test1" @click.self="clickTest('爷爷')">
      <div class="test2" @click="clickTest('爸爸')">
        <div class="test3" @click.stop="clickTest('儿子')"></div>
      </div>
    </div>
  </div>
</template>
<script>
export default {
  methods: {
    clickTest(msg) {
      console.log(msg);
    }
  }
};
</script>
<style scoped>
.test1 {
  width: 300px;
  height: 300px;
  background-color: green;
}
.test2 {
  width: 200px;
  height: 200px;
  background-color: yellow;
}
.test3 {
  width: 100px;
  height: 100px;
  background-color: red;
}
</style>