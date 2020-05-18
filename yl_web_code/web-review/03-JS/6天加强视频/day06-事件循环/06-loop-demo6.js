
setImmediate( function () {
  console.log( 'main process immediate 1' );
} )

console.log( 'main process 1' );
console.log( 'main process 2' );

console.log( 'main process 3' );
console.log( 'main process 4' );


setTimeout( function () {
  console.log( 'main process timeout 1' );
}, 3 );


// 启用队列, 优先执行 timer

// 如果进入 timer 队列的时候 还不足 5 毫秒, 那么 就会进入下一个循环队列

// 需求, 因为不知道谁会先执行, 如果我就希望先执行 timeout 的事件处理, 后处理 immediate 
// 要实现, 只需要将代码 放到 immediate 逻辑中即可

setImmediate( () => {
  // 若要执行这段代码, 必然是在 check 事件队列中, 此时, 接着进入 timer 对象
  setImmediate( function () {
    console.log( 'main process immediate 1' );
  } )

  setTimeout( function () {
    console.log( 'main process timeout 1' );
  }, 0 );

} )


// 假如我就要先执行 immediate, 那就只需将代码放在 timeout 中

setTimeout( () => {
  // 若要执行这段代码, 必然是在 timer 事件队列中, 此时, 接着进入 其他的队列中
  setImmediate( function () {
    console.log( 'main process immediate 1' );
  } )

  setTimeout( function () {
    console.log( 'main process timeout 1' );
  }, 0 );

}, 0 );