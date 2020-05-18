setTimeout( function () {
  console.log( 'main process timeout 1' );
}, 1000 );

console.log( 'main process 1' );
console.log( 'main process 2' );
console.log( 'main process 3' );
console.log( 'main process 4' );
console.log( 'main process 5' );
console.log( 'main process 6' );

// 分析
// 1. 执行 `setTimeout`, 这个执行是同步的, 会将 回调函数, 放入事件队列的 Timer 队列中, 现在不会执行, 并记录执行时间
// 2. 进入 console.log 系列, 此时就是先行执行, 这里执行完成以后, 启用事件队列中的代码
// 3. 进入事件队列后, 优先开始运行 timer 队列, 发现只有里面存在一个函数, 将其取出执行
// 4. 此时需要注意 timer 事件队列中的函数存在一个 时间的范围, 加入现在已过去 900ms, 不好意思, 
//    此时不会执行, 还会继续遍历 pending, roll, check, close ... 队列,
//    等到这些队列遍历完, 又会回调 timer 队列, 如果此时发现时间已过去 990ms, 不好意思, 
//    此时还不会执行, 还会继续遍历 pending, roll, check, close ... 队列, 
//    等到这些队列遍历完, 又会回调 timer 队列, 如果此时发现时间已过去 1000ms, 才会执行. 
//    注意： 在遍历pending, roll, check, close ... 队列时，会把队列里面的任务执行完成在继续下一个队列

