<template>
  <el-row :gutter="20">
    <el-col :span="24">
      <el-card class="box-card" v-loading="loading">
        <div style="text-align: center;">
          <span style="font-size: 12px;margin-right: 10px;">{{file.filename}}</span>
          <span style="font-size: 12px;">{{file.filesize}}</span>
        </div>
        <div style="text-align: center;margin-top: 20px;">
          <img :src="file.fileicon" class="image" style />
        </div>
      </el-card>
    </el-col>
  </el-row>
</template>

<script>
export default {
  data() {
    return {
      loading: false,
      components: [{ componentcode: "preview_text", componentname: "预览" }],
      file: {
        id: "",
        filename: "",
        fileicon: "",
        filesize: "",
        filesuffix: "",
        filemd5: "",
      },
    };
  },
  methods: {
    setData(id, filename, fileicon, filesize, filesuffix, filemd5) {
      this.file.id = id;
      this.file.filename = filename;
      this.file.fileicon = fileicon;
      this.file.filesize = filesize;
      this.file.filesuffix = filesuffix;
      this.file.filemd5 = filemd5;
    },
  },
};
</script>

<style scoped>
.image {
  vertical-align: middle;
  width: 468px;
  background-size: cover;
}
</style>