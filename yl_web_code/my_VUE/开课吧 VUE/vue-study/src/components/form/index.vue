<template>
  <div>
    <yl-form :model="model" :rules="rules" ref="ylForm">
      <yl-formItem label="用户名" prop='username'>
        <yl-input v-model="model.username" type="text"></yl-input>
      </yl-formItem>
      <yl-formItem label="密码" prop='password'>
        <yl-input v-model="model.password" type="password"></yl-input>
      </yl-formItem>
      <yl-formItem >
        <button @click="onLogin">登陆</button>
      </yl-formItem>
      {{model}}
    </yl-form>
  </div>
</template>
<script>
import ylInput from "./ylInput";
import ylFormItem from "./ylFormItem";
import ylForm from "./ylForm";

export default {
  components: {
    ylInput,
    ylFormItem,
    ylForm
  },
  data() {
    return {
      model: {
        username: "tom",
        password: ""
      },
      rules: {
        username: [{ required: true, message: "用户名必填" }],
        password: [{ required: true, message: "密码必填" }]
      }
    };
  },
  methods: {
    onLogin(){
      this.$refs.ylForm.validate((isValid)=>{
        if(isValid){
          alert("登陆成功")
        }else{
          alert("登陆失败")
        }
      })
    }
  },
};
</script>