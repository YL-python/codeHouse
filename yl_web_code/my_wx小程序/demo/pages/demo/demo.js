Page({
  // tabbar上的页面会被缓存，不会被销毁
  onLoad(){
    console.log("页面 加载");
  },
  onunload(){
    console.log("页面 卸载");
  },
  // 会和全局的 onShow一起触发
  onShow(){
    console.log("页面 显示");
  },
  onHide(){
    console.log("页面 隐藏");
  },
  // 先加载，在显示，在渲染完成
  onReady(){
    console.log("页面 渲染完成");
  },
  data:{
    name: "haha",
    arr:[1,2,3,4],
    obj:{us:123,ps:456}
  },
  changeName(e){
    // console.log("点到我了",this);
    // this.data.name = "heiheihie"
    // console.log(this.data.name);
    this.setData({name:"heiheihei"})
    console.log(e);
    console.log(e.target);
    console.log(e.currentTarget);
    let {hehe, xixi} = e.target.dataset
  }
})