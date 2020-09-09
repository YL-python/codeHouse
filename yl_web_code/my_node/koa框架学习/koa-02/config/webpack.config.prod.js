// 生产模式下 webpack配置

const { merge } = require('webpack-merge')
const baseWebpackConfig = require('./webpack.config.base')
const terserWebpackPlugin = require('terser-webpack-plugin')

const webpackConfig = merge(baseWebpackConfig, {
  mode: 'production',
  stats: { children: false, warnings: false },
  optimization: {
    minimizer: [
      new terserWebpackPlugin({
        terserOptions: {
          warnings: false,
          compress: {
            warnings: false,
            drop_console: false,
            dead_code: true,
            drop_debugger: true,
          },
          output: {
            comments: false,
            beautify: false,
          },
          mangle: true,
        },
        parallel: true,
        sourceMap: false,
      }),
    ],
    splitChunks: {
      cacheGroups: {
        commons: {
          name: 'commons',
          chunks: 'initial',
          minChunks: 3,
          enforce: true,
        },
      },
    },
  },
})
module.exports = webpackConfig
