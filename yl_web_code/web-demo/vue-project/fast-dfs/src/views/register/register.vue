<template>
  <div class="register-container">
    <el-card class="register">
      <div slot="header" class="header">
        <img class="header-img" src="../../assets/logo.png" />
        <span class="header-title">个人分布式文件管理系统</span>
      </div>
      <el-form
        ref="registerForm"
        :model="form"
        label-width="0px"
        :rules="rules"
        v-loading="loading"
      >
        <el-form-item prop="username">
          <el-input v-model="form.username" placeholder="自定义用户名"></el-input>
        </el-form-item>
        <el-form-item prop="telephone">
          <el-input v-model="form.telephone" placeholder="请输入手机号"></el-input>
        </el-form-item>
        <el-form-item prop="password">
          <el-input v-model="form.password" placeholder="请输入密码" show-password></el-input>
        </el-form-item>
        <el-form-item>
          <el-button style="width:100%;" type="warning" @click="onSubmit('registerForm')">注册</el-button>
        </el-form-item>
      </el-form>
      <div class="footer">
        <el-link type="primary" @click="$router.go(-1)">返回</el-link>
      </div>
    </el-card>
  </div>
</template><script>
export default {
  data() {
    return {
      loading: false,
      form: {
        username: "",
        password: "",
        telephone: ""
      },
      rules: {
        username: [
          { required: true, message: "请输入账号", trigger: "blur" },
          { min: 3, max: 18, message: "长度在 3 到 18 个字符", trigger: "blur" }
        ],
        password: [
          { required: true, message: "请输入密码", trigger: "blur" },
          { min: 6, max: 18, message: "长度在 6 到 18 个字符", trigger: "blur" }
        ],
        telephone: [
          { required: true, message: "请输入电话号码", trigger: "blur" },
          { min: 11, max: 11, message: "长度有误", trigger: "blur" }
        ]
      }
    };
  },
  methods: {
    onSubmit(formName) {
      this.$refs[formName].validate(valid => {
        if (valid) {
          // 登陆成功  存储信息到本地并且 跳转到首页
          alert("submit!");
        } else {
          console.log("error submit!!");
          return false;
        }
      });
    }
  }
};
</script>
<style scoped lang='less'>
.register-container {
  background-color: #fff;
  padding-top: 10%;
  height: 100%;
}
.register {
  width: 500px;
  height: 500px;
  margin: 0 auto;
  padding: 64px 75px 48px;
  box-sizing: border-box;
  -webkit-box-shadow: 0px 20px 80px 0px rgba(0, 0, 0, 0.3);

  .header {
    position: relative;
    text-align: center;
    .header-img {
      display: inline-block;
      width: 32px;
      height: 32px;
      position: absolute;
      top: 0;
      left: 0;
    }
    .header-title {
      line-height: 32px;
      height: 32px;
    }
  }
  .footer {
    text-align: right;
    font-size: 12px;
  }
}
</style>