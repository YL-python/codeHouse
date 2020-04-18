<template>
  <scroll
    class="listview"
    :data="data"
    ref="listview"
    :listenScroll="listenScroll"
    :probeType="probeType"
    @scroll="scroll"
  >
    <ul>
      <li v-for="(group,gIndex) in data" class="list-group" ref="listGroup" :key="gIndex">
        <h2 class="list-group-title">{{group.title}}</h2>
        <ul>
          <li v-for="(item,iIndex) in group.items" class="list-group-item" :key="iIndex">
            <img class="avatar" v-lazy="item.avatar" />
            <span class="name">{{item.name}}</span>
          </li>
        </ul>
      </li>
    </ul>
    <div
      class="list-shortcut"
      @touchstart.stop.prevent="onShortcutTouchStart"
      @touchmove.stop.prevent="onShortcutTouchMove"
      @touchend.stop
    >
      <ul>
        <!-- data-index H5自定义属性，用来获取点击的元素的索引 -->
        <li
          v-for="(item, index) in shortcutList"
          :data-index="index"
          class="item"
          :class="{'current':currentIndex===index}"
          :key="index"
        >{{item}}</li>
      </ul>
    </div>
    <div class="list-fixed" ref="fixed" v-show="fixedTitle">
      <div class="fixed-title">{{fixedTitle}}</div>
    </div>
    <div v-show="!data.length" class="loading-container">
      <loading></loading>
    </div>
  </scroll>
</template>

<script type="text/ecmascript-6">
import Scroll from "base/scroll/scroll";
import Loading from "base/loading/loading";
import { getData } from "common/js/dom";

const TITLE_HEIGHT = 30;
const ANCHOR_HEIGHT = 18; // 快速入口每一个元素的高度，用来计算移动多少个时候用的

