// 左上第一个柱形图
(function () {
  // 实例化对象
  let myChart = echarts.init(document.querySelector(".bar1 .chart"))
  // 指定配置项
  let option = {
    color: ['#2f89cf'],
    tooltip: {
      trigger: 'axis',
      axisPointer: { // 坐标轴指示器，坐标轴触发有效
        type: 'shadow' // 默认为直线，可选为：'line' | 'shadow'
      }
    },
    // 修改图标的位置  大小
    grid: {
      left: '0%',
      right: '0%',
      top: "10px",
      bottom: '4%',
      containLabel: true
    },
    xAxis: [{
      type: 'category',
      data: ["旅游行业", "教育培训", "游戏行业", "医疗行业", "电商行业", "社交行业", "金融行业"],
      axisTick: {
        alignWithLabel: true
      },
      // 修改 x轴刻度标签
      axisLabel: {
        color: "rgba(255,255,255,.6)",
        fontSize: 10
      },
      // x轴不显示
      axisLine: {
        show: false
      }
    }],
    yAxis: [{
      type: 'value',
      // 修改 y轴刻度标签
      axisLabel: {
        color: "rgba(255,255,255,.6)",
        fontSize: 10
      },
      // y轴样式修改
      axisLine: {
        lineStyle: {
          color: 'rgba(255,255,255,.1)'
        }
      },
      // y 轴分隔线样式
      splitLine: {
        lineStyle: {
          color: "rgba(255,255,255,.1)"
        }
      }
    }],
    series: [{
      name: '直接访问',
      type: 'bar',
      barWidth: '35%',
      data: [200, 300, 300, 900, 1500, 1200, 600],
      itemStyle: {
        // 修改柱子圆角
        barBorderRadius: [5, 5, 0, 0]
      }
    }]
  };
  // 使用刚指定的配置项和数据显示图表。
  myChart.setOption(option);
  // 让图表跟随屏幕自动的去适应
  window.addEventListener("resize", function () {
    myChart.resize();
  });
})();

// 右上第一个柱形图
(function () {
  // 实例化对象
  let myChart = echarts.init(document.querySelector(".bar2 .chart"))
  let myColor = ["#1089E7", "#F57474", "#56D0E3", "#F8B448", "#8B78F6"];
  // 指定配置项
  let option = {
    // 图标位置
    grid: {
      top: "10%",
      left: "22%",
      bottom: "10%",
      // containLabel: true
    },
    xAxis: {
      show: false
    },
    yAxis: [{
      type: 'category',
      data: ["HTML5", "CSS3", "javascript", "VUE", "NODE"],
      //不显示y轴线条
      inverse: true,
      axisLine: {
        show: false
      },
      // 不显示刻度
      axisTick: {
        show: false
      },
      axisLabel: {
        color: "#fff",
        fontSize: 10
      }
    }, {
      type: 'category',
      data: [702, 350, 610, 793, 664],
      //不显示y轴线条
      axisLine: {
        show: false
      },
      // 不显示刻度
      axisTick: {
        show: false
      },
      axisLabel: {
        color: "#fff",
        fontSize: 10
      }
    }],
    series: [{
        name: '条',
        type: 'bar',
        data: [70, 34, 60, 78, 69],
        // 柱子之间的距离
        barCategoryGap: 50,
        //柱子的宽度
        barWidth: 10,
        // 柱子设为圆角
        itemStyle: {
          barBorderRadius: 20,
          color: function (seriesIndex) {
            return myColor[seriesIndex.dataIndex]
          }
        },
        // 图形上的文本标签
        label: {
          show: true,
          // 图形内显示
          position: "inside",
          // 文字的显示格式
          formatter: "{c}%"
        },
        yAxisIndex: 0,
      },
      {
        name: '框',
        type: "bar",
        barCategoryGap: 50,
        barWidth: 15,
        itemStyle: {
          color: "none",
          borderColor: "#00c1de",
          borderWidth: 3,
          barBorderRadius: 15
        },
        data: [100, 100, 100, 100, 100],
        yAxisIndex: 1
      }
    ]
  };

  // 使用刚指定的配置项和数据显示图表。
  myChart.setOption(option);
  // 让图表跟随屏幕自动的去适应
  window.addEventListener("resize", function () {
    myChart.resize();
  });
})();