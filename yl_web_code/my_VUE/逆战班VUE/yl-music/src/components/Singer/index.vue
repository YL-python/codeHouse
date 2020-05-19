<template>
  <div class="singers">
    <!-- 滚动区域 -->
    <div class="wrapper" ref="singerWrapper">
      <div class="content">
        <ul>
          <li v-for="(item,index) in singers" :key="index" class="singerGroup" :ref="item.Findex">
            <!-- 首字母 -->
            <h3>{{item.Findex}}</h3>
            <!-- 对应的歌手信息 -->
            <ol>
              <li v-for="(sItem,sIndex) in item.list"
              :key="sIndex"
              @click="goDetail(sItem.Fsinger_mid)">
                <img v-lazy="sItem.avator" alt />
                <span>{{sItem.Fsinger_name}}</span>
              </li>
            </ol>
          </li>
        </ul>
      </div>
    </div>
    <!-- 快速列表 -->
    <div class="quicklist">
      <ul
          @touchstart='touchStart'
          @touchmove='touchMove'
          @touchend='touchEnd'
        >
        <li
          v-for="(item,index) in quickData"
          :key="index"
          :class='selFindex==item?"quickItem sel":"quickItem"'
          @click='quickJump(item)'
        >{{item}}</li>
      </ul>
    </div>
    <!-- 详情页 -->
    <transition
      enter-active-class="animated faster slideInRight"
      leave-active-class="animated faster slideOutRight">
      <router-view></router-view>
    </transition>
  </div>
</template>
<script>
/*
1.请求数据 v
1.5 对请求的数据进行整理
2.根据数据渲染界面
[
  {Findex:A,list:[{a1},{a2},{a3}]}
  {Findex:b,list:[{b1},{b2},{b3}]}
]
3.渲染歌手列表 v
4.歌手列表能滚动 v
5.渲染快速入口 的数据 是和歌手列表数据进行关联 计算属性 v
6.歌手列表滚动可以控制快速入口 item切换 v
  滚动的时候 获取滚动区域内的首字母
  1. 首字母数字 quickdata
  2. 距离数组  每一组歌手块的高度
  3. 判断向上移动的距离在距离数组里的下标
  4. 根据下标在首字母数组里获取首字母
7.快速入扣点击  可以控制歌手   滚动  v
  1.点击快速入口
  2.点完了需要能滚
8.快速入口滑动 控制歌手滚动
  a.获取按下点的坐标
  b.移动的过程中 计算 移动过的距离
  c.用移动过的距离除以每一个快的尺寸 计算出滚动了多少格格
  4.起始点的下标 +滚动的格格数  求出滚动的字母位置
  5. scrollElement 左边滚动到某一个元素

9.点击歌手进入到歌手详情页

*/
import { getSingersData } from 'api/api.js'
import { nomalData } from './index'
import BS from 'better-scroll'
export default {
  data () {
    return {
      singers: [],
      selFindex: '热'
    }
  },
  created () {
    // 初始化数据 把移动距离挂载到this对象下
    this.touch = { y: 0 }
    getSingersData().then(res => {
      const data = nomalData(res.data.list)
      this.singers = data
      // console.log(data)
      // 请求到数据之后在进行初始化
      this.$nextTick(() => {
        this.initBS()
      })
    })
  },
  methods: {
    goDetail (mid) {
      // console.log('goDetail:', mid)
      this.$router.push(`/singer/${mid}`)
    },
    // 手指的触摸移动事件
    touchStart (e) {
      // 设定距离屏幕顶部的位置是140
      const y = e.touches[0].pageY
      // 获取按下的格子下标
      const startCount = parseInt((y - 140) / 18)
      this.touch.y = y
      this.touch.startCount = startCount
      // console.log('按下', y, startCount)
    },
    touchMove (e) {
      const moveY = e.touches[0].pageY
      const moveDis = moveY - this.touch.y // 计算出移动过的距离
      const count = parseInt(moveDis / 18) // 获取移动过的格子数
      // console.log('移动', moveDis, count)
      const moveIndex = this.touch.startCount + count // 获取下标
      // 防止超出边界
      if (moveIndex < 0 || moveIndex > this.quickData.length - 1) { return false }
      const moveFindex = this.quickData[moveIndex]
      this.quickJump(moveFindex)
    },
    touchEnd () {
      // console.log('抬起')
    },
    initBS () {
      const wapper = this.$refs.singerWrapper
      /* eslint-disable no-new */
      this.Bs = new BS(wapper, { probeType: 3, click: true })
      // BS 默认不能点击， click: true配置可以点击
      // 获取距离数组
      const distance = []
      for (const key in this.$refs) {
        if (key !== 'singerWrapper') {
          distance.push(this.$refs[key][0].offsetTop)
        }
      }
      // console.log(distance)
      // 监听滚动
      this.Bs.on('scroll', (pos) => {
        const y = Math.abs(pos.y)
        // console.log('滚了', y)
        // 判断每一次滚动的距离在什么范围内
        let scrollIndex = 0 // 滚动所在区域的下标
        for (let index = 0; index < distance.length; index++) {
          if (y >= distance[index] && y < distance[index + 1]) {
            scrollIndex = index
          } else if (y >= distance[distance.length - 1]) {
            //  最后的边界判断
            scrollIndex = distance.length - 1
          }
        }
        // 根据下标换字母
        const scrollFindex = this.quickData[scrollIndex]
        // console.log(scrollFindex)
        this.selFindex = scrollFindex
      })
    },
    quickJump (Findex) {
      // 点击每一项之后 触发事件需要知道点到谁了
      // 根据字母获取到固定的元素
      const dom = this.$refs[Findex][0]
      // console.log('点到我了', Findex, dom)
      // //  用bs 内部的方法直接跳转到固定元素
      this.Bs.scrollToElement(dom, 500)
    }
  },
  // 计算属性，快速入口的数据要和歌手数据关联
  computed: {
    quickData: function () {
      const result = this.singers.map(item => {
        return item.Findex
      })
      return result
    }
  }
}
</script>
<style lang="less" scoped>
// 只有在样式里面使用别名需要加 ~
@import "~style/index.less";
.singers {
  position: fixed;
  top: 88px;
  bottom: 0px;
  left: 0px;
  right: 0px;
  .wrapper {
    height: 100%;
    overflow: hidden;
    .content {
      .w(375);
      h3 {
        height: 30px;
        line-height: 30px;
        color: rgba(255, 255, 255, 0.5);
        background: #333;
        font-size: @fs-s;
        padding-left: 20px;
      }
      ol {
        li {
          .w(375);
          height: 70px;
          box-sizing: border-box;
          padding: 20px 0px 0px 30px;
          display: flex;
          align-items: center;
          img {
            width: 50px;
            height: 50px;
            border-radius: 25spx;
          }
          span {
            padding-left: 20px;
            display: inline-block;
            height: 50px;
            line-height: 50px;
            font-size: @fs-s;
            color: rgba(255, 255, 255, 0.5);
          }
        }
      }
    }
  }
}
.singerGroup {
  padding-bottom: 20px;
}
.quicklist {
  position: absolute;
  right: 0;
  top: 50px;
  width: 20px;
  background: rgba(0, 0, 0, 0.3);
  font-size: @fs-s;
  padding: 20px 0;
  color: rgba(255, 255, 255, 0.5);
  text-align: center;
  border-radius: 10px;
}
.quickItem {
  padding: 3px;
  height: 12px;
  line-height: 12px;
}
.sel {
  color: @yellow;
}
</style>
