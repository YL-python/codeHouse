// pages/my/my.js
Page({
  // 下拉加载
  onPullDownRefresh(){
    console.log("下拉");
  },
  // 上拉刷新
  // 页面高度没有满屏的时候上拉不会触发
  onReachBottom(){
    console.log("上拉");
  }
})