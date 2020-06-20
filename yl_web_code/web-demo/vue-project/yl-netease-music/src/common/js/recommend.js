// 关于推荐页的所有请求方法都会写在这里
import axios from './axiosutil'
import API from './APIconfig'

// 获取推荐页面的轮播图数据
const getBannerData = () => {
  return axios.get(API.banner)
}

export {
  getBannerData
}