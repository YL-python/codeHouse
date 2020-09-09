// 开发模式下 webpack配置

const { merge } = require('webpack-merge')
const baseWebpackConfig = require('./webpack.config.base')

const webpackConfig = {
  mode: 'development',
  devtool: 'eval-source-map',
  status: { children: false },
}
module.exports = merge(baseWebpackConfig, webpackConfig)
