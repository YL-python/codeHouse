<template>
  <div>
    <ul class="left">
      左侧是下单
      <li class="list" v-for="(item, index) in lists">
        菜名：{{ item.name }},图片：{{ item.url }},分类：{{
          item.type
        }},价格：{{ item.price }}
        <button @click="minus(item, index)">-</button>
        <span>{{ typeof item.num === "undefined" ? 0 : item.num }}</span>
        <button @click="add(item, index)">+</button>
      </li>
    </ul>
    <div class="right">
      计算部分
      <ul>
        <li class="list" v-for="(item, index) in orders">
          菜名：{{ item.name }},数量：{{ item.num }},价格{{
            item.price * item.num
          }}
        </li>
      </ul>
      <p v-show="total">总价：{{ total }}</p>
    </div>
  </div>
</template>
<script>
import _ from "lodash";
export default {
  data() {
    return {
      lists: this.$store.state.lists
    };
  },
  methods: {
    minus(item, index) {
      if (typeof item.num === "undefined") {
        item.num = 0;
      }
      item.num--;
      if (item.num < 0) {
        item.num = 0;
      }
      this.$set(this.lists, index, item);
    },
    add(item, index) {
      if (typeof item.num === "undefined") {
        item.num = 0;
      }
      item.num++;
      if (item.num > 100) {
        item.num = 100;
      }
      this.$set(this.lists, index, item);
    }
  },
  computed: {
    orders() {
      return this.lists.filter(item => {
        return item.num !== "undefined" && item.num > 0;
      });
    },
    total() {
      let sum = 0;
      this.orders.forEach(item => {
        sum += item.num * item.price;
      });
      return sum;
    }
  }
};
</script>
<style scoped lang="scss"></style>
