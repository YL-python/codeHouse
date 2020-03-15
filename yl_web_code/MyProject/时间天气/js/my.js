$(document).ready(function () {
    // 自定义地址，省 市 乡，没有值的时候会自动获取地理位置，精度不能保证！
    var province;  // 省份，自定义时必填例如：江西，北京。不需要写省
    var city;  // 市，自定义时必填例如：九江，不需要写市
    var county;  // 乡/区/县   选填参数

    updateTime()
    getWeather()

    // 粒子效果
    particlesJS('particles-js', {
        "particles": {
            "number": {
                "value": 50,
                "density": {
                    "enable": false,
                    "value_area": 800
                }
            },
            "color": {
                "value": "#145768"
            },
            "shape": {
                "type": "circle",
                "stroke": {
                    "width": 0,
                    "color": "#000000"
                },
                "polygon": {
                    "nb_sides": 5
                },
                "image": {
                    "src": "img/github.svg",
                    "width": 100,
                    "height": 100
                }
            },
            "opacity": {
                "value": 1,
                "random": true,
                "anim": {
                    "enable": false,
                    "speed": 1,
                    "opacity_min": 0.1,
                    "sync": false
                }
            },
            "size": {
                "value": 5,
                "random": true,
                "anim": {
                    "enable": false,
                    "speed": 40,
                    "size_min": 0.1,
                    "sync": false
                }
            },
            "line_linked": {
                "enable": false,
                "distance": 150,
                "color": "#ffffff",
                "opacity": 0.4,
                "width": 1
            },
            "move": {
                "enable": true,
                "speed": 3,
                "direction": "top",
                "random": false,
                "straight": false,
                "out_modehour": "out",
                "attract": {
                    "enable": false,
                    "rotateX": 600,
                    "rotateY": 1200
                }
            }
        },
        "interactivity": {
            "detect_on": "window",
            "events": {
                "onhover": {
                    "enable": false,
                    "modehour": "repulse"
                },
                "onclick": {
                    "enable": false,
                    "modehour": "push"
                },
                "resize": true
            },
            "modehours": {
                "grab": {
                    "distance": 400,
                    "line_linked": {
                        "opacity": 1
                    }
                },
                "bubble": {
                    "distance": 400,
                    "size": 40,
                    "duration": 2,
                    "opacity": 8,
                    "speed": 3
                },
                "repulse": {
                    "distance": 200
                },
                "push": {
                    "particles_nb": 4
                },
                "remove": {
                    "particles_nb": 2
                }
            }
        },
        "retina_detect": true,
        "config_demo": {
            "hide_card": false,
            "background_color": "#b61924",
            "background_image": "",
            "background_position": "50% 50%",
            "background_repeat": "no-repeat",
            "background_size": "cover"
        }
    });


    function updateTime() {
        var d = new Date((new Date).getTime());

        var time = d.getTime();
        var h = d.getHours();
        var m = d.getMinutes();
        var s = d.getSeconds();

        if (m < 10) {
            m = "0" + m;
        }

        if (s < 10) {
            s = "0" + s;
        }

        var month = d.getMonth();
        var day = d.getDate();
        var year = d.getFullYear();
        var weekday = d.getDay();

        var months = ["01", "02", "03", "04", "05", "06", "07", "08", "09", "10", "11", "12"];
        var days = ["星期日", "星期一", "星期二", "星期三", "星期四", "星期五", "星期六"];

        $('#time-second').html(h + ":" + m + ":" + s);
        $('#time-day').html("" + year + "年" + months[month] + "月" + day + "日，" + days[weekday] + "");
    }

    function updateWeather() {
        alert(province + "," + city + "," + county)
    }

    function getAddress() {

        // $.ajax({
        //     type: "get",
        //     url: "https://apis.map.qq.com/ws/location/v1/ip?key=3BFBZ-ZKD3X-LW54A-ZT76D-E7AHO-4RBD5",
        //     data: {},
        //     dataType: 'jsonp',
        //     success: function (resp) {
        //         province = resp.result.ad_info.province
        //         city = resp.result.ad_info.city
        //         county = resp.result.ad_info.district
        //         updateWeather();
        //     },
        //     error: function (e) {
        //         console.log(e.msg)
        //     }
        // });

        // req = $.get('http://apis.map.qq.com/ws/location/v1/ip?key=3BFBZ-ZKD3X-LW54A-ZT76D-E7AHO-4RBD5');
        // req.then(function (resp) {
        //     province = resp.result.ad_info.province
        //     city = resp.result.ad_info.city
        //     county = resp.result.ad_info.district
        //     updateWeather();
        // });
        $.getJSON('https://www.mxnzp.com/ip/self?app_id=hmnqziklvnthnckr&app_secret=TFZnZVdMSVdCdUlVUEhaOFVQOHBZdz09&callback=?',function(resp){
            province = resp.data.province
            city = resp.data.city
            //county = resp.result.ad_info.district
            updateWeather();
        });
    }

    function showAddress() {
        if (province) {
            $('#w-text').html(province + "，失败");
            if (city) {
                $('#w-text').html(province + "，" + city);
                if (county) {
                    $('#w-text').html(city + "，" + county);
                }
            }
        }
    }

    function getWeather() {
        if (province && city) {
            showAddress()
            updateWeather()
        } else {
            // 获取地址在 获取天气
            getAddress()
            showAddress()
            updateWeather()
        }
    }

    setInterval(function () {
        updateTime();
    }, 1000);

    // 默认五分钟请求一次
    setInterval(function () {
        getWeather();
    }, (1000 * 60 * 5));

});