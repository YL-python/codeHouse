<template>
  <scroll
    ref="suggest"
    class="suggest"
    :data="result"
    :pullup="pullup"
    :beforeScroll="beforeScroll"
    @scrollToEnd="searchMore"
    @beforeScroll="listScroll"
  >
    <ul class="suggest-list">
      <li
        @click="selectItem(item)"
        class="suggest-item"
        v-for="(item,index) in result"
        :key="index"
      >
        <div class="icon">
          <i :class="getIconCls(item)"></i>
        </div>
        <div class="name">
          <p class="text" v-html="getDisplayName(item)"></p>
        </div>
      </li>
      <loading v-show="hasMore" title></loading>
    </ul>
    <div v-show="!hasMore && !result.length" class="no-result-wrapper">
      <no-result title="抱歉，暂无搜索结果"></no-result>
    </div>
  </scroll>
</template>

<script type="text/ecmascript-6">
import Scroll from "base/scroll/scroll";
import Loading from "base/loading/loading";
import NoResult from "base/no-result/no-result";
import { search } from "api/search";
import { ERR_OK } from "api/config";
import { createSong, filterSong } from "common/js/song";
import { mapMutations, mapActions } from "vuex";
import Singer from "common/js/singer";
import { getRealSongUrl } from "api/singer";

const TYPE_SINGER = "singer";
const perpage = 20; // 每一页的数据量

export default {
  props: {
    // 搜索结果要不要歌手
    showSinger: {
      type: Boolean,
      default: true
    },
    // 搜索词
    query: {
      type: String,
      default: ""
    }
  },
  data() {
    return {
      page: 1, // 当前页码
      pullup: true, // 监听上拉加载
      beforeScroll: true,
      hasMore: true, // 是否有更多的数据
      result: [] // 接收搜索结果
    };
  },
  methods: {
    refresh() {
      this.$refs.suggest.refresh();
    },
    // 监听query 的变化来请求数据
    search() {
      search(this.query, this.page, this.showSinger, perpage).then(res => {
        if (res.data.code === ERR_OK) {
          this.result = this._genResult(res.data.data);
          this._checkMore(res.data.data);
        }
      });
    },
    // 处理搜索结果 返回数据中的 歌手数据
    _genResult(data) {
      let ret = [];
      let songList = [];
      if (data.zhida && data.zhida.singerid) {
        ret.push({ ...data.zhida, ...{ type: TYPE_SINGER } });
      }
      if (data.song) {
        songList = this._normalizeSongs(data.song.list);
        getRealSongUrl(songList).then(data => {
          if (data.data.result === 100) {
            songList = filterSong(songList, data.data.data);
          }
        });
      }
      ret = ret.concat(songList);
      return ret;
    },
    // 处理搜索结果 返回数据中的 歌曲数据
    _normalizeSongs(list) {
      let ret = [];
      list.forEach(musicData => {
        if (musicData.songid && musicData.albummid) {
          ret.push(createSong(musicData));
        }
      });
      return ret;
    },
    // 检测能不能搜索更多
    _checkMore(data) {
      const song = data.song;
      if (
        !song.list.length ||
        song.curnum + song.curpage * perpage > song.totalnum
      ) {
        this.hasMore = false;
      }
    },
    // 搜索列表显示的图标
    getIconCls(item) {
      if (item.type === TYPE_SINGER) {
        return "icon-mine";
      } else {
        return "icon-music";
      }
    },
    // 搜索列表显示的名称处理
    getDisplayName(item) {
      if (item.type === TYPE_SINGER) {
        return item.singername;
      } else {
        return `${item.name}-${item.singer}`;
      }
    },
    // 上拉刷新 搜索更多
    searchMore() {
      if (!this.hasMore) {
        return;
      }
      this.page++;
      search(this.query, this.page, this.showSinger, perpage).then(res => {
        if (res.data.code === ERR_OK) {
          // 向结果添加
          this.result = this.result.concat(this._genResult(res.data.data));
          this._checkMore(res.data.data);
        }
      });
    },
    listScroll() {
      this.$emit("listScroll");
    },
    // 搜索列表点击事件
    selectItem(item) {
      console.log(item);

      if (item.type === TYPE_SINGER) {
        const singer = new Singer({
          id: item.singermid,
          name: item.singername
        });
        this.$router.push({
          path: `/search/${singer.id}`
        });
        this.setSinger(singer);
      } else {
        this.insertSong(item);
      }
      this.$emit("select", item);
    },
    ...mapMutations({
      setSinger: "SET_SINGER"
    }),
    ...mapActions(["insertSong"])
  },
  watch: {
    // 监听搜索词改变，请求服务器数据
    query(newQuery) {
      this.page = 1;
      this.hasMore = true;
      this.$refs.suggest.scrollTo(0, 0);
      this.search(newQuery);
    }
  },
  components: {
    Scroll,
    Loading,
    NoResult
  }
};
</script>

<style scoped lang="stylus" rel="stylesheet/stylus">
@import '~common/stylus/variable';
@import '~common/stylus/mixin';

.suggest {
  height: 100%;
  overflow: hidden;

  .suggest-list {
    padding: 0 30px;

    .suggest-item {
      display: flex;
      align-items: center;
      padding-bottom: 20px;
    }

    .icon {
      flex: 0 0 30px;
      width: 30px;

      [class^='icon-'] {
        font-size: 14px;
        color: $color-text-d;
      }
    }

    .name {
      flex: 1;
      font-size: $font-size-medium;
      color: $color-text-d;
      overflow: hidden;

      .text {
        no-wrap();
      }
    }
  }

  .no-result-wrapper {
    position: absolute;
    width: 100%;
    top: 50%;
    transform: translateY(-50%);
  }
}
</style>