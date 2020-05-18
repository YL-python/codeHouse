setTimeout( function () {
  console.log( 'main process timeout 1' );
}, 500 );


// 给一个 500ms 的延时
console.log( '延时 500 ms' );
let curr = +new Date();
while( (+new Date) - curr < 500 );

console.log( 'main process 1' );
console.log( 'main process 2' );

setTimeout( function () {
  console.log( 'main process timeout 2' );
}, 0 );

console.log( 'main process 3' );
console.log( 'main process 4' );

setTimeout( function () {
  console.log( 'main process timeout 3' );
}, 0 ); // 此时 对中有 3 个函数



// 时间很微妙

// 分析: setTimeout 的时间是从刚刚加入time队列开始计算的
//  也就是说主程序执行耗时500ms  之后 这个500毫秒延迟执行的回调函数不会在等500ms 而是立即执行
