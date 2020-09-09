const windMap = {
	"0": "无持续风向",
	"1": "东北风",
	"2": "东风",
	"3": "东南风",
	"4": "南风",
	"5": "西南风",
	"6": "西风",
	"7": "西北风",
	"8": "北风",
	"9": "旋转风"
};

const weekObj = {
	"0": "星期日",
	"1": "星期一",
	"2": "星期二",
	"3": "星期三",
	"4": "星期四",
	"5": "星期五",
	"6": "星期六"
}

const dayUrl = "http://mat1.gtimg.com/pingjs/ext2020/weather/mobile2.0/assets/weather/day/weather_code.svg"
const nightUrl = "http://mat1.gtimg.com/pingjs/ext2020/weather/mobile2.0/assets/weather/night/weather_code.svg"

// 首页需要的数据太多了  单独写一个函数来处理
function formatData(data) {
	makeimgUrl(data)
	// 需要一个当前天气 --> nowWeather
	let nowWeather = formatNowWeather(data)
	// 需要未来七天的数据 --> future7d
	let future7d = formatfuture7d(data)
	// 需要未来48小时的数据 --> future48h
	let future48h = data.forecast_1h
	// 需要生活小贴士的数据 --> t
	return {
		nowWeather,
		future48h,
		future7d
	}
}

function makeimgUrl(obj) {
	for (let key in obj) {
		if (typeof obj[key] === 'object') {
			makeimgUrl(obj[key])
		} else {
			if (key === 'weather_code' || key === 'day_weather_code') {
				obj[key] = dayUrl.replace("weather_code", obj[key])
			} else if (key === 'night_weather_code') {
				obj[key] = nightUrl.replace("weather_code", obj[key])
			}
		}
	}
}

function formatNowWeather(data) {
	let res = {
		"environment": {
			"aqi": {},
			"humidity": {},
			"wind": {}
		},
		"time": {
			"date": "",
			"time": "",
			"uptime": ""
		},
		"weather": {},
		"tips": []

	}
	// 环境质量 需要 空气质量 湿度 风向风力
	res.environment.aqi.level = data.air.aqi_name
	res.environment.aqi.num = data.air.aqi
	res.environment.humidity.level = data.observe.humidity
	res.environment.wind.direction = windMap[data.observe.wind_direction]
	res.environment.wind.level = data.observe.wind_power

	// 时间
	res.time.date = formatDate(data.observe.update_time, "1")
	res.time.time = formatDate(data.observe.update_time, "3")
	res.time.uptime = formatDate(data.observe.update_time, "2")

	// 当前天气
	res.weather.img = data.observe.weather_code
	res.weather.degree = data.observe.degree
	res.weather.text =
		`${data.forecast_24h["1"].day_weather}转${data.forecast_24h["1"].night_weather}  ${data.forecast_24h["1"].min_degree}~${data.forecast_24h["1"].max_degree}℃`

	// 提示文字
	res.tips = Object.values(data.tips.observe)
	return res
}

function formatfuture7d(data) {
	let res = data.forecast_24h
	for (let day in res) {
		for (let key in res[day]) {
			if (key === 'time') {
				res[day][key] = formatDate2(res[day][key])
			}
		}
	}

	res["0"].time.week = '昨天'
	res["1"].time.week = '今天'
	res["2"].time.week = '明天'
	res["3"].time.week = '后天'
	return res
}

function formatDate2(dateStr) {
	// 传入  2020-07-06  返回对象 包括日期和  07/06 的时间数据
	let res = {}
	let month = dateStr.slice(5, 7)
	let day = dateStr.slice(8, 10)
	res.date = `${month}/${day}`
	res.week = weekObj[new Date(dateStr).getDay()].replace("星期", "周")
	return res
}

function formatDate(dateStr, type) {
	if (!dateStr) return
	let year = dateStr.slice(0, 4)
	let month = dateStr.slice(4, 6)
	let day = dateStr.slice(6, 8)
	let hours = dateStr.slice(8, 10)
	let minutes = dateStr.slice(10, 12)

	let date = `${year}年${month}月${day}日`;
	let time = `${hours}:${minutes}`;
	let week = weekObj[new Date(`${year}-${month}-${day}`).getDay()]
	switch (type) {
		case "1":
			return date
			break;
		case "2":
			return time
			break;
		case "3":
			return week
			break;
	}
}

export default formatData
