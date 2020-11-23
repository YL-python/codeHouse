import Compile from './Compile.js';
class Kvue {
  constructor(options) {
    // super();
    this.$options = options;
    // this.compile();
    this.compile = new Compile(options);
    this.observe(this.$options.data);
  }
  observe(data) {
    let _this = this;
    this.$options.data = new Proxy(data, {
      get(target, key) {
        return target[key];
      },
      set(target, key, newValue) {
        let event = new CustomEvent(key, {
          detail: newValue,
        });
        _this.compile.dispatchEvent(event);
        target[key] = newValue;
        return true;
      },
    });
  }
}

export default Kvue;
