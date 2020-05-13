<template>
  <div class="view">
    router-view  根据地址栏的改变切换组件
    <component :is="componentId"></component>
  </div>
</template>

<script>
import Recommend from '../components/Recommend'
import Singer from '../components/Singer'
import Rank from '../components/Rank'

export default {
  components:{
    Recommend,
    Singer,
    Rank
  },
  data() {
    return {
      componentId:''
    }
  },
  created(){
    // 监听地址栏的改变
    window.addEventListener('hashchange',()=>{
      console.log("hash值改变了",window.location.hash);
      const hash = window.location.hash.split('#')[1]
      // 创建路由表
      const routs = [
        {path:'/recommend',component:'Recommend'},
        {path:'/singer',component:'Singer'},
        {path:'/rank',component:'Rank'}
      ]
      // 进行匹配
      routs.map((item,index)=>{
        if(item.path === hash){
          this.componentId = item.component
        }
        return item
      })
    })
  }
}
</script>
<style>
</style>
