<template>
  <div class="star" :class="starType">
    <span
      v-for="(itemClass ,index) in itemClasses"
      :key="index"
      :class="itemClass"
      class="start-item"
    >{{itemClass}}</span>
  </div>
</template>
<script>
const LENGTH = 5;
const CLS_ON = "on";
const CLS_HALF = "half";
const CLS_OFF = "off";

export default {
  props: {
    size: {
      // 尺寸
      type: Number,
      required: true
    },
    score: {
      // 评分
      type: Number,
      required: true
    }
  },
  computed: {
    starType() {
      return "star-" + this.size;
    },
    itemClasses() {
      let result = [];
      let score = Math.floor(this.score * 2) / 2;
      let integer = Math.floor(score);
      let hasHalf = integer - score === 0 ? 0 : 1;
      for (let index = 0; index < integer; index++) {
        result.push(CLS_ON);
      }
      if (hasHalf) {
        result.push(CLS_HALF);
      }
      while (result.length < LENGTH) {
        result.push(CLS_OFF);
      }
      // console.log(result);
      return result;
    }
  }
};
</script>
<style scoped lang="stylus">
@import '~common/stylus/mixin.styl';

.star {
  font-size: 0px;

  &.star-24 {
    .start-item {
      width: 10px;
      height: 10px;
      background-size: 10px 10px;
      margin-right: 3px;

      &:last-child {
        margin-right: 0px;
      }

      &.on {
        bg-image('star24_on');
      }

      &.half {
        bg-image('star24_half');
      }

      &.off {
        bg-image('star24_off');
      }
    }
  }

  &.star-36 {
    .start-item {
      width: 15px;
      height: 15px;
      background-size: 15px 15px;
      margin-right: 6px;

      &:last-child {
        margin-right: 0px;
      }

      &.on {
        bg-image('star36_on');
      }

      &.half {
        bg-image('star36_half');
      }

      &.off {
        bg-image('star36_off');
      }
    }
  }

  &.star-48 {
    .start-item {
      width: 20px;
      height: 20px;
      background-size: 20px 20px;
      margin-right: 22px;

      &:last-child {
        margin-right: 0px;
      }

      &.on {
        bg-image('star48_on');
      }

      &.half {
        bg-image('star48_half');
      }

      &.off {
        bg-image('star48_off');
      }
    }
  }

  .start-item {
    display: inline-block;
    background-repeat: no-repeat;
  }
}
</style>