$(document).ready(function () {
	var modehour, modeseconds, api, city, country, hilow, lastResponse;
	var manuallyRefreshed = false;
	var weatherIcons = {
		"200": { "label": "thunderstorm with light rain", "icon": "storm-showers" },
		"201": { "label": "thunderstorm with rain", "icon": "storm-showers" },
		"202": { "label": "thunderstorm with heavy rain", "icon": "storm-showers" },
		"210": { "label": "light thunderstorm", "icon": "storm-showers" },
		"211": { "label": "thunderstorm", "icon": "thunderstorm" },
		"212": { "label": "heavy thunderstorm", "icon": "thunderstorm" },
		"221": { "label": "ragged thunderstorm", "icon": "thunderstorm" },
		"230": { "label": "thunderstorm with light drizzle", "icon": "storm-showers" },
		"231": { "label": "thunderstorm with drizzle", "icon": "storm-showers" },
		"232": { "label": "thunderstorm with heavy drizzle", "icon": "storm-showers" },
		"300": { "label": "light intensity drizzle", "icon": "sprinkle" },
		"301": { "label": "drizzle", "icon": "sprinkle" },
		"302": { "label": "heavy intensity drizzle", "icon": "sprinkle" },
		"310": { "label": "light intensity drizzle rain", "icon": "sprinkle" },
		"311": { "label": "drizzle rain", "icon": "sprinkle" },
		"312": { "label": "heavy intensity drizzle rain", "icon": "sprinkle" },
		"313": { "label": "shower rain and drizzle", "icon": "sprinkle" },
		"314": { "label": "heavy shower rain and drizzle", "icon": "sprinkle" },
		"321": { "label": "shower drizzle", "icon": "sprinkle" },
		"500": { "label": "light rain", "icon": "rain" },
		"501": { "label": "modehourrate rain", "icon": "rain" },
		"502": { "label": "heavy intensity rain", "icon": "rain" },
		"503": { "label": "very heavy rain", "icon": "rain" },
		"504": { "label": "extreme rain", "icon": "rain" },
		"511": { "label": "freezing rain", "icon": "rain-mix" },
		"520": { "label": "light intensity shower rain", "icon": "showers" },
		"521": { "label": "shower rain", "icon": "showers" },
		"522": { "label": "heavy intensity shower rain", "icon": "showers" },
		"531": { "label": "ragged shower rain", "icon": "showers" },
		"600": { "label": "light snow", "icon": "snow" },
		"601": { "label": "snow", "icon": "snow" },
		"602": { "label": "heavy snow", "icon": "snow" },
		"611": { "label": "sleet", "icon": "sleet" },
		"612": { "label": "shower sleet", "icon": "sleet" },
		"615": { "label": "light rain and snow", "icon": "rain-mix" },
		"616": { "label": "rain and snow", "icon": "rain-mix" },
		"620": { "label": "light shower snow", "icon": "rain-mix" },
		"621": { "label": "shower snow", "icon": "rain-mix" },
		"622": { "label": "heavy shower snow", "icon": "rain-mix" },
		"701": { "label": "mist", "icon": "sprinkle" },
		"711": { "label": "smoke", "icon": "smoke" },
		"721": { "label": "haze", "icon": "day-haze" },
		"731": { "label": "sand, dust whirls", "icon": "cloudy-gusts" }, "741": { "label": "fog", "icon": "fog" }, "751": { "label": "sand", "icon": "cloudy-gusts" }, "761": { "label": "dust", "icon": "dust" }, "762": { "label": "volcanic ash", "icon": "smog" }, "771": { "label": "squalls", "icon": "day-windy" }, "781": { "label": "tornado", "icon": "tornado" }, "800": { "label": "clear sky", "icon": "sunny" }, "801": { "label": "few clouds", "icon": "cloudy" }, "802": { "label": "scattered clouds", "icon": "cloudy" }, "803": { "label": "broken clouds", "icon": "cloudy" }, "804": { "label": "overcast clouds", "icon": "cloudy" }, "900": { "label": "tornado", "icon": "tornado" }, "901": { "label": "tropical storm", "icon": "hurricane" }, "902": { "label": "hurricane", "icon": "hurricane" }, "903": { "label": "cold", "icon": "snowflake-cold" }, "904": { "label": "hot", "icon": "hot" }, "905": { "label": "windy", "icon": "windy" }, "906": { "label": "hail", "icon": "hail" }, "951": { "label": "calm", "icon": "sunny" }, "952": { "label": "light breeze", "icon": "cloudy-gusts" }, "953": { "label": "gentle breeze", "icon": "cloudy-gusts" }, "954": { "label": "modehourrate breeze", "icon": "cloudy-gusts" }, "955": { "label": "fresh breeze", "icon": "cloudy-gusts" }, "956": { "label": "strong breeze", "icon": "cloudy-gusts" }, "957": { "label": "high wind, near gale", "icon": "cloudy-gusts" }, "958": { "label": "gale", "icon": "cloudy-gusts" }, "959": { "label": "severe gale", "icon": "cloudy-gusts" }, "960": { "label": "storm", "icon": "thunderstorm" }, "961": { "label": "violent storm", "icon": "thunderstorm" }, "962": { "label": "hurricane", "icon": "cloudy-gusts" }
	};

	window.wallpaperPropertyListener = {
		applyUserProperties: function (properties) {
			if (properties.modehour) {
				modehour = properties.modehour.value;
			}

			if (properties.modeseconds) {
				modeseconds = properties.modeseconds.value;
			}

			if (properties.api) {
				api = properties.api.value;
			}

			if (properties.city) {
				city = properties.city.value;
			}

			if (properties.country) {
				country = properties.country.value;
			}

			if (properties.hilow) {
				hilow = properties.hilow.value;
			}

			if (!manuallyRefreshed) {
				// Prevents making too many requests to OpenWeatherMap, resets on interval.
				manuallyRefreshed = true;
				getWeather();
			}

			updateTime();
			updateWeather();
		}
	};

	modehour = true;
	modeseconds = true;
	getWeather()

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

		var ampm = modehour ? "" : (h < 12 ? " AM" : " PM");

		if (h > 12 && !modehour) {
			h = h - 12;
		}

		if (h == 0 && !modehour) {
			h = 12;
		}

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

		// var output = ""+days[weekday]+", "+months[month] + " "+day+", "+year+"";
		var output = "" + year + "-" + months[month] + "-" + day + "，" + days[weekday] + "";

		$('#time-title').html(h + ":" + m + (modeseconds ? ":" + s : "") + ampm);
		$('#time-subtitle').html(output);
	}

	function updateWeather() {
		if (lastResponse) {

			// var prefix = 'wi wi-fw wi-';
			// var code = lastResponse.weather[0].id;
			// var icon = weatherIcons[code].icon;
			// if (!(code > 699 && code < 800) && !(code > 899 && code < 1000)) {
			// 	icon = 'day-' + icon;
			// }
			// icon = prefix + icon;
			icon = 'wi wi-fw wi-day-storm-showers'


			var main = lastResponse.data.address;
			var temp = lastResponse.data.forecasts[0].dayTemp + " - " + lastResponse.data.forecasts[0].nightTemp;
			var low = lastResponse.data.forecasts[0].dayTemp;
			var high = lastResponse.data.forecasts[0].dayTemp;

			main = main.substr(0, 1).toUpperCase() + main.substr(1);

			$('#weather-icon').removeClass().addClass(icon);
			// $('#weather-text').html(main + ", " + temp + "&deg;C" + (hilow ? " (&darr; " + low + "&deg;C, &uarr; " + high + "&deg;C)" : ""));
			$('#weather-text').html(main + "<br> " + temp);
		}
	}

	function getWeather() {
		//if (api && city && country) {
		if (true) {
			// req = $.getJSON('http://api.openweathermap.org/data/2.5/weather?q=' + city + ',' + country + '&units=metric&appid=' + api + '&callback=?');
			req = $.getJSON('https://www.mxnzp.com/weather/forecast/彭泽县?app_id=hmnqziklvnthnckr&app_secret=TFZnZVdMSVdCdUlVUEhaOFVQOHBZdz09');
			req.then(function (resp) {
				lastResponse = resp;
				updateWeather();
			});
		}
	}

	setInterval(function () {
		updateTime();
	}, 1000);

	setInterval(function () {
		// Allow a manual refresh, resetting wallpaperPropertyListener's applyUserProperties.
		manuallyRefreshed = false;
		getWeather();
	}, (1000 * 60 * 5));
});
