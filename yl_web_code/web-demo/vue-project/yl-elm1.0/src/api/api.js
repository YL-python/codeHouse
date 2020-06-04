import axios from "utils/axios";

const getGoods = () => {
  const url = 'http://coderyl.top/node2/elm/goods'
  return axios.get(url)
}

const getRatings = () => {
  const url = 'http://coderyl.top/node2/elm/ratings'
  return axios.get(url)
}

const getSeller = () => {
  const url = 'http://coderyl.top/node2/elm/seller'
  return axios.get(url)
}

export {
  getGoods,
  getRatings,
  getSeller
}