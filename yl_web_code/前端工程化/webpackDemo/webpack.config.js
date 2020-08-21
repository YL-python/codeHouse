const path = require('path');
const webpack = require('webpack');
const HtmlWebpackPlugin = require('html-webpack-plugin'); // 打包文件夹生成html页面
const {
  CleanWebpackPlugin
} = require('clean-webpack-plugin'); // 清除打包后文件夹内多余的文件
const CopyWebpackPlugin = require('copy-webpack-plugin'); // 复制文件到打包的目录
const MiniCssExtractPlugin = require('mini-css-extract-plugin'); // 提取css为单独文件
const TerserJSPlugin = require('terser-webpack-plugin'); // 压缩js
const OptimizeCssAssetsPlugin = require('optimize-css-assets-webpack-plugin'); // 压缩css

const config = {
  mode: 'development', // production
  entry: "./src/index.js", // 配置入口文件
  optimization: {
    minimizer: [new TerserJSPlugin({}), new OptimizeCssAssetsPlugin({})]
  },
  output: { // 配置输出
    path: path.join(__dirname, 'dist_1'), // 输出路径
    filename: 'bundle.js' // 输出文件名称
  },
  module: {
    rules: [{
      test: /\.(scss|sass)$/,
      use: [MiniCssExtractPlugin.loader, 'css-loader', 'sass-loader'] // 使用多个loader时，从后往前链式执行
    }, {
      test: /\.(png|svg|jpg|gif)$/,
      use: ['file-loader']
    }, {
      test: /\.(woff|woff2|eot|ttf|otf)$/,
      use: ['file-loader']
    }, {
      test: /\.js$/,
      use: ['babel-loader']
    }]
  },
  plugins: [
    new HtmlWebpackPlugin({
      filename: "out.html",
      template: "template.html"
    }),
    new webpack.HotModuleReplacementPlugin(),
    new CleanWebpackPlugin(),
    new CopyWebpackPlugin({
      patterns: [{
        from: path.join(__dirname, 'assets'),
        to: 'assets'
      }]
    }),
    new MiniCssExtractPlugin({
      filename: '[name].css',
      chunkFilename: '[id].css'
    })
  ],
  devServer: { // 热部署 和 package.json  的 hot指令一起使用
    hot: true,
    contentBase: './dist_1'
  },
}

module.exports = config