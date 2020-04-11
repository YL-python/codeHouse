<template>
  <div class="recommend">
    <!-- <Banner :banners="list"></Banner> -->
    <!-- 滚动区域 -->
    <div class="wrapper" ref="wrapper">
      <div class="content">
        <!-- 轮播图 -->
        <Banner :banners="list"></Banner>
        <!-- 歌曲列表 -->
        <div class="list-title">歌曲推荐</div>
        <ul class="list">
          <li v-for="(item,index) in recommendList" :key="index">
            <div class="left">
              <!-- <img :src="item.imgurl" alt /> -->
              <!-- 懒加载指令 -->
              <img v-lazy="item.imgurl" alt />
            </div>
            <div class="right">
              <p class="name">{{item.creator.name}}</p>
              <p class="album">{{item.dissname}}</p>
            </div>
          </li>
        </ul>
      </div>
    </div>
  </div>
</template>
<script>
import Banner from '../Banner/index'
// import axios from '../../utils/axios'
import BS from 'better-scroll'
import { getBannerData, getRecommendData } from '../../api/api'
export default {
  components: {
    Banner
  },
  data: function () {
    return {
      list: [],
      recommendList: []
    }
  },
  methods: {
    // getBannerData () {
    //   const url =
    //     // '/hehe/image/girl/list/random?app_id=hmnqziklvnthnckr&app_secret=TFZnZVdMSVdCdUlVUEhaOFVQOHBZdz09'
    //     '/xixi/music/api/getTopBanner?g_tk=1928093487&inCharset=utf8&outCharset=utf-8&notice=0&format=json&platform=yqq.json&hostUin=0&needNewCode=0&-=recom012845016368453477&data=%7B%22comm%22:%7B%22ct%22:24%7D,%22category%22:%7B%22method%22:%22get_hot_category%22,%22param%22:%7B%22qq%22:%22%22%7D,%22module%22:%22music.web_category_svr%22%7D,%22recomPlaylist%22:%7B%22method%22:%22get_hot_recommend%22,%22param%22:%7B%22async%22:1,%22cmd%22:2%7D,%22module%22:%22playlist.HotRecommendServer%22%7D,%22playlist%22:%7B%22method%22:%22get_playlist_by_category%22,%22param%22:%7B%22id%22:8,%22curPage%22:1,%22size%22:40,%22order%22:5,%22titleid%22:8%7D,%22module%22:%22playlist.PlayListPlazaServer%22%7D,%22new_song%22:%7B%22module%22:%22newsong.NewSongServer%22,%22method%22:%22get_new_song_info%22,%22param%22:%7B%22type%22:5%7D%7D,%22new_album%22:%7B%22module%22:%22newalbum.NewAlbumServer%22,%22method%22:%22get_new_album_info%22,%22param%22:%7B%22area%22:1,%22sin%22:0,%22num%22:10%7D%7D,%22new_album_tag%22:%7B%22module%22:%22newalbum.NewAlbumServer%22,%22method%22:%22get_new_album_area%22,%22param%22:%7B%7D%7D,%22toplist%22:%7B%22module%22:%22musicToplist.ToplistInfoServer%22,%22method%22:%22GetAll%22,%22param%22:%7B%7D%7D,%22focus%22:%7B%22module%22:%22QQMusic.MusichallServer%22,%22method%22:%22GetFocus%22,%22param%22:%7B%7D%7D%7D'
    //   // axios.get(url, () => {})
    //   //   .then((res) => {
    //   //     console.log(res)
    //   //   })
    //   this.$axios.get(url).then(res => {
    //     // console.log(res)
    //     this.list = res.data.slider
    //   })
    // },
    // getRecommendData () {
    //   const url =
    //     '/xixi/music/api/getDiscList?g_tk=1928093487&inCharset=utf-8&outCharset=utf-8&notice=0&format=json&platform=yqq&hostUin=0&sin=0&ein=29&sortId=5&needNewCode=0&categoryId=10000000&rnd=0.3321077924954854'
    //   this.$axios.get(url).then(res => {
    //     // console.log(res.data)
    //     // this.list = res.data.slider
    //     this.recommendList = res.data.list
    //   })
    // },
    initBS () {
      const wrapper = this.$refs.wrapper
      /* eslint-disable no-new */
      new BS(wrapper, {})
    }
  },
  mounted () {
    // this.getBannerData()
    // this.getRecommendData()
    getBannerData().then(res => {
      this.list = res.data.slider
    })
    getRecommendData().then(res => {
      this.recommendList = res.data.list
    })
    this.initBS()
  }
}
</script>
<style lang="less" scoped>
@import "../../style/index.less";
.wrapper {
  overflow: hidden;
  position: fixed;
  top: 88px;
  bottom: 0px;
  left: 0px;
  right: 0px;
  .content {
    .w(375);
    .list-title {
      .w(375);
      height: 65px;
      text-align: center;
      line-height: 65px;
      color: @yellow;
      font-size: @fs-s;
    }
    .list {
      li {
        .w(375);
        padding: 0px 20px 20px 20px;
        height: 82px;
        box-sizing: border-box;
        display: flex;
        .left {
          width: 82px;
          height: 60px;
          img {
            width: 60spx;
            height: 60px;
          }
        }
        .right {
          color: #ffffff;
          font-size: @fs-s;
          .name {
            margin-bottom: 10px;
          }
          .album {
            color: hsla(0, 0%, 100%, 0.3);
          }
        }
      }
    }
  }
}
</style>
