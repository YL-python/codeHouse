<template>
  <div style="height: 100%;">
    <!--==================================功能栏==================================-->
    <el-row style="margin-top:-10px;margin-left: -20px;margin-right: -20px;">
      <el-col :span="18" class="nav">
        <!-- 上传文件按钮 -->
        <el-button
          style="margin-left: 20px;"
          type="text"
          icon="el-icon-upload"
          :disabled="checkedcount!=0"
          @click="uploadUI"
        >上传文件</el-button>

        <el-button
          type="text"
          icon="el-icon-bottom"
          :disabled="checkedcount==0"
          @click="downloadBatch"
        >下载</el-button>

        <el-button
          type="text"
          icon="el-icon-delete"
          :disabled="checkedcount==0"
          @click="deleteBatch"
        >删除</el-button>
      </el-col>
      <el-col :span="4" class="nav" style="text-align: center;"></el-col>
      <el-col :span="2" class="nav">
        <!-- <el-button type="text" icon="el-icon-tickets" @click="toggle()">列表模式</el-button> -->
        <el-button type="text" icon="el-icon-refresh" @click="refreshs">刷新</el-button>
      </el-col>
    </el-row>
    <!--==================================链接导航==================================-->
    <el-row>
      <el-col :span="24">
        <el-button
          type="text"
          size="mini"
          icon="el-icon-caret-right"
          v-for="(item,index) in items"
          :key="index"
          @click="itemClickPrev(item.id)"
        >{{item.name}}</el-button>
      </el-col>
    </el-row>
    <!--=================================列表========================================-->
    <el-row style="height: 85%;overflow: auto;">
      <el-col :span="24">
        <el-table
          v-loading="loading"
          :data="table.data"
          size="small"
          @selection-change="selectionChange"
        >
          <el-table-column type="selection" width="55"></el-table-column>
          <el-table-column prop="filename" label="文件名">
            <template slot-scope="scope">
              <img
                :src="scope.row.icon"
                style="vertical-align: middle;margin-right: 10px; width:32px;height:32px;"
              />
              <span class="link" @click="itemClickEnter(scope.row.rowindex)">{{scope.row.filename}}</span>
            </template>
          </el-table-column>
          <el-table-column prop="filesize" label="大小" width="120">
            <template slot-scope="scope">
              <span>{{scope.row.filesize==0?"-":scope.row.filesizename}}</span>
            </template>
          </el-table-column>
          <el-table-column prop="createtime" label="修改日期" width="150"></el-table-column>
        </el-table>
      </el-col>
    </el-row>
    <!--===============================分页======================================-->
    <el-row>
      <el-col :span="24" style="text-align: center;">
        <el-pagination
          @current-change="currentchange"
          @prev-click="prevClick"
          @next-click="nextClick"
          :current-page="table.currentPage"
          :page-size="table.pagesize"
          :total="table.total"
          layout="total, prev, pager, next, jumper"
        ></el-pagination>
      </el-col>
    </el-row>
    <!--===================================弹出框====================================-->
    <el-dialog
      :title="dialog.title"
      :visible.sync="dialog.visible"
      :width="dialog.width"
      :show-close="true"
      @close="cancel"
      :modal="true"
      :close-on-click-modal="false"
      :close-on-press-escape="false"
    >
      <open ref="form" v-if="dialog.type=='open'"></open>
      <div slot="footer" class="dialog-footer" v-if="dialog.type=='copy'||dialog.type=='move'">
        <el-button @click="cancel()">取 消</el-button>
        <el-button type="primary" @click="confirm()">确 定</el-button>
      </div>
    </el-dialog>

    <!--上传弹出框-->
    <el-dialog
      :title="drawer.title"
      :visible.sync="drawer.visible"
      :width="drawer.width"
      :show-close="true"
      @close="uploaderClose"
      :modal="true"
      :close-on-click-modal="false"
      :close-on-press-escape="false"
    >
      <el-upload
        action="http://39.103.133.166:22100/filesystem/upload"
        list-type="picture"
        :on-preview="handlePictureCardPreview"
        :on-success="handleSuccess"
        ref="elUpload"
        multiple
      >
        <i class="el-icon-plus">点击添加</i>
      </el-upload>
      <el-dialog :visible.sync="dialogVisible">
        <img width="100%" :src="dialogImageUrl" alt />
      </el-dialog>
    </el-dialog>
  </div>
