<template>
  <div>
    <label v-if="label">{{label}}</label>
    <slot></slot>
    <p v-if="errorMessage">{{errorMessage}}</p>
  </div>
</template>
<script>
import Schema from "async-validator";
export default {
  inject: ["form"],
  props: {
    label: {
      type: String,
      default: ""
    },
    prop: String
  },
  data() {
    return {
      errorMessage: ""
    };
  },
  mounted() {
    // 监听校验事件
    this.$on("validate", () => {
      this.validate();
    });
  },
  methods: {
    validate() {
      // 校验规则
      const rule = this.form.rules[this.prop];
      // 校验数据
      const value = this.form.model[this.prop];

      // 执行校验
      const desc = {
        [this.prop]: rule
      };
      const schema = new Schema(desc);
      // 返回是promise对象
      return schema.validate({ [this.prop]: value }, errors => {
        if(errors){
          console.log(errors);
          this.errorMessage = errors[0].message
          console.log(this.errorMessage);
        }else{
          this.errorMessage = ''
        }
      });
    }
  }
};
</script>
<style scoped>
</style>