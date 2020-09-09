const LOCATION_KEY = '__yujian_weather_location__'

export function saveLocation(location) {
	let locations = uni.getStorageSync(LOCATION_KEY)
	locations = locations ? locations : []

	let flag = true
	console.log('locations', locations);
	locations.forEach((item) => {
		if (item.province === location.province && item.city === location.city && item.district === location.district) {
			flag = false
		}
	})
	if (flag) {
		locations.push(location)
	}
	uni.setStorageSync(LOCATION_KEY, locations);
	return locations
}

export function deleteLocation(location) {
	let locations = uni.getStorageSync(LOCATION_KEY)
	locations = locations ? locations : []
	// 在 locations 中删除 location
	locations = locations.filter((item) => {
		if (item.province === location.province && item.city === location.city && item.district === location.district) {
			return false
		}
		return true
	})
	uni.setStorageSync(LOCATION_KEY, locations);
	return locations
}

export function loadLocation() {
	let locations = uni.getStorageSync(LOCATION_KEY)
	return locations ? locations : []
}
