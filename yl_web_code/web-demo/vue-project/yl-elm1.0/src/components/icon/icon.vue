<template>
  <span v-show="iconType>=0" class="icon" :class="[iconClass,marginRight]"></span>
</template>
<script>
export default {
  props: {
    iconType: {
      type: Number
    },
    iconNum: {
      type: String
    },
    mr: {
      type: String
    }
  },
  created() {
    this.classMap = ["decrease", "discount", "special", "invoice", "guarantee"];
  },
  computed: {
    iconClass() {
      return "icon-" + this.classMap[this.iconType] + "-" + this.iconNum;
    },
    marginRight() {
      if (this.mr) {
        return "mr-" + this.mr;
      } else {
        return "";
      }
    }
  }
};
</script>
<style scoped lang="stylus">
@import '~common/stylus/mixin.styl';

.icon {
  display: inline-block;
  vertical-align: top;
  background-repeat: no-repeat;

  &.icon-decrease-1, &.icon-decrease-3 {
    width: 12px;
    height: 12px;
    background-size: 12px 12px;
  }

  &.icon-decrease-1 {
    bg-image('decrease_1');
  }

  &.icon-decrease-3 {
    bg-image('decrease_3');
  }

  &.icon-decrease-2, &.icon-decrease-4 {
    width: 16px;
    height: 16px;
    background-size: 16px 16px;
  }

  &.icon-decrease-2 {
    bg-image('decrease_2');
  }

  &.icon-decrease-4 {
    bg-image('decrease_4');
  }

  &.icon-discount-1, &.icon-discount-3 {
    width: 12px;
    height: 12px;
    background-size: 12px 12px;
  }

  &.icon-discount-1 {
    bg-image('discount_1');
  }

  &.icon-discount-3 {
    bg-image('discount_3');
  }

  &.icon-discount-2, &.icon-discount-4 {
    width: 16px;
    height: 16px;
    background-size: 16px 16px;
  }

  &.icon-discount-2 {
    bg-image('discount_2');
  }

  &.icon-discount-4 {
    bg-image('discount_4');
  }

  &.icon-guarantee-1, &.icon-guarantee-3 {
    width: 12px;
    height: 12px;
    background-size: 12px 12px;
  }

  &.icon-guarantee-1 {
    bg-image('guarantee_1');
  }

  &.icon-guarantee-3 {
    bg-image('guarantee_3');
  }

  &.icon-guarantee-2, &.icon-guarantee-4 {
    width: 16px;
    height: 16px;
    background-size: 16px 16px;
  }

  &.icon-guarantee-2 {
    bg-image('guarantee_2');
  }

  &.icon-guarantee-4 {
    bg-image('guarantee_4');
  }

  &.icon-invoice-1, &.icon-invoice-3 {
    width: 12px;
    height: 12px;
    background-size: 12px 12px;
  }

  &.icon-invoice-1 {
    bg-image('invoice_1');
  }

  &.icon-invoice-3 {
    bg-image('invoice_3');
  }

  &.icon-invoice-2, &.icon-invoice-4 {
    width: 16px;
    height: 16px;
    background-size: 16px 16px;
  }

  &.icon-invoice-2 {
    bg-image('invoice_2');
  }

  &.icon-invoice-4 {
    bg-image('invoice_4');
  }

  &.icon-special-1, &.icon-special-3 {
    width: 12px;
    height: 12px;
    background-size: 12px 12px;
  }

  &.icon-special-1 {
    bg-image('special_1');
  }

  &.icon-special-3 {
    bg-image('special_3');
  }

  &.icon-special-2, &.icon-special-4 {
    width: 16px;
    height: 16px;
    background-size: 16px 16px;
  }

  &.icon-special-2 {
    bg-image('special_2');
  }

  &.icon-special-4 {
    bg-image('special_4');
  }
}

.mr-2 {
  margin: 0 2px 0 0;
}

.mr-4 {
  margin: 0 4px 0 0;
}

.mr-6 {
  margin: 0 6px 0 0;
}
</style>