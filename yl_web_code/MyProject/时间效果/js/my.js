$(document).ready(function () {

    updateTime()

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

    setInterval(function () {
        updateTime();
    }, 1000);
});