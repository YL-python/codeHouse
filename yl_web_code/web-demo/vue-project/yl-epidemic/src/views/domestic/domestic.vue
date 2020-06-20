<template>
  <div class="domestic">
    <updataTime title="国内疫情" :updataTime="epidemic.mapLastUpdatedTime"></updataTime>
    <div class="show-list">
      <showData
        title="现有确诊"
        :data="epidemic.summaryDataIn.curConfirm"
        :subData="epidemic.summaryDataIn.curConfirmRelative"
      ></showData>
      <showData
        title="无症状"
        :data="epidemic.summaryDataIn.asymptomatic"
        :subData="epidemic.summaryDataIn.asymptomaticRelative"
      ></showData>
      <showData
        title="现有疑似"
        :data="epidemic.summaryDataIn.unconfirmed"
        :subData="epidemic.summaryDataIn.unconfirmedRelative"
      ></showData>
      <showData
        title="现有重症"
        :data="epidemic.summaryDataIn.icu"
        :subData="epidemic.summaryDataIn.icuRelative"
      ></showData>
    </div>
    <div class="show-list">
      <showData
        title="累计确诊"
        :data="epidemic.summaryDataIn.confirmed "
        :subData="epidemic.summaryDataIn.confirmedRelative"
      ></showData>
      <showData
        title="境外输入"
        :data="epidemic.summaryDataIn.overseasInput"
        :subData="epidemic.summaryDataIn.overseasInputRelative"
      ></showData>
      <showData
        title="累积治愈"
        :data="epidemic.summaryDataIn.cured"
        :subData="epidemic.summaryDataIn.curedRelative"
      ></showData>
      <showData
        title="累计死亡"
        :data="epidemic.summaryDataIn.died"
        :subData="epidemic.summaryDataIn.diedRelative"
      ></showData>
    </div>

    <mMap :mapType="showMap" :mapData="confirmedData"></mMap>
  </div>
</template>
<script>
import updataTime from "components/updataTime/updataTime";
import showData from "components/showData/showData";
import mMap from "../../components/chart/map/map";
// eslint-disable-next-line
import provinceMap from "./provinceMap";
import longNameCountryMap from "./longNameCountryMap";

export default {
  props: ["epidemic"],
  components: {
    updataTime,
    showData,
    mMap
  },
  data() {
    return {
      showMap: this.$route.query.showMap,
      // 现有确诊
      curConfirmData: [],
      // 累计确诊
      confirmedData: []
    };
  },
  created() {
    this._getAboutAllShowData(
      this.$route.query.showMap,
      this.epidemic.caseList
    );
  },
  methods: {
    _getAboutAllShowData(map, caseList) {
      console.log("map", map);
      console.log("caseList", caseList);
      if (!map || map === "china") {
        caseList.forEach(list => {
          let { area, curConfirm, confirmed } = list;
          area = this.formatCity(area);
          this.curConfirmData.push({ name: area, value: curConfirm });
          this.confirmedData.push({ name: area, value: confirmed });
        });
      } else {
        caseList.forEach(list => {
          if (list.area === map) {
            list.subList.forEach(sub => {
              let { city, curConfirm, confirmed } = sub;
              city = this.formatCity(city);
              this.curConfirmData.push({ name: city, value: curConfirm });
              this.confirmedData.push({ name: city, value: confirmed });
            });
          }
        });
      }
    },
    formatCity(city) {
      console.log(city);
      // 没有市没有区 的后面加市
      if (city.indexOf("市") === -1 && city.indexOf("区") === -1) {
        city += "市";
      }
      if (longNameCountryMap[city]) {
        city = longNameCountryMap[city];
      }
      return city;
    }
  },
  computed: {}
};
</script>
<style scoped lang='less'>
.show-list {
  display: flex;
  justify-content: space-around;
  margin-top: 1.25rem;
}
</style>