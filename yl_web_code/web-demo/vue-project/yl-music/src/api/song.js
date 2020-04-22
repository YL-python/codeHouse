import axios from 'axios'


export function getLyric(mid) {
  const url = `/xixi/music/api/lyric?g_tk=1928093487&inCharset=utf-8&outCharset=utf-8&notice=0&format=json&songmid=${mid}&platform=yqq&hostUin=0&needNewCode=0&categoryId=10000000&pcachetime=1587471333392`

  return axios.get(url)
}