class Compile extends EventTarget {
  constructor(options) {
    super();
    this.$options = options;
    this.compile();
  }
  compile() {
    let el = document.querySelector(this.$options.el);
    this.compileNode(el);
  }
  compileNode(el) {
    let childNodes = el.childNodes;
    console.log(childNodes);
    childNodes.forEach((node) => {
      if (node.nodeType === 1) {
        // 标签
        let attrs = node.attributes;
        // console.log(attrs)
        [...attrs].forEach((attr) => {
          // console.log(attr)
          let attrName = attr.name;
          let attrValue = attr.value;
          if (attrName.indexOf('v-') === 0) {
            attrName = attrName.substr(2);
            // console.log(attrName);
            if (attrName === 'html') {
              node.innerHTML = this.$options.data[attrValue];
            } else if (attrName === 'model') {
              node.value = this.$options.data[attrValue];
              node.addEventListener('input', (e) => {
                // console.log(e.target.value);
                this.$options.data[attrValue] = e.target.value;
              });
            }
          }
        });

        if (node.childNodes.length > 0) {
          this.compileNode(node);
        }
      } else if (node.nodeType === 3) {
        //文本节点
        let reg = /\{\{\s*(\S+)\s*\}\}/g;
        let textContent = node.textContent;
        if (reg.test(textContent)) {
          // console.log("存在双花括号");
          // console.log(RegExp.$2)
          let $1 = RegExp.$1;
          // node.textContent = this.$options.data[$1];
          node.textContent = node.textContent.replace(reg, this.$options.data[$1]);
          this.addEventListener($1, (e) => {
            console.log(e.detail);
            // console.log("触发了修改..");
            // 重新渲染视图；
            // console.log(this.$options.data[$1]);
            let oldValue = this.$options.data[$1];
            // let reg = /oldValue/g
            let reg = new RegExp(oldValue);
            node.textContent = node.textContent.replace(reg, e.detail);
          });
        }
      }
    });
  }
}

export default Compile;
