const path = require('path')
function resolve (dir) {
  return path.join(__dirname, dir)
}
module.exports = {
  lintOnSave: true, // eslint开启
  devServer: {
    proxy: { // 配置代理服务器
      '/xixi': {
        target: 'http://ustbhuangyi.com', // 要转发的目标网址目标网址
        changeOrigin: true,  // 是否跨域
        pathRewrite: {
          '^/xixi': '' // 将路径中多余的暗号 删除
        }
      },
      '/hehe': {
        target: 'https://api.qq.jsososo.com', // 要转发的目标网址目标网址
        changeOrigin: true,  // 是否跨域
        pathRewrite: {
          '^/hehe': '' // 将路径中多余的暗号 删除
        }
      }
    }
  },
  chainWebpack: (config) => {
    config.resolve.alias
      .set('@', resolve('./src')) // src的绝对路径起一个别名叫@
      .set('common', resolve('./src/common'))
      .set('components', resolve('./src/components'))
      .set('router', resolve('./src/router'))
      .set('store', resolve('./src/store'))
      .set('api', resolve('./src/api'))
      .set('base', resolve('./src/base'))
  }
}
