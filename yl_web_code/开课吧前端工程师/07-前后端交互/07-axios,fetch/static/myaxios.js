//1. 混入模式；2.拦截器； 3、适配器；
let util = {
  extends(a, b, context) {
    for (let key in b) {
      if (b.hasOwnProperty(key)) {
        if (typeof b[key] === 'function') {
          a[key] = b[key].bind(context);
        } else {
          // console.log()
          a[key] = b[key];
        }
      }
    }
  },
};

class Axios {
  constructor() {
    // this.mytest = "你好";
    this.Intercepters = {
      request: new IntercepterManager(),
      response: new IntercepterManager(),
    };
  }
  // get(){}
  // post(){}
  request(config) {
    let chain = [this.xhr, undefined];
    console.log(this.Intercepters.request.handles);
    this.Intercepters.request.handles.forEach((Intercepter) => {
      chain.unshift(Intercepter.fulfilled, Intercepter.reject);
    });
    this.Intercepters.response.handles.forEach((Intercepter) => {
      chain.push(Intercepter.fulfilled, Intercepter.reject);
    });
    let promise = Promise.resolve(config);
    // ['fulfilled1','reject1','fulfilled2','reject2','this.xhr','undefined','fulfilled2','reject2','fulfilled1','reject1']
    // promise.then()
    console.log(chain);
    while (chain.length > 0) {
      promise = promise.then(chain.shift(), chain.shift());
    }
    return promise;
  }
  xhr(config) {
    return new Promise((resolve) => {
      // this.intercepters;
      // 发送请求
      let xhr = new XMLHttpRequest();
      // 合并配置；
      let { url = '', data = null, method = 'get', headers = {} } = config;
      xhr.open(method, url, true);
      xhr.onload = function () {
        // console.log(xhr.responseText);
        resolve(xhr.responseText);
      };
      xhr.send(data);
    });
  }
}

//拦截器管理器；
class IntercepterManager {
  constructor() {
    this.handles = [];
  }
  use(fulfilled, reject) {
    this.handles.push({ fulfilled, reject });
  }
}

let methodArr = ['get', 'post', 'put', 'delete', 'options', 'patch'];
methodArr.forEach((method) => {
  Axios.prototype[method] = function (url, data = null) {
    let config = { method, url, data };
    // console.log(config);
    return this.request(config);
  };
});

// console.dir(Axios);

function createInstance() {
  let context = new Axios();
  let Instance = context.request.bind(context); //request函数；
  // console.dir(Instance);
  // 混入方法；
  util.extends(Instance, Axios.prototype, context);
  // 混入实例对象的属性
  util.extends(Instance, context);
  // 把类的prototype上的方法混入（扩展）到Instance；
  console.dir(Instance);
  return Instance;
}
let axios = createInstance();
// console.log(axios);
// axios()
