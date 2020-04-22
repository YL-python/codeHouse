<template>
  <transition name="slide">
    <music-list :rank="rank" :title="title" :bg-image="bgImage" :songs="songs"></music-list>
  </transition>
</template>

<script type="text/ecmascript-6">
import MusicList from "components/music-list/music-list";
import { getMusicList } from "api/rank";
import { ERR_OK } from "api/config";
import { mapGetters } from "vuex";
import { createSong, filterSong } from "common/js/song";
import { getRealSongUrl } from "api/singer";

export default {
  computed: {
    title() {
      return this.topList.topTitle;
    },
    bgImage() {
      if (this.songs.length) {
        return this.songs[0].image;
      }
      return "";
    },
    ...mapGetters(["topList"])
  },
  data() {
    return {
      songs: [],
      rank: true
    };
  },
  created() {
    this._getMusicList();
  },
  methods: {
    _getMusicList() {
      if (!this.topList.id) {
        this.$router.push("/rank");
        return;
      }
      getMusicList(this.topList.id).then(res => {
        // console.log(res);
        if (res.code === ERR_OK) {
          this.songs = this._normalizeSongs(res.songlist);
          getRealSongUrl(this.songs).then(data => {
            if (data.data.result === 100) {
              this.songs = filterSong(this.songs, data.data.data);
              // console.log(this.songs);
            }
          });
        }
      });
    },
    _normalizeSongs(list) {
      let ret = [];
      list.forEach(item => {
        const musicData = item.data;
        if (musicData.songid && musicData.albummid) {
          ret.push(createSong(musicData));
        }
      });
      return ret;
    }
  },
  components: {
    MusicList
  }
};
</script>

<style scoped lang="stylus" rel="stylesheet/stylus">
.slide-enter-active, .slide-leave-active {
  transition: all 0.3s ease;
}

.slide-enter, .slide-leave-to {
  transform: translate3d(100%, 0, 0);
}
</style>