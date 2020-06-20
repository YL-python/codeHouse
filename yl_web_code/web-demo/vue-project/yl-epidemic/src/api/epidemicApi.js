import axios from "utils/axios";

const getData = () => {
  const url = 'http://coderyl.top/node/epidemic'
  return axios.get(url)
}

export {
  getData
}