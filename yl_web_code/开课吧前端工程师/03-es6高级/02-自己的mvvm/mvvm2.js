class MyVue extends EventTarget {
  constructor(options) {
    super();
    this.$options = options;
    this.compile();
    this.observe();
  }
  observe() {
    let _this = this;
    this.$options.data = new Proxy(this.$options.data, {
      get(target, key) {
        return target[key];
      },
      set(target, key, newValue) {
        let event = new CustomEvent(key, {
          detail: newValue,
        });
        _this.dispatchEvent(event);
        target[key] = newValue;
        return true;
      },
    });
  }
  compile() {
    let el = document.querySelector(this.$options.el);
    this.compileNode(el);
  }
  compileNode(el) {
    let childNodes = el.childNodes;
    childNodes.forEach((node) => {
      if (node.nodeType === 1) {
        // 标签
        let attrs = node.attributes;
        [...attrs].forEach((attr) => {
          // console.log(attr);
          let attrName = attr.name;
          let attrValue = attr.value;
          if (attrName.indexOf('v-') === 0) {
            attrName = attrName.substr(2);
            if (attrName === 'html') {
              node.innerHTML = this.$options.data[attrValue];
            } else if (attrName === 'model') {
              node.value = this.$options.data[attrValue];
              node.addEventListener('input', (e) => {
                this.$options.data[attrValue] = e.target.value;
              });
            }
          }
        });
        this.compileNode(node);
      } else if (node.nodeType === 3) {
        // 文本
        let reg = /\{\{\s*(\S+)\s*\}\}/g;
        if (reg.test(node.textContent)) {
          // console.log(RegExp.$1)
          let $1 = RegExp.$1;
          node.textContent = node.textContent.replace(reg, this.$options.data[$1]);
          this.addEventListener($1, (e) => {
            // console.log(e.detail);
            let oldValue = this.$options.data[$1];
            let reg = new RegExp(oldValue);
            node.textContent = node.textContent.replace(reg, e.detail);
          });
        }
      }
    });
  }
}
