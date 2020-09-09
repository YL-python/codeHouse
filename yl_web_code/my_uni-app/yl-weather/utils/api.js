// const BASE_URL = "http://localhost:3000/hmshop"
const BASE_URL = "https://coderyl.top/node"

export const myRequest = (options) => {
	// console.log("当前请求的 url为：", BASE_URL + parseUri(options.url))
	return new Promise((resolve, reject) => {
		uni.request({
			url: BASE_URL + parseUri(options.url),
			method: options.method || "GET",
			data: options.data || {},
			success: (res) => {
				// console.log('res',res);
				if (res.statusCode === 200) {
					resolve(res.data)
				} else {
					return uni.showToast({
						title: "数据获取失败",
						icon: "loading"
					})
				}
			},
			fail: (err) => {
				uni.showToast({
					title: "数据获取失败",
					icon: "loading"
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
