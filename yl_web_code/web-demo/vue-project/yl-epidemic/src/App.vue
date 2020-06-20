<template>
  <div id="app">
    <mHeader></mHeader>
    <div class="content">
      <div class="tab">
        <router-link to="/domestic?showMap=china" active-class="active">国内疫情</router-link>
        <router-link to="/foreign" active-class="active">国外疫情</router-link>
        <router-link to="/information" active-class="active">疫情资讯</router-link>
      </div>
      <router-view v-if="flag" :epidemic='epidemicData'></router-view>
      <loading v-if="!flag"></loading>
    </div>
  </div>
</template>
<script>
import mHeader from "./views/mHeader/m-header";
import loading from "./components/loading/loading";
import { getData } from "api/epidemicApi";
const STATUS = 0
export default {
  created() {
    this._getData();
  },
  data() {
    return {
      epidemicData:{},
      flag:false
    }
  },
  methods: {
    _getData() {
      getData().then((res)=>{
        if(res.status === STATUS){
          this.epidemicData = res.data
          console.log(this.epidemicData);
          this.flag = true
        }
      })
    }
  },
  components: {
    mHeader,
    loading
  }
};
</script>
<style lang="less" scoped>
#app {
  margin: 0 auto;
  max-width: 768px;
}
.content {
  display: flex;
  flex-direction: column;
  background-color: #fff;
  position: relative;
  border-radius: 0.625rem;
  padding: 0.917rem 1.0625rem 1.875rem;
  .tab {
    display: flex;
    justify-content: space-around;
    border-bottom: 1px solid #f5f6f7;
    a {
      font-size: 16px;
      height: 2.1rem;
      &.active {
        color: #10aeb5;
        font-weight: 700;
        border-bottom: 3px solid #10aeb5;
      }
    }
  }
}

// @media screen and (max-width: 768px) {
//   #app {
//     display: flex;
//     flex-direction: column;
//   }
// }
</style>