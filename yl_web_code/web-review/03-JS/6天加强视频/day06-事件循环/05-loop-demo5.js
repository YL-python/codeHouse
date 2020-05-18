setImmediate(function () {
  console.log('main process immediate 1');
})

console.log('main process 1');
console.log('main process 2');

console.log('main process 3');
console.log('main process 4');

setTimeout(function () {
  console.log('main process timeout 1');
}, 0);


// 启用队列
// 主程序线性执行把 setTimeout加入到time队列，把setImmediate加入到check队列
// 又因为队列的处理循序中，time队列的处理优先与check队列