<template>
  <div class="home">
    <div>{{ msg }}</div>
    <div class="left">
      <form action="" v-if="isShow">
        <div class="item">
          菜品名称
          <input type="text" v-model="unit.name" id="" />
        </div>
        <div class="item">
          菜品图片
          <input type="text" v-model="unit.url" id="" />
        </div>
        <div class="item">
          菜品分类
          <input type="text" v-model="unit.type" id="" />
        </div>
        <div class="item">
          菜品价格
          <input type="text" v-model="unit.price" id="" />
        </div>
        <button @click="isShow = false">添加</button>
      </form>
      <div class="info" v-else>
        菜名：{{ unit.name }},图片：{{ unit.url }},分类：{{
          unit.type
        }},价格：{{ unit.price }}

        <br />
        <button @click="add">确定</button>
        <button @click="isShow = true">取消</button>
      </div>
    </div>
    <ul class="right">
      菜单栏
      <li class="list" v-for="(item, index) in lists">
        菜名：{{ item.name }},图片：{{ item.url }},分类：{{
          item.type
        }},价格：{{ item.price }}
      </li>
    </ul>
  </div>
</template>

<script>
export default {
  name: "Home",
  data() {
    return {
      msg: "hello vue",
      unit: {
        name: "",
        url: "",
        type: "",
        price: ""
      },
      isShow: true,
      lists: []
    };
  },
  mounted() {
    this.lists = this.$store.state.lists;
  },
  methods: {
    add() {
      this.lists.push({ ...this.unit });
      this.$store.commit("setList", this.lists);
      this.unit.name = "";
      this.unit.url = "";
      this.unit.type = "";
      this.unit.price = "";
      this.isShow = true;
    }
  }
};
</script>
<style lang="scss" scoped></style>
