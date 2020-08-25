// 引入用户信息文件
const userList = require("./userList.js")
const schedule = require("node-schedule");
const request = require("request")
const Mail = require('./mail')

// 封装数据
function dayData(day, res_day) {
    day.time = res_day.time;
    day.day_weather = res_day.day_weather;
    day.night_weather = res_day.night_weather;
    day.max_degree = res_day.max_degree;
    day.min_degree = res_day.min_degree;
    day.day_weather_code = res_day.day_weather_code;
    day.night_weather_code = res_day.night_weather_code;
}

// 获取天气
function getWeather(address) {
    let { province, city, county } = address;
    WeatherUrl = "https://wis.qq.com/weather/common?source=pc&weather_type=forecast_24h&province=" + encodeURIComponent(province) + "&city=" + encodeURIComponent(city) + "&county=" + encodeURIComponent(county)
    return new Promise((resolve, reject) => {
        request(WeatherUrl, function (error, response, body) {
            console.log(response.statusCode);
            if (response.statusCode === 200) {
                let res = JSON.parse(body);
                resolve([res.data.forecast_24h['1'],res.data.forecast_24h['2'],res.data.forecast_24h['3']]);
            } else {
                reject("获取天气失败 接口出现问题");
            }
        });
    })
}

function getMailData(data,address) {
    let firstDay = {
        time: '',
        day_weather: "",
        night_weather: "",
        max_degree: '',
        min_degree: "",
        day_weather_code: "",
        night_weather_code: ''
    }
    let secondDay = {
        time: '',
        day_weather: "",
        night_weather: "",
        max_degree: '',
        min_degree: "",
        day_weather_code: "",
        night_weather_code: ''
    }
    let thirdDay = {
        time: '',
        day_weather: "",
        night_weather: "",
        max_degree: '',
        min_degree: "",
        day_weather_code: "",
        night_weather_code: ''
    }
    dayData(firstDay, data[0]);
    dayData(secondDay, data[1]);
    dayData(thirdDay, data[2]);
    return new Promise((resolve, reject) => {
        console.log(firstDay,address);
        if(firstDay.day_weather){
            let HTMLData = `<table width="400"border="1"style="width: 400px; background-color: #fff;"align="center"cellspacing="0"cellpadding="0"><tr style="height: 50px;"><td align="center"colspan="3">来自node服务器的每日定时天气信息</td><td align="center"colspan="1">${address.province}-${address.city}-${address.county}</td></tr><tr><td align="center"><span style="color: #384c78;">今天</span><br><span style="color: #8a9baf;">${firstDay.time}</span></td><td align="center">${firstDay.day_weather}转${firstDay.night_weather}<br>${firstDay.max_degree}°~${firstDay.min_degree}°</td><td align="center"><img src="http://mat1.gtimg.com/pingjs/ext2020/weather/pc/icon/weather/day/${firstDay.day_weather_code}.png"alt=""></td><td align="center"><img src="http://mat1.gtimg.com/pingjs/ext2020/weather/pc/icon/weather/night/${firstDay.night_weather_code}.png"alt=""></td></tr><tr><td align="center"><span style="color: #384c78;">明天</span><br><span style="color: #8a9baf;">${secondDay.time}</span></td><td align="center">${secondDay.day_weather}转${secondDay.night_weather}<br>${secondDay.max_degree}°~${secondDay.min_degree}°</td><td align="center"><img src="http://mat1.gtimg.com/pingjs/ext2020/weather/pc/icon/weather/day/${secondDay.day_weather_code}.png"alt=""></td><td align="center"><img src="http://mat1.gtimg.com/pingjs/ext2020/weather/pc/icon/weather/night/${secondDay.night_weather_code}.png"alt=""></td></tr><tr><td align="center"><span style="color: #384c78;">后天</span><br><span style="color: #8a9baf;">${thirdDay.time}</span></td><td align="center">${thirdDay.day_weather}转${thirdDay.night_weather}<br>${thirdDay.max_degree}°~${thirdDay.min_degree}°</td><td align="center"><img src="http://mat1.gtimg.com/pingjs/ext2020/weather/pc/icon/weather/day/${thirdDay.day_weather_code}.png"alt=""></td><td align="center"><img src="http://mat1.gtimg.com/pingjs/ext2020/weather/pc/icon/weather/night/${thirdDay.night_weather_code}.png"alt=""></td></tr><tr><td align="center"colspan="5">有疑问联系QQ：2336739721</td></tr></table>`
            resolve(HTMLData);
        }else{
            reject("封装数据  接口出现问题")
        }
    })
}

const scheduleCronstyle = () => {
    console.log('时间监听启动');
    schedule.scheduleJob('0 0 6 * * *', () => {
        let code = 1;
        for(var i=0;i<3;i++){
            let userAddress = userList[i].address;
            let userEmail = userList[i].email;
            getWeather(userAddress).then((data) => {
                return getMailData(data, userAddress)
            }).then((res) => {
                return Mail.send(userEmail, res)
            }).catch((err) => {
                let errData = '发生了错误，原因是：'+err+'<br> 将错误反馈管理员呀，qq:2336739721'
                Mail.send(userEmail, errData)
                Mail.send('2336739721@qq.com', '在第'+i+"位用户获取数据时发生下面问题："+err);
                code = 0;
            })
        }
        if(code == 1){
            Mail.send('2336739721@qq.com', '今天信息全部发送，没有出现问题');
            console.log(new Date() + '今天信息全部发送，没有出现问题');
        }else{
            console.log(new Date() + '今天的发送除了一点问题哦');
        }
    });
}

scheduleCronstyle();