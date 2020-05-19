<template>
  <div>
    <h1>这里是 less 样式的案例</h1>
    <hr>
    <div class="demo">

    </div>
    <div class="test">
      <p>2
        <span>
          2
        </span>
      </p>
    </div>
  </div>
</template>
<script>
export default {

}
</script>
<style lang="less" scoped >
@import '../../../style/index.less';
  // lang 语言  scoped作用域表示只能在当前组件或者子组件中生效
  // 用@ 声明变量
  @color:green;
  @width:100px;
  // 简单计算
  @height:@width * 2;
  // mixin 混合，css的函数，对样式进行封装
  .hehe(@borderColor){
    border: 2px @borderColor solid;
    border-radius: 30px;
  }
  .test{
    background: @color;
    width: @width;
    height: @height;
    .hehe(black);
    // 嵌套封装
    p {
      background:yellow;
      height: 40px;
      span{
        display: inline-block;
        height: 20px;
        width: 20px;
        background:red;
      }
    }
  }
  .demo{
    // width: 5rem;
    .w(187.5);
    height: 100px;
    background: pink;
  }
</style>
