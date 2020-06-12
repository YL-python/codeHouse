<template>
  <div class="goods">
    <!-- 左侧导航列表 -->
    <div class="menu-wrapper" ref="mw">
      <ul>
        <li
          v-for="(good,index) in goods"
          :key="index"
          class="menu-item"
          :class="{'current': currentIndex===index}"
          @click="selectMnue(index,$event)"
        >
          <span class="text border-1px">
            <icon :iconType="good.type" iconNum="3"></icon>
            {{good.name}}
          </span>
        </li>
      </ul>
    </div>
    <!-- 右侧食品列表 -->
    <div class="foods-wrapper" ref="fw">
      <ul>
        <li v-for="(good,gindex) in goods" :key="gindex" class="foods-list">
          <h1 class="title">{{good.name}}</h1>
          <ul>
            <li v-for="(food,findex) in good.foods" :key="findex" class="border-1px foods-item">
              <div class="icon">
                <img :src="food.icon" alt width="57" height="57" />
              </div>
              <div class="food-info">
                <h2>{{food.name}}</h2>
                <p class="desc" v-if="food.description">{{food.description}}</p>
                <div class="extra">
                  <span class="count">月售{{food.sellCount}}份</span>
                  <span>好评率{{food.rating}}%</span>
                </div>
                <div class="price">
                  <span class="now">￥{{food.price}}</span>
                  <span class="old" v-if="food.oldPrice">￥{{food.oldPrice}}</span>
                </div>
              </div>
            </li>
          </ul>
        </li>
      </ul>
    </div>
    <!-- 购物车 -->

    <shopcart
      :selectFood="selectedFood"
      :deliveryPrice="seller.deliveryPrice"
      :minPrice="seller.minPrice"
    ></shopcart>
  </div>
</template>
<script>
import { getGoods } from "api/api.js";
import icon from "components/icon/icon.vue";
import shopcart from "components/shopcart/shopcart.vue";
import BScroll from "better-scroll";
const STATUS = 0;
export default {
  props: {
    seller: {
      type: Object
    }
  },
  data() {
    return {
      goods: [],
      listHeight: [],
      scrollY: 0,
      selectedFood: []
    };
  },
  computed: {
    currentIndex() {
      for (let index = 0; index < this.listHeight.length - 1; index++) {
        let height1 = this.listHeight[index];
        let height2 = this.listHeight[index + 1];
        if (this.scrollY >= height1 && this.scrollY < height2) {
          return index;
        }
      }
      return 0;
    }
  },
  created() {
    this._getGoods();
    // this.$nextTick(() => {
    //   this._initScroll();
    //   this._calculateHeight();
    // });
    // setTimeout(() => {
    //   this._initScroll();
    //   this._calculateHeight();
    // }, 20);
  },
  mounted() {
    // setTimeout(() => {
    //   this._initScroll();
    //   this._calculateHeight();
    // }, 20);
    // this.$nextTick(() => {
    //   this._initScroll();
    //   this._calculateHeight();
    // });
  },
  methods: {
    selectMnue(index, event) {
      // bs 派发的原生事件 和浏览器事件冲突
      if (!event._constructed) {
        return;
      }
      let foodList = this.$refs.fw.firstChild.childNodes;
      let el = foodList[index];
      this.foodsScroll.scrollToElement(el, 300);
    },
    _getGoods() {
      getGoods().then(res => {
        if (res.status === STATUS) {
          this.goods = res.data;
          this.$nextTick(() => {
            this._initScroll();
            this._calculateHeight();
          });
        }
      });
    },
    _initScroll() {
      this.menuScroll = new BScroll(this.$refs.mw, {
        click: true
      });
      this.foodsScroll = new BScroll(this.$refs.fw, {
        probeType: 3
      });
      this.foodsScroll.on("scroll", pos => {
        // console.log(pos);
        this.scrollY = Math.abs(Math.round(pos.y));
      });
    },
    _calculateHeight() {
      let foodList = this.$refs.fw.firstChild.childNodes;
      let heihgt = 0;
      this.listHeight.push(heihgt);
      for (let index = 0; index < foodList.length; index++) {
        const element = foodList[index];
        heihgt += element.clientHeight;
        this.listHeight.push(heihgt);
      }
    }
  },
  components: {
    icon,
    shopcart
  }
};
</script>
<style scoped lang="stylus">
@import '~common/stylus/mixin.styl';

.goods {
  position: absolute;
  top: 174px;
  bottom: 46px;
  display: flex;
  overflow: hidden;
  width: 100%;

  .menu-wrapper {
    flex: 0 0 80px;
    width: 80px;
    background-color: #f3f5f7;

    .menu-item {
      display: table;
      height: 54px;
      width: 56px;
      line-height: 14px;
      padding: 0 12px;

      .text {
        font-size: 12px;
        display: table-cell;
        width: 56px;
        vertical-align: middle;
        border-1px(rgba(7, 17, 27, 0.1));
      }
    }

    .current {
      background-color: rgb(255, 255, 255);
      position: relative;
      margin-top: -1px;
      z-index: 10;
      font-weight: 700;

      .text {
        border-none();
      }
    }
  }

  .foods-wrapper {
    flex: 1;

    .foods-list {
      .title {
        padding-left: 14px;
        height: 26px;
        line-height: 26px;
        font-size: 12px;
        color: rgb(147, 153, 159);
        border-left: 2px solid #d9dde1;
        background-color: #f3f5f7;
      }

      .foods-item {
        display: flex;
        padding: 18px 18px;
        border-1px(rgba(7, 17, 27, 0.1));

        &:last-child {
          border-none();
        }

        .icon {
          margin-right: 10px;
          flex: 0 0 57px;
        }

        .food-info {
          flex: 1;

          h2 {
            font-size: 14px;
            font-weight: 700;
            margin-top: 2px;
            line-height: 14px;
          }

          .desc, .extra {
            font-size: 10px;
            line-height: 10px;
            margin: 8px 0 0 0;
            color: rgb(147, 153, 159);
          }

          .extra {
            .count {
              margin-right: 12px;
            }
          }

          .price {
            font-size: 0px;
            padding: 8px 0 0 0;
            font-weight: 700;

            .now {
              margin-right: 8px;
              font-size: 14px;
              line-height: 14px;
              color: rgb(240, 20, 20);
            }

            .old {
              font-size: 10px;
              text-decoration: line-through;
              color: rgb(147, 153, 159);
            }
          }
        }
      }
    }
  }
}
</style>