export default {
  props: {
    data: {
      // 数据
      type: Array,
      default: null
    }
  },
  computed: {
    // 快速入口列表数据
    shortcutList() {
      return this.data.map(group => {
        return group.title.substr(0, 1);
      });
    },
    // 头部标题
    fixedTitle() {
      if (this.scrollY > 0) {
        return "";
      }
      return this.data[this.currentIndex]
        ? this.data[this.currentIndex].title
        : "";
    }
  },
  data() {
    return {
      scrollY: -1, // 滚动Y坐标起始值
      currentIndex: 0, // 快速入口的选定项
      diff: -1 // 顶部重合的时候一个动画效果的偏移量
    };
  },
  created() {
    this.probeType = 3; // scroll组件监听事件的类型
    this.listenScroll = true; // 监听滚动事件
    this.touch = {}; // 记录快速入口点击时候的一些数值
    this.listHeight = []; // 计算每一个 list-group 的高度方便做联动
    this.fixedTop = 0   // 下一个标题距离顶部的距离 默认是0
  },
  methods: {
    selectItem(item) {
      this.$emit("select", item);
    },
    // 开始触摸事件，用来获取 点击的快速入口元素的下标
    onShortcutTouchStart(e) {
      // console.log(e);
      let anchorIndex = getData(e.target, "index"); // 点击元素的下标
      let firstTouch = e.touches[0];
      this.touch.y1 = firstTouch.pageY;
      this.touch.anchorIndex = anchorIndex; // 当前点击的下标，是字符串

      this._scrollTo(anchorIndex); // 把滚动组件的跳转方法封装一下
    },
    onShortcutTouchMove(e) {
      let firstTouch = e.touches[0];
      this.touch.y2 = firstTouch.pageY;
      let delta = ((this.touch.y2 - this.touch.y1) / ANCHOR_HEIGHT) | 0; // 或 0 是向下取整
      let anchorIndex = parseInt(this.touch.anchorIndex) + delta;

      this._scrollTo(anchorIndex);
    },
    refresh() {
      this.$refs.listview.refresh();
    },
    scroll(pos) {
      // 监听滚动事件
      this.scrollY = pos.y;
      if(this.listHeight.length === 0){
        console.log("listHeight值突然消失");
        // 出现值突然消失，不太清楚啥情况，现在的解决方法就是值消失了就重新获取
        this._calculateHeight()
      }
    },
    _calculateHeight() {
      // 计算每一个 list-group 的高度方便做联动
      const list = this.$refs.listGroup;
      let height = 0;
      this.listHeight.push(height);
      for (let i = 0; i < list.length; i++) {
        let item = list[i];
        height += item.clientHeight;
        this.listHeight.push(height);
      }
    },
    _scrollTo(index) {
      // 封装跳转方法
      if (!index && index !== 0) {
        return;
      }
      if (index < 0) {
        index = 0;
      } else if (index > this.listHeight.length - 2) {
        index = this.listHeight.length - 2;
      }
      // 点击事件不会触发滚动事件，我们自己派发一个滚动事件
      this.scrollY = -this.listHeight[index];
      // 400 是滚动动画的时间
      this.$refs.listview.scrollToElement(this.$refs.listGroup[index], 400);
    }
  },
  watch: {
    data() {
      // 监听  data 数据的变化  渲染dom以及计算每一个group的高度
      setTimeout(() => {
        this._calculateHeight();
      }, 20);
    },
    scrollY(newY) {
      const listHeight = this.listHeight;
      // 当滚动到顶部，newY>0
      if (newY > 0) {
        this.currentIndex = 0;
        return;
      }
      // 在中间部分滚动  遍历范围是listHeight.length - 1
      for (let i = 0; i < listHeight.length - 1; i++) {
        let height1 = listHeight[i];
        let height2 = listHeight[i + 1];
        if (-newY >= height1 && -newY < height2) {
          this.currentIndex = i;
          this.diff = height2 + newY;
          return;
        }
      }
      // 当滚动到底部，且-newY大于最后一个元素的上限
      this.currentIndex = listHeight.length - 2;
    },
    diff(newVal) {
      let fixedTop =
        newVal > 0 && newVal < TITLE_HEIGHT ? newVal - TITLE_HEIGHT : 0;
      // 判断两个标题之间的距离，在需要移动的时候才设置值进行移动
      if (this.fixedTop === fixedTop) {
        return;
      }
      // if 判断是因为需要做 dom操作，而 diff值的变化是很频繁的，只有这个值不是0的时候我们才进行dom操作
      this.fixedTop = fixedTop;
      this.$refs.fixed.style.transform = `translate3d(0,${fixedTop}px,0)`;
    }
  },
  components: {
    Scroll,
    Loading
  }
};
</script>

<style scoped lang="stylus" rel="stylesheet/stylus">
@import '~common/stylus/variable';

.listview {
  position: relative;
  width: 100%;
  height: 100%;
  overflow: hidden;
  background: $color-background;

  .list-group {
    padding-bottom: 30px;

    .list-group-title {
      height: 30px;
      line-height: 30px;
      padding-left: 20px;
      font-size: $font-size-small;
      color: $color-text-l;
      background: $color-highlight-background;
    }

    .list-group-item {
      display: flex;
      align-items: center;
      padding: 20px 0 0 30px;

      .avatar {
        width: 50px;
        height: 50px;
        border-radius: 50%;
      }

      .name {
        margin-left: 20px;
        color: $color-text-l;
        font-size: $font-size-medium;
      }
    }
  }

  .list-shortcut {
    position: absolute;
    z-index: 30;
    right: 0;
    top: 50%;
    transform: translateY(-50%);
    width: 20px;
    padding: 20px 0;
    border-radius: 10px;
    text-align: center;
    background: $color-background-d;
    font-family: Helvetica;

    .item {
      padding: 3px;
      line-height: 1;
      color: $color-text-l;
      font-size: $font-size-small;

      &.current {
        color: $color-theme;
      }
    }
  }

  .list-fixed {
    position: absolute;
    top: 0;
    left: 0;
    width: 100%;

    .fixed-title {
      height: 30px;
      line-height: 30px;
      padding-left: 20px;
      font-size: $font-size-small;
      color: $color-text-l;
      background: $color-highlight-background;
    }
  }

  .loading-container {
    position: absolute;
    width: 100%;
    top: 50%;
    transform: translateY(-50%);
  }
}
</style>
