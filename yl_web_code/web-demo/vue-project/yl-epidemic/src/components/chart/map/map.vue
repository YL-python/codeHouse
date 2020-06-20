<template>
  <div class="chart-map">
    <div class="chart"></div>
  </div>
</template>
<script>
import echarts from "../echarts";
export default {
  props: {
    mapType: {
      type: String,
      default: "china"
    },
    mapData: {
      type: Array,
      default: () => {
        return null;
      }
    }
  },
  data() {
    return {
      myChart: null,
      option: {
        legend: {
          formatter: function(name) {
            return "Legend " + name;
          }
        },
        tooltip: {
          trigger: "item",
          triggerOn: "click",
          enterable: true,
          formatter: e => {
            console.log("e", e);
            return (
              "地区：" +
              e.name +
              "<br />" +
              "确诊：" +
              e.value +
              '<div class="tooltipLink" href="www.baidu.com">查看详情</div>'
            );
          }
        },
        visualMap: {
          type: "piecewise",
          itemWidth: 10,
          itemHeight: 10,
          itemGap: 3,
          textGap: 5,
          left: "10%",
          bottom: "10%",
          textStyle: {
            color: "#333",
            fontSize: 8
          },
          pieces: [
            {
              gte: 10000,
              label: ">=10000",
              color: "#B80909"
            },
            {
              gte: 1000,
              lt: 10000,
              label: "1000-9999",
              color: "#E64546"
            },
            {
              gte: 100,
              lt: 1000,
              label: "100-999",
              color: "#F57567"
            },
            {
              gte: 10,
              lt: 100,
              label: "10-99",
              color: "#FF9985"
            },
            {
              gte: 1,
              lt: 10,
              label: "1-9",
              color: "#FFE5DB"
            },
            {
              value: 0,
              color: "#ffffff",
              label: "0"
            }
          ]
        },
        series: [
          {
            type: "map",
            mapType: "china",
            roam: false,
            zoom: 1.2,
            label: {
              show: true,
              color: "rgb(0, 0, 0)",
              fontSize: 10,
              formatter: function(series) {
                series.name = series.name.replace("市", "");
                return series.name ;
              }
            },
            itemStyle: {
              emphasis: {
                areaColor: "rgb(199,255,253)"
              }
            }
          }
        ]
      }
    };
  },
  created() {
    if (this.mapType) {
      this.option.series[0].mapType = this.mapType;
    } else {
      this.option.series[0].mapType = "china";
    }
    if (this.mapData) {
      this.option.series[0].data = this.mapData;
    }

    console.log("this.option.series[0].mapType", this.option.series[0].mapType);
    console.log("this.option.series[0].data", this.option.series[0].data);
    // console.log(this.mapType);
  },
  mounted() {
    this.drowMap();
  },
  methods: {
    drowMap() {
      this.myChart = echarts.init(document.querySelector(".chart"));
      this.myChart.setOption(this.option);
      console.log("this.machart.getMap", this.myChart.getOption());
      window.addEventListener("resize", () => {
        if (this.myChart) {
          this.myChart.resize();
        }
      });
    }
  },
  watch: {
    mapType: val => {
      this.option.series[0].mapType = val;
      console.log(this.option.series[0].mapType);
    }
  }
};
</script>
<style scoped lang='less'>
.chart-map {
  height: 561px;
  max-width: 734px;
  background-color: #f8f9fa;
  margin-top: 1rem;
  margin-bottom: 0.625rem;
  .chart {
    width: 100%;
    height: 100%;
  }
}
</style>