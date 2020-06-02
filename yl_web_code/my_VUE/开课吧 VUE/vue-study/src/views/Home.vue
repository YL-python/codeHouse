<template>
  <div class="home">
    <!-- 
      @foo="onFoo"
        一个参数的时候 写法等价
      @foo="onFoo($event) 写法等价
    -->
    <HelloWorld msg="Welcome to Your Vue.js App" ref="hw" @foo="onFoo" />
    <HelloWorld2 msg="this is Hello World 2">
      <!-- 默认插槽用default做参数 -->
      <template v-slot:default>默认插槽</template>
      <!-- 具名插槽用插槽名做参数 -->
      <template v-slot:content>具名插槽</template>
    </HelloWorld2>

    <formTest></formTest>  
  </div>
</template>

<script>
// @ is an alias to /src
import HelloWorld from "@/components/HelloWorld.vue";
import HelloWorld2 from "@/components/HelloWorld2.vue";
import formTest from "../components/form";

export default {
  provide() {
    // 使用返回对象，保证this 的指向
    return {
      data1: "data1",
      homeThis: this.mua
    };
  },
  name: "Home",
  components: {
    HelloWorld,
    HelloWorld2,
    formTest
  },
  data() {
    return {
      mua: "mua"
    };
  },
  methods: {
    onFoo(e, w) {
      console.log(" 子组件 h1标签被点击");
      console.log(e);
      console.log(w);
    }
  },
  created() {
    console.log(this.$refs.hw);
  },
  mounted() {
    this.$refs.hw.foo = "world";

    // 访问第一个子组件
    this.$children[0].foo = "hello world";
  }
};
</script>
