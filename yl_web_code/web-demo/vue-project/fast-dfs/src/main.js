import Vue from 'vue'
import App from './App.vue'
import router from './router'
import store from './store'

//运行环境
var baseurl = "http://106.15.248.223:80/netdisk-web-perpc/";
var socketurl = "106.15.248.223:80/netdisk-service-provider";
var uploadurl = "http://106.15.248.223:80/disk";
Vue.prototype.baseurl = baseurl; //后台接口
Vue.prototype.socketurl = socketurl; //socket服务器
Vue.prototype.uploadurl = uploadurl; // 图片上传接口

// ElementUI
import ElementUI from 'element-ui';
import 'element-ui/lib/theme-chalk/index.css';
Vue.use(ElementUI);

// alertMsg 和 sessionStorage
import utils from '@/assets/js/utils.js'
Vue.use(utils);

// 公共样式
import './assets/css/common.css'
import './styles/normalize.css'

// 吧axios挂载到原型上，形成一个全局变量
import axios from './assets/js/axios'
Vue.prototype.$axios = axios

Vue.config.productionTip = false

new Vue({
  router,
  store,
  render: h => h(App)
}).$mount('#app')