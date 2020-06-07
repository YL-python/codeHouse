<template>
  <div class="header">
    <div class="content-wrapper">
      <div class="avatar">
        <img :src="seller.avatar" alt width="64" height="64" />
      </div>
      <div class="content">
        <div class="title">
          <span class="brand"></span>
          <span class="name">{{seller.name}}</span>
        </div>
        <div class="description">{{seller.description}}/{{seller.deliveryTime}}分钟内送达</div>
        <!-- v-if 判断是必须的，一开始还没有数据，传进来的是空对象，没有supports属性 -->
        <div v-if="seller.supports" class="support">
          <!-- <span class="icon" :class="classMap[seller.supports[0].type]"></span> -->
          <icon :iconType="seller.supports[0].type" iconNum="1" mr="4"></icon>
          <span class="text">{{seller.supports[0].description}}</span>
        </div>
      </div>
      <div v-if="seller.supports" class="support-count" @click="detailShow = true">
        <span class="count">{{seller.supports.length}}个</span>
        <i class="icon-keyboard_arrow_right"></i>
      </div>
    </div>

    <div class="bulletin-wrapper" @click="detailShow = true">
      <span class="bulletin-title"></span>
      <span class="bulletin-text">{{seller.bulletin}}</span>
      <i class="icon-keyboard_arrow_right"></i>
    </div>

    <div class="background">
      <img :src="seller.avatar" width="100%" height="100%" />
    </div>

    <transition name="fade">
      <div v-if="detailShow" class="detail">
        <!-- 完美解决 sticky footer 布局 -->
        <!-- 需要使用一个容器包裹本身的内容并且清楚浮动 -->
        <div class="detail-wrapper clearfix">
          <div class="detail-content">
            <h1 class="name">{{seller.name}}</h1>
            <div class="star-wrapper">
              <star :size="48" :score="seller.score"></star>
            </div>
            <lineText info="优惠信息"></lineText>
            <ul v-if="seller.supports" class="supports">
              <li class="support-item" v-for="(item,index) in seller.supports" :key="index">
                <!-- <span class="icon" :class="classMap[seller.supports[index].type]"></span> -->
                <icon :iconType="seller.supports[index].type" iconNum="2" mr="6"></icon>
                <span class="text">{{seller.supports[index].description}}</span>
              </li>
            </ul>
            <lineText info="商家公告"></lineText>
            <div class="bulletin">
              <p class="content">{{seller.bulletin}}</p>
            </div>
          </div>
        </div>
        <!-- footer -->
        <div class="detail-close">
          <i class="icon-close" @click="detailShow = false"></i>
        </div>
      </div>
    </transition>
  </div>
</template>
<script>
import star from "components/star/star.vue";
import lineText from "components/twoLineTextCenter/twoLineTextCenter.vue";
import icon from "components/icon/icon.vue";
export default {
  props: {
    seller: {
      type: Object,
      required: true
    }
  },
  data() {
    return {
      detailShow: false
    };
  },
  components: {
    star,
    lineText,
    icon
  }
};
</script>
<style scoped lang='stylus'>
@import '~common/stylus/mixin.styl';

.header {
  color: #fff;
  position: relative;
  background-color: rgba(7, 17, 27, 0.5);
  // 模糊效果会溢出
  overflow: hidden;

  .content-wrapper {
    padding: 24px 12px 18px 24px;
    font-size: 0px;
    position: relative;

    .avatar {
      display: inline-block;
      vertical-align: top;

      img {
        border-radius: 10px;
      }
    }

    .content {
      display: inline-block;
      margin-left: 16px;

      .title {
        font-size: 16px;
        margin: 2px 0 8px 0;

        .brand {
          display: inline-block;
          vertical-align: top;
          width: 30px;
          height: 18px;
          bg-image('brand');
          background-size: 30px 18px;
          background-repeat: no-repeat;
        }

        .name {
          font-weight: bold;
          margin-left: 6px;
          line-height: 18px;
        }
      }

      .description {
        font-size: 12px;
        margin: 0 0 10px 0;
        line-height: 12px;
        font-weight: 200;
      }

      .support {
        .text {
          font-size: 10px;
          line-height: 12px;
          font-weight: 200;
        }
      }
    }

    .support-count {
      position: absolute;
      right: 12px;
      bottom: 14px;
      padding: 0px 8px;
      height: 24px;
      line-height: 24px;
      border-radius: 14px;
      background-color: rgba(0, 0, 0, 0.2);
      font-size: 10px;
      text-align: center;

      .count {
        margin-right: 2px;
        vertical-align: top;
      }

      i {
        text-align: center;
        line-height: 24px;
      }
    }
  }

  .bulletin-wrapper {
    position: relative;
    height: 28px;
    line-height: 28px;
    padding: 0 22px 0 12px;
    white-space: nowrap;
    overflow: hidden;
    text-overflow: ellipsis;
    background-color: rgba(7, 17, 7, 0.2);

    .bulletin-title {
      display: inline-block;
      margin-top: 8px;
      vertical-align: top;
      width: 22px;
      height: 12px;
      bg-image('bulletin');
      background-size: 22px 12px;
      background-repeat: no-repeat;
    }

    .bulletin-text {
      vertical-align: top;
      font-size: 10px;
      line-height: 28px;
      font-weight: 200;
      margin: 0 4px;
    }

    .icon-keyboard_arrow_right {
      position: absolute;
      font-size: 10px;
      right: 12px;
      top: 8px;
    }
  }

  .background {
    position: absolute;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    z-index: -1;
    overflow: hidden;
    filter: blur(10px);
  }

  .detail {
    position: fixed;
    z-index: 100;
    top: 0;
    left: 0;
    bottom: 0;
    right: 0;
    overflow: auto;
    background: rgba(7, 17, 27, 0.8);
    backdrop-filter: blur(10px);

    &.fade-enter-active, &.fade-leave-active {
      transition: opacity 0.5s;
    }

    &.fade-enter, &.fade-leave-to {
      opacity: 0;
    }

    .detail-wrapper {
      width: 100%;
      min-height: 100%;

      .detail-content {
        margin-top: 64px;
        // 这个padding-bottom 很重要
        padding-bottom: 64px;

        .name {
          line-height: 16px;
          text-align: center;
          font-size: 16px;
          font-weight: 700px;
        }

        .star-wrapper {
          margin: 18px 0 28px 0;
          padding: 2px 0;
          text-align: center;
        }

        .supports {
          width: 80%;
          margin: 0 auto;

          .support-item {
            padding: 0 12px;
            margin: 0 0 6px 0;
            font-size: 0;

            &:last-child {
              margin: 0;
            }

            .text {
              font-size: 12px;
              line-height: 16px;
              font-weight: 200;
            }
          }
        }

        .bulletin {
          width: 80%;
          margin: 0 auto;

          .content {
            font-size: 12px;
            line-height: 24px;
            font-weight: 200;
            padding: 0 12px;
          }
        }
      }
    }

    .detail-close {
      position: relative;
      width: 32px;
      height: 32px;
      font-size: 32px;
      margin: -64px auto 0 auto;
      clear: both;
    }
  }
}
</style>