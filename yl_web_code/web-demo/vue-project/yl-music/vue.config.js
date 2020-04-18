module.exports = {
  devServer: {
    proxy: { // 配置代理服务器
      // 接口小暗号
      '/xixi': {
        target: 'http://ustbhuangyi.com', // 要转发的目标网址目标网址
        changeOrigin: true,  // 是否跨域
        pathRewrite: {
          '^/xixi': '/' // 重写路径
        }
      },
      // 接口小暗号
      '/hehe': {
        target: 'https://www.mxnzp.com', // 要转发的目标网址目标网址
        changeOrigin: true,  // 是否跨域
        pathRewrite: {
          '^/hehe': '' // 重写路径
        }
      }
    }
  }
}
