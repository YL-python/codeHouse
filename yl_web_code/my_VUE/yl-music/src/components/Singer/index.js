// 处理数据
function nomalData (data) {
  // console.log(data)
  const obj = { hot: [] }
  // 数据分组
  for (let index = 0; index < data.length; index++) {
    const { Findex, Fother_name, Fsinger_mid, Fsinger_name } = data[index]
    const avator = `https://y.gtimg.cn/music/photo_new/T001R300x300M000${Fsinger_mid}.jpg?max_age=2592000`
    const temp = { Findex, Fother_name, Fsinger_name, avator, Fsinger_mid }
    if (index <= 9) {
      obj.hot.push(temp)
    }
    if (!obj[Findex]) {
      // 新建一个
      obj[Findex] = [temp]
    } else {
      // 添加一个
      obj[Findex].push(temp)
    }
  }
  // 对象变数组，为了排序
  const hot = []
  const other = []
  for (const key in obj) {
    if (key === 'hot') {
      hot.push({ Findex: '热', list: obj[key] })
    } else if (key !== '9') {
      other.push({ Findex: key, list: obj[key] })
    }
  }
  const rank = other.sort((a, b) => {
    return a.Findex.charCodeAt() - b.Findex.charCodeAt()
  })
  const result = hot.concat(rank)
  // console.log(result)
  return result
}

export {
  nomalData
}
