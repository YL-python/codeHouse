import axios from 'axios'

// 请求拦截器  发起请求前对请求参数做拦截处理
axios.interceptors.request.use(function (config) {
  // Do something before request is sent
  return config
}, function (error) {
  // Do something with request error
  return Promise.reject(error)
})

// 响应拦截器  接受到数据的时候对数据进行处理
axios.interceptors.response.use(function (response) {
  // 做一个数据清洗的小拦截器
  return response.data
}, function (error) {
  return Promise.reject(error)
})

export default axios