</template>
<script>
import open from "../../components/dialog_open.vue";
export default {
  data() {
    return {
      loading: false,
      checkedcount: 0,
      checkeditems: [],
      items: [{ id: "0", name: "全部文件" }],
      search: {
        pid: 0,
        orderfield: "createtime",
        ordertype: "descending",
      },
      table: {
        currentPage: 1,
        pagesize: 10,
        total: 1110,
        data: [
          {
            id: "1",
            filename: "你好",
            filesize: 1234,
            filesizename: "1234Kb",
            createtime: "2020-1-1",
            icon: "../../assets/folder.png",
          },
        ],
      },
      dialog: {
        width: "",
        type: "",
        visible: false,
        title: "",
      },
      drawer: {
        title: "",
        width: "800px",
        type: "",
        visible: false,
      },
      dialogImageUrl: "",
      dialogVisible: false,
    };
  },
  created() {
    let userid = sessionStorage.getItem("userId");
    if (userid) {
      //查询 文件
      this.searchs();
    } else {
      this.alertMsg(1, "非法登陆请求，请重新登陆");
      this.$router.push("/");
    }
  },
  methods: {
    // 刷新
    refreshs() {
      this.$confirm("是否刷新列表?", "提示", {
        confirmButtonText: "确定",
        cancelButtonText: "取消",
        type: "warning",
      }).then(() => {
        this.searchs();
      });
    },
    // 搜索
    searchs() {
      this.table.currentPage = 1;
      this.findList();
    },
    findList() {
      this.loading = true;
      this.$axios
        .get("http://39.103.133.166:22100/filesystem/page", {
          params: {
            currentPage: this.table.currentPage,
            userId: sessionStorage.getItem("userId"),
          },
        })
        .then((response) => {
          if (response.code === 200) {
            let data = response.data;
            let rows = data.records;
            if (rows != null && rows.length != 0) {
              for (let i = 0; i < rows.length; i++) {
                let d = rows[i];
                if (d.size) {
                  d.filesizename = d.size;
                } else {
                  d.filesizename = "未知";
                }
                d.createtime = d.created;
                if (d.fileName === "1") {
                  d.rowindex = i;
                  d.filename = d.fileName;
                  d.icon = require("@/assets/folder.png");
                  d.fileicon = "http://39.103.133.166/" + d.path;
                } else {
                  d.rowindex = i;
                  d.filename = d.fileName;
                  d.icon = "http://39.103.133.166/" + d.path;
                  d.fileicon = "http://39.103.133.166/" + d.path;
                }
              }
            }
            this.table.data = rows;
            this.table.total = data.total;
          } else {
            this.alertMsg("1", "查找失败");
          }
          this.loading = false;
        });
    },
    // 点击某一个页码
    currentchange(currentPage) {
      this.table.currentPage = currentPage;
      this.findList();
    },
    // 点击 上一页
    prevClick() {
      this.table.currentPage = this.table.currentPage - 1;
      this.findList();
    },
    // 点击 下一页
    nextClick() {
      this.table.currentPage = this.table.currentPage + 1;
      this.findList();
    },
    // 切换到卡片模式
    toggle() {
      this.$router.push("/index/fileall/card");
    },
    // 导航栏点击事件
    itemClickPrev(id) {
      //条目
      let index = this.items.findIndex((item) => {
        if (item.id == id) {
          return true;
        }
      });

      let newitems = new Array();
      this.items.some((item, i) => {
        if (i <= index) {
          newitems.push(item);
        }
      });
      this.items = [];
      this.items = newitems;

      //查询
      this.search.pid = id;
      this.searchs();
    },
    //勾选 checkbox
    selectionChange(val) {
      // console.log('val',val);
      this.checkedcount = val.length;
      this.checkeditems = [];
      for (let i = 0; i < val.length; i++) {
        this.checkeditems.push({
          id: val[i].id,
          name: val[i].filename,
          path: val[i].path,
        });
      }
    },
    // 文件列表 的 文件名被点击
    itemClickEnter(rowindex) {
      let row = this.table.data[rowindex];
      if (row == null) {
        this.alertMsg(1, "您点击的记录不存在");
        return;
      }
      this.dialog.width = "550px";
      this.dialog.title = "文件预览";
      this.dialog.visible = true;
      this.dialog.type = "open";
      setTimeout(() => {
        this.$refs.form.setData(
          row.id,
          row.filename,
          row.fileicon,
          row.filesizename,
          row.filesuffix,
          row.filemd5
        );
      }, 0);
    },
    // 上传文件
    uploadUI() {
      this.drawer.type = "uploader";
      this.drawer.visible = true;
      this.drawer.title = "上传文件";
    },
    // 上传成功图片点击钩子
    handlePictureCardPreview(file) {
      this.dialogImageUrl = file.path;
      this.dialogVisible = true;
    },
    // 上传成功钩子
    handleSuccess(response, file) {
      response.userId = sessionStorage.getItem("userId");
      file.path = "http://39.103.133.166/" + response.path;
      this.$axios
        .post("http://39.103.133.166:22100/filesystem/save", response)
        .then((res) => {
          this.alertMsg(0, res.data.fileName + "上传成功");
        });
    },
    deleteBatch() {
      console.log("this.checkeditems", this.checkeditems);
      this.$confirm("此操作将删除您勾选的记录, 是否继续?", "提示", {
        confirmButtonText: "确定",
        cancelButtonText: "取消",
        type: "warning",
      }).then(() => {
        this.loading = true;
        let ids = [];
        for (let i = 0; i < this.checkeditems.length; i++) {
          ids.push(this.checkeditems[i].id);
        }
        this.$axios
          .post("http://39.103.133.166:22100/filesystem/delete", ids)
          .then((response) => {
            console.log(response);
            let code = 1;
            if (response.code == 200) {
              code = 0;
              this.searchs();
            }
            this.alertMsg(code, response.msg);
            this.loading = false;
          });
      });
    },
    downloadBatch() {
      var len = this.checkeditems.length;
      if (len == 0) {
        this.alertMsg(1, "请选择记录");
        return;
      }

      this.$confirm(
        "是否下载" + this.checkeditems[0].name + "等" + len + "个文件",
        "提示",
        {
          confirmButtonText: "确定",
          cancelButtonText: "取消",
          type: "warning",
        }
      ).then(() => {
        for (let i = 0; i < this.checkeditems.length; i++) {
          // let url =
          //   "http://39.103.133.166:22100/filesystem/download?path=" +
          //   this.checkeditems[i].path;
          let url =
            "http://qiu.ngrok2.xiaomiqiu.cn/filesystem/download?path=" +
            this.checkeditems[i].path;
          window.open(url, "_self");
        }
      });
    },
    cancel() {
      this.dialog.visible = false;
      this.dialog.type = "";
    },
    uploaderClose() {
      this.drawer.type = "";
      this.drawer.visible = false;
      this.$refs.elUpload.clearFiles();
      this.searchs();
    },
  },
  components: {
    open,
  },
};
</script>
<style scoped>
.link:hover {
  color: blue;
  cursor: pointer;
}

.nav {
  background: #f2f6fc;
  height: 60px;
  line-height: 40px;
  border-bottom: 1px solid #e4e7ed;
  margin-top: 0;
  display: flex;
  flex-wrap: wrap;
  justify-content: left;
  align-items: center;
}
</style>