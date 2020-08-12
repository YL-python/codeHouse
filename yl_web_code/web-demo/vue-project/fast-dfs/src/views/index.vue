<template>
  <div>
    <el-container>
      <el-header class="header">
        <el-row>
          <el-col :span="9" class="headercol left">
            <el-row>
              <el-col :span="4">
                <img src="../assets/logo.png" style="vertical-align: middle;" />
              </el-col>
              <el-col :span="20">
                <div class="text-center">fast-dfs 分布式文件管理系统</div>
              </el-col>
            </el-row>
          </el-col>
          <el-col :span="12" class="headercol center">
            <!-- 搜索框 -->
            <!-- <el-input placeholder="搜索您的文件" style="width: 250px;" v-model="keyword" size="small">
              <el-button slot="append" icon="el-icon-search" @click="gotoSearchs"></el-button>
            </el-input>-->
          </el-col>
          <el-col :span="3" class="headercol right">
            <el-popover width="160" v-model="visible">
              <p style="line-height: 30px;text-align: center;">是否退出系统?</p>
              <div style="text-align: center; margin-top: 10px;">
                <el-button type="text" size="mini" @click="visible = false">取消</el-button>
                <el-button type="primary" size="mini" @click="logout">确定</el-button>
              </div>
              <el-button icon="el-icon-switch-button" size="small" slot="reference">{{nickname}}</el-button>
            </el-popover>
          </el-col>
        </el-row>
      </el-header>
      <el-main style="overflow:hidden;height: 100%;">
        <router-view></router-view>
      </el-main>
    </el-container>
  </div>
</template>
<script>
export default {
  data() {
    return {
      keyword: "",
      visible: false,
      // nickname: sessionStorage.getItem("username"),
      nickname: "用户名",
    };
  },
  created() {
    let name = sessionStorage.getItem("username");
    if (name) {
      this.nickname = name;
    } else {
      this.alertMsg(1, "非法登陆请求，请重新登陆");
      this.$router.push("/");
    }
  },
  methods: {
    gotoSearchs() {
      this.$router.push({
        path: "/main/search/index",
        query: {
          keyword: this.keyword,
        },
      });
    },
    logout() {
      this.removeSession();
      this.$router.push("/");
    },
  },
};
</script>
<style scoped >
.header {
  background: white;
  /*box-shadow: 0 6px 0 rgba(0,0,0,.05);
		z-index: 11111;*/
  border-bottom: 1px solid #f4f4f4;
  box-shadow: 0px 3px 3px rgba(0, 0, 0, 0.05);
  z-index: 1111;
}
.headercol {
  height: 60;
  /*line-height: 60px;*/
  box-sizing: border-box;
  margin-top: 15px;
}
.headercol img {
  display: block;
  height: 32px;
  width: 32px;
}

.right {
  text-align: right;
}
.left {
  text-align: left;
}
.center {
  text-align: center;
}

/*=======================================================*/
.item {
  height: 40px;
  line-height: 40px;
}

/*=======================================================*/
.capacity {
  padding-left: 20px;
  padding-right: 20px;
  box-sizing: border-box;
  position: absolute;
  width: 100%;
  bottom: 50px;
}

/*=======================================================*/
.ullist {
}
.ullist li {
  list-style-type: none;
  padding: 10px;
  margin-bottom: 10px;
  font-size: 13px;
  box-shadow: 0 2px 4px rgba(0, 0, 0, 0.12), 0 0 6px rgba(0, 0, 0, 0.04);
}
.text-center {
  line-height: 32px;
}
</style>