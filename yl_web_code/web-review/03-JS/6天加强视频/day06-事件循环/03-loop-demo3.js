setTimeout( function () {
  console.log( 'main process timeout 1' );
}, 0 );

console.log( 'main process 1' );
console.log( 'main process 2' );
console.log( 'main process 3' );
console.log( 'main process 4' );

setTimeout( function () {
  console.log( 'main process timeout 2' );
}, 0 );

console.log( 'main process 5' );
console.log( 'main process 6' );

setTimeout( function () {
  console.log( 'main process timeout 3' );
}, 0 ); // 此时 time 队列中有 3 个函数

// 开始启用队列, 依次执行存入的 回调函数

//   分析: setTimeout方法是同步执行的，会把回调函数加入到time队列中
//   线性执行完成之后，time队列中就会有三个回调函数
