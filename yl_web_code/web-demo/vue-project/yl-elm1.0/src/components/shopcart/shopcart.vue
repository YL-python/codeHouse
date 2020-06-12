<template>
  <div class="shopcart">
    <div class="content">
      <div class="content-left">
        <div class="logo-wrapper">
          <div class="logo" :class="{'heightLight':totalCount>0}">
            <i class="icon-shopping_cart"></i>
          </div>
          <div class="num" v-show="totalCount>0">{{totalCount}}</div>
        </div>
        <div class="price" :class="{'heightLight':totalPrice>0}">￥{{totalPrice}}</div>
        <div class="desc">另需配送费 ￥{{deliveryPrice}}</div>
      </div>
      <div class="content-right" :class="totalPrice>minPrice?'heightLight':''">
        <div class="pay">{{payDesc}}</div>
      </div>
    </div>
  </div>
</template>
<script>
export default {
  props: {
    deliveryPrice: {
      type: Number,
      default: 0,
      required: true
    },
    minPrice: {
      type: Number,
      default: 0,
      required: true
    },
    selectFood: {
      type: Array,
      default() {
        return [];
      }
    }
  },
  data() {
    return {
      totalPrice: 0,
      totalCount: 0
    };
  },
  watch: {
    selectFood(newValue) {
      console.log(newValue);
      let totalP = 0;
      let totalC = 0;
      newValue.forEach(food => {
        totalP += food.price * food.conut;
        totalC += food.conut;
      });
      this.totalPrice = totalP;
      this.totalCount = totalC;
    }
  },
  computed: {
    payDesc() {
      let desc = "哎呀，出错啦！";
      if (this.totalPrice === 0) {
        desc = `满 ￥${this.minPrice} 起送`;
      } else if (this.totalPrice < this.minPrice) {
        desc = `还需 ￥${this.minPrice - this.totalPrice}起送`;
      } else {
        desc = "去结算";
      }
      return desc;
    }
  }
};
</script>
<style scoped lang='stylus'>
.shopcart {
  position: fixed;
  bottom: 0;
  left: 0;
  right: 0;
  z-index: 50;
  height: 48px;

  .content {
    display: flex;
    background-color: #141d27;
    color: rgba(255, 255, 255, 0.4);
    height: 100%;

    .content-left {
      flex: 1;
      font-size: 0px;

      .logo-wrapper {
        display: inline-block;
        width: 56px;
        height: 56px;
        position: relative;
        bottom: 8px;
        z-index: 100;
        border-radius: 50%;
        margin-left: 18px;
        padding: 6px;
        box-sizing: border-box;
        text-align: center;
        background-color: #141d27;

        .logo {
          width: 100%;
          height: 100%;
          border-radius: 50%;
          background-color: #2b343c;
          color: #80858a;

          &.heightLight {
            background-color: rgb(0, 160, 220);
            color: #ffffff;
          }

          i {
            font-size: 24px;
            line-height: 44px;
          }
        }

        .num {
          position: absolute;
          top: 0;
          right: 0;
          min-width: 24px;
          background-color: rgb(240, 20, 20);
          box-shadow: 0px 4px 8px 0px rgba(0, 0, 0, 0.4);
          font-size: 9px;
          line-height: 16px;
          color: #fff;
          border-radius: 12px;
          font-weight: 700;
        }
      }

      .price {
        display: inline-block;
        vertical-align: top;
        margin: 12px 0;
        padding: 0 12px;
        line-height: 24px;
        font-size: 16px;
        border-right: 1px solid rgba(255, 255, 255, 0.1);
        box-sizing: border-box;
        font-weight: 700;

        &.heightLight {
          color: #ffffff;
        }
      }

      .desc {
        display: inline-block;
        margin: 12px 0 12px 12px;
        font-size: 10px;
        line-height: 24px;
        vertical-align: top;
      }
    }

    .content-right {
      flex: 0 0 105px;
      width: 105px;
      text-align: center;
      background-color: #2b343c;

      &.heightLight {
        background-color: #00b43c;
        color: #fff;
        font-size: 16px;
      }

      .pay {
        font-size: 12px;
        height: 48px;
        line-height: 48px;
        font-weight: 700;
      }
    }
  }
}
</style>