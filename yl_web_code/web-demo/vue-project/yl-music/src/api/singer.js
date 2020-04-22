// 定义一些方法用来获取 歌手页面的数据
import jsonp from 'common/js/jsonp.js'
import axios from 'axios'
import {
  commonParams,
  options
} from './config'

export function getSingerList() {
  const url = 'https://c.y.qq.com/v8/fcg-bin/v8.fcg'

  const data = Object.assign({}, commonParams, {
    channel: 'singer',
    page: 'list',
    key: 'all_all_all',
    pagesize: 100,
    pagenum: 1,
    hostUin: 0,
    needNewCode: 0,
    platform: 'yqq'
  })

  return jsonp(url, data, options)
}

export function getSingerDetail(singerMid) {
  const url = 'https://c.y.qq.com/v8/fcg-bin/fcg_v8_singer_track_cp.fcg'

  const data = Object.assign({}, commonParams, {
    hostUin: 0,
    needNewCode: 0,
    platform: 'yqq',
    order: 'listen',
    begin: 0,
    num: 80,
    songstatus: 1,
    singermid: singerMid,
    g_tk: 1928093487
  })

  return jsonp(url, data, options)
}

export function getRealSongUrl(songs) {
  const url = '/hehe/song/urls'

  let idStr = ''
  songs.forEach(song => {
    idStr = idStr + "," + song.mid 
  });
  
  return axios.get(url+'?id='+idStr.substr(1))
}