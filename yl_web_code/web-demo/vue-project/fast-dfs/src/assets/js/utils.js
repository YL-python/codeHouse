// alertMsg 和 sessionStorage
export default {
	install(Vue) {
		Vue.prototype.alertMsg = function (code, msg) {
				if (code == 0) {
					this.$message({
						message: msg,
						type: 'success'
					});
				} else {
					if ("ssofail" == msg) {
						this.$message.error("登录失效,请重新登录系统!");
						this.removeSession();
						this.$router.push("/");
					} else {
						this.$message.error(msg);
					}
				}
			},
			Vue.prototype.addSession = function (userId, username) {
				//分享提取的时候用到
				localStorage.setItem("userId", userId);
				localStorage.setItem("username", username);
				sessionStorage.setItem("userId", userId);
				sessionStorage.setItem("username", username);
			},
			Vue.prototype.removeSession = function () {
				localStorage.removeItem("token");
				localStorage.removeItem("userId");
				localStorage.removeItem("username");

				sessionStorage.removeItem("token");
				sessionStorage.removeItem("userId");
				sessionStorage.removeItem("username");

				sessionStorage.removeItem("activeIndex");
			}
	}
}