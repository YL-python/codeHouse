<template>
  <transition name="slide">
    <music-list :title="title" :bg-image="bgImage" :songs="songs"></music-list>
  </transition>
</template>

<script type="text/ecmascript-6">
import MusicList from "components/music-list/music-list";
import { mapGetters } from "vuex";
import { getSingerDetail, getRealSongUrl } from "api/singer";
import { ERR_OK } from "api/config";
import { createSong, filterSong } from "common/js/song.js";
export default {
  data() {
    return {
      songs: []
    };
  },
  computed: {
    title() {
      return this.singer.name;
    },
    bgImage() {
      return this.singer.avatar;
    },
    ...mapGetters(["singer"])
  },
  created() {
    // console.log(this.singer);
    this._getDetail();
  },
  methods: {
    _getDetail() {
      if (!this.singer.id) {
        this.$router.push("/singer");
        return;
      }
      getSingerDetail(this.singer.id).then(res => {
        // console.log(res);
        if (res.code === ERR_OK) {
          this.songs = this._normalizeSongs(res.data.list);
          getRealSongUrl(this.songs).then(data => {
            if (data.data.result === 100) {
              this.songs = filterSong(this.songs, data.data.data);
            }
          });
        }
      });
    },
    _normalizeSongs(list) {
      let res = [];
      list.forEach(element => {
        let { musicData } = element;
        if (musicData.songid && musicData.albummid) {
          // 必须要有的数据
          // 调用工厂函数
          res.push(createSong(musicData));
        }
      });
      return res;
    }
  },
  components: {
    MusicList
  }
};
</script>

<style scoped lang="stylus" rel="stylesheet/stylus">
.slide-enter-active, .slide-leave-active {
  transition: all 0.3s;
}

.slide-enter, .slide-leave-to {
  transform: translate3d(100%, 0, 0);
}
</style>