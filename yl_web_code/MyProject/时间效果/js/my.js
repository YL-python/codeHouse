$(document).ready(function () {

    updateTime()

    // 粒子效果
    particlesJS('particles-js', {
        "particles": {
            "number": {
                "value": 80, // 粒子个数
                "density": {  // 密度参数，不开启，和个数差不多
                    "enable": false,
                    "value_area": 800
                }
            },
            "color": {
                "value": "#145768"  // 颜色
            },
            "shape": {
                // 形状  circle(圆形)，edge(正方形)，triangle(三角形)，polygon(多边形)，star(五角星)，image(图片)
                // 还可以是形状数组  ["circle", "triangle", "image"]
                "type": "circle",
                "stroke": {
                    "width": 0,
                    "color": "#000000"
                },
                "polygon": {   // 形状是多边形的时候
                    "nb_sides": 5
                },
                "image": {  // 形状是图片的时候
                    "src": "img/github.svg",
                    "width": 100,
                    "height": 100
                }
            },
            "opacity": {  // 透明度
                "value": 1,
                "random": true,
                "anim": {
                    "enable": false,
                    "speed": 1,
                    "opacity_min": 0.1,
                    "sync": false
                }
            },
            "size": {  // 大小
                "value": 5,
                "random": true,
                "anim": {
                    "enable": false,
                    "speed": 40,
                    "size_min": 0.1,
                    "sync": false
                }
            },
            "line_linked": {  //是否用线连接
                "enable": false,
                "distance": 150,  // 线的长度
                "color": "#ffffff",
                "opacity": 0.4,
                "width": 1
            },
            "move": {  // 移动
                "enable": true,
                "speed": 3,  // 时间
                "direction": "top",  // 移动的方向
                // "none"随机，"top"上，"top-right"，"right"，"bottom-right"，"bottom"，"bottom-left"，"left"，"top-left"
                "random": false,  // 随机
                "straight": false,  // 标准的移动
                "out_modehour": "out",  // out  出去  bounce  反弹
                "attract": {
                    "enable": false,
                    "rotateX": 600,
                    "rotateY": 1200
                }
            }
        },
        "interactivity": {
            "detect_on": "window",  //  交互  window，canvas
            "events": {  // 时间
                "onhover": {  // 悬停
                    "enable": false,
                    // 样式 "grab"，"bubble"，"repulse"，也可以是数组
                    "mode": ["grab", "bubble"]
                },
                "onclick": {  // 点击
                    "enable": true,
                    // 样式 "push"，"remove"，"bubble"，"repulse"，也可以是数组
                    "mode": "bubble"
                },
                "resize": true
            },
            "mode": {  // 修改时间触发时候的样式
                "grab": {
                    "distance": 140,
                    "line_linked": {
                        "opacity": 0.75
                    }
                },
                "bubble": {
                    "distance": 400,
                    "size": 40,
                    "duration": 2,
                    "opacity": 8,
                    "speed": 1
                },
                "repulse": {
                    "distance": 200,
                    "duration": 0.4
                },
                "push": {
                    "particles_nb": 4
                },
                "remove": {
                    "particles_nb": 2
                }
            }
        },
        "retina_detect": true
    });
    // 粒子效果启动方式
    // particlesJS.load('particles-js', 'assets/particles.json', function () {
    //     console.log('callback - particles.js config loaded');
    // });


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

    setInterval(function () {
        updateTime();
    }, 1000);
});