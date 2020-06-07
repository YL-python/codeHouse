const path = require('path')

function resolve (dir) {
  return path.join(__dirname, dir)
}

module.exports = {
  lintOnSave: true, // 开启eslint
  chainWebpack: (config) => {
    config.resolve.alias
      .set('@', resolve('./src')) // src的绝对路径起一个别名叫@
      .set('components', resolve('./src/components'))
      .set('api', resolve('./src/api'))
      .set('common', resolve('./src/common'))
      .set('utils', resolve('./src/utils'))
      .set('views', resolve('./src/views'))
  }
}