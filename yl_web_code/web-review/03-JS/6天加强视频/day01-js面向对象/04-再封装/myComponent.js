var r = /([a-z])([A-Z])/g;

function parse(str) {
  return str.replace(r, function (_, g1, g2) {
    return g1 + '-' + g2.toLowerCase(); // vue 源码中的实现
  });
}

var r1 = /\{\{\s*(.+?)\s*\}\}/g;
var r2 = /:(\w+)="(\w+)"/g;
var r3 = /:style="(\w+)"/g;

function MyComponent(opts) {
  this.opts = opts;

  this.init();

  this.render();
}

MyComponent.prototype.init = function () {
  // 就是需要给 this 添加属性, data 里面同名的属性, 该属性需要具备 get 与 set
  var data = this.opts.data;
  var that = this;
  for (var k in data) {
    (function (value) {
      Object.defineProperty(that, k, {
        get() {
          return value;
        },
        set(val) {
          value = val;
          that.render(); // this 的 意译
        }
      });

      // 修改data数据，因为render()的时候使用的的data里面的数据
      Object.defineProperty(that.opts.data, k, {
        get() {
          return value;
        },
        set(val) {
          value = val;
          that.render(); // this 的 意译
        }
      });
    })(data[k]);
  }
};


MyComponent.prototype.render = function () {
  var opts = this.opts;

  var template = opts.template;
  template = template.replace(r1, function (match, propName) {
    return opts.data[propName];
  });
  template = template.replace(r3, function (_, cssObj) {
    var style = opts.data[cssObj];
    var _temp = [];
    for (var k in style) {
      _temp.push(parse(k) + ": " + style[k]);
    }
    return 'style="' + _temp.join(';') + ';"';
  });
  // 处理属性
  template = template.replace(r2, function (_, attrName, propName) {
    return attrName + '="' + opts.data[propName] + '"';
  });
  // 2. 找到容器元素
  var root = document.querySelector(opts.el);
  // 3. 使用 innerHTML
  root.innerHTML = template;
};

// 在 给 p.name 赋值的时候应该得到什么效果?
// 只要赋值 就需要 重新渲染页面