// const BASE_URL = "http://localhost:3000/hmshop"
const BASE_URL = "http://coderyl.top/node/hmshop"

export const myRequest = (options) => {
	return new Promise((resolve, reject) => {
		uni.request({
			url: BASE_URL + parseUri(options.url),
			method: options.method || "GET",
			data: options.data || {},
			success: (res) => {
				if (res.data.status === 0) {
					resolve(res.data)
				} else {
					return uni.showToast({
						title: "数据获取失败"
					})
				}
			},
			fail: (err) => {
				uni.showToast({
					title: "请求接口失败"
				})
				reject(err)
			}
		})
	})
}

// uri 第一个不是斜杠就加斜杠,是就直接返回
function parseUri(uri) {
	if (uri.indexOf('/') === 0) {
		return uri
	} else {
		return '/' + uri
	}
}
