# 疫情数据可视化

## 前端

技术： vue全家桶 + ECharts

前端页面需求：
国内

国外



## 数据格式的约定

```js
// 重要参数
// 数据更新时间
{   //    全国疫情数据
    confirm // 累计确诊
    heal    // 累计治愈
    dead   // 累计死亡
    nowConfirm // 现有确诊
    noInfect   // 无症状感染者
    importedCase  // 境外输入
}

{   //    与昨日比较  增加的
    confirm // 累计确诊
    heal    // 累计治愈
    dead   // 累计死亡
    nowConfirm // 现有确诊
    noInfect   // 无症状感染者
    importedCase  // 境外输入
}
```



## 后端

技术： node Express框架 + axioc 