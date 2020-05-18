var r = /([a-z])([A-Z])/g;

function parse(str) {
  return str.replace(r, function (_, g1, g2) {
    return g1 + '-' + g2.toLowerCase(); // vue 源码中的实现
  });
}

var r1 = /\{\{\s*(.+?)\s*\}\}/g;
var r2 = /:(\w+)="(\w+)"/g;
var r3 = /:style="(\w+)"/g;

function MyComponent(obj) {

  // 利用数据 替换模板，得到需要显示的HTML
  var template = obj.template;
  template = template.replace(r1, function (match, propName) {
    console.log(match, propName);
    return obj.data[propName]
  })

  // 处理样式
  template = template.replace(r3, function (_, cssObj) {
    // 返回形如: style="width: 100px; height: 200px; border: 1px solid blue;"
    var style = obj.data[cssObj]; // { backgroundColor: '...' }
    var _temp = [];
    for (var k in style) {
      _temp.push(parse(k) + ": " + style[k]);
    }
    return 'style="' + _temp.join(';') + ';"';
  });

  // 处理属性
  template = template.replace(r2, function (_, attrName, propName) {
    // 假如 attrName 为 title, 而 data 中提供 { title: '一个文本' }
    //      'title' + '="' + '一个文本' + '"'
    //      'title="一个文本"'
    return attrName + '="' + obj.data[propName] + '"';
  });

  // 2. 找到容器元素
  var root = document.querySelector(obj.el);

  // 3. 使用 innerHTML
  root.innerHTML = template;
}