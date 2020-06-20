<template>
  <header>
    <h3>新型冠状病毒肺炎</h3>
    <h1>疫情实时大数据报告</h1>
  </header>
</template>
<script>
export default {};
</script>
<style scoped lang='less'>
header {
  height: 189px;
  background-image: url("../../assets/images/bg.png");
  background-size: 695px 189px;
  background-position: 50% 50%;
  background-repeat: no-repeat;
  margin-bottom: -0.625rem;

  h3 {
    display: inline-block;
    // margin-top 头部传递
    margin-top: 71px;
    margin-left: 17px;
    font-size: 14px;
    color: #c4faff;
  }
  h1 {
    margin-top: 10px;
    font-size: 32px;
    height: 32px;
    line-height: 32px;
    position: relative;
    padding-left: 17px;
    font-weight: 700;
    color: #fff;

    &::after {
      content: "疫情实时大数据报告";
      display: block;
      position: absolute;
      color: #afdade;
      top: 0;
      -webkit-mask-image: -webkit-gradient(
        linear,
        0 0,
        0 bottom,
        from(rgba(0, 0, 255, 0)),
        to(#afdade)
      );
      mask-image: -webkit-gradient(
        linear,
        0 0,
        0 bottom,
        from(rgba(0, 0, 255, 0)),
        to(#afdade)
      );
    }
  }
}
</style>