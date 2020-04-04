### vue总结

#### vue01
+ 数据绑定

+ v-if   v-show

+ v-on
  v-on:click  ===  @click 
  
+ 响应式的数据

+ v-bind
  v-bind:src === :src
  
+ v-for
  ```html
  <li v-for ='循环数据的每一项 in/of 要循环的数据'></li>
  <li v-for ='(循环数据的每一项,每一项的下标)in/of 要循环的数据'></li>
  <li v-for="(对象value,对象里的key,下标) in 要循环的对象">{{key}}:{{value}}-{{index}}</li>
  ```

+ v-model
  双向数据绑定，表单绑定
  [官网 v-model介绍](https://cn.vuejs.org/v2/guide/forms.html)

+ 自定义指令
  全局，局部
  [官网自定义指令](https://cn.vuejs.org/v2/guide/custom-directive.html#ad)

