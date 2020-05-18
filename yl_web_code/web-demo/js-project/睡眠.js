// 参数是睡眠的毫秒值
function sleep(time){
	let startTime = +new Date();
	while( ( +new Date() ) - startTime < time );
}

console.log(111);
sleep(5000)
console.log(222);