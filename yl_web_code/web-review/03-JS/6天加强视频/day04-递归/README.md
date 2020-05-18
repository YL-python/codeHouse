# 递归就这么简单

目标:

1. 能分析 this 的实际意义
2. 口述递归的一般处理办法
3. 能实现基本的算术递归案例
4. 实现深拷贝


## 1. 函数的调用模式

回顾:

- 每一个函数在运行的时候都会创建一个独有活动对象
  - 在活动对象中包含 函数的 参数, 以及函数内部的声明的数据
  - 除了 定义参数与声明的变量与函数外, 在这个活动对象上还存在一个 叫做上下文的( context ) 东西

在 js 中 this 的意译

目标:

1. ***记住*** this 在什么情况下表示什么东西
2. 通过对代码的分析, 我们可以定位是哪一种情况, 能分析出 this 的意义


函数的 5 中调用模式( ES3 时代 函数有 4 中调用模式, ES5 引入了 bind, 所以 函数有 5 中调用模式 )

- 函数模式: this 表示全局对象( 浏览器中是window, 在 node 中是 global )
- 构造器( constructor )模式: this 表示刚刚创建出来的对象
- 方法 ( method ) 模式: this 表示引导方法调用的对象
- 上下文 ( context ) 模式: this 可以使用参数来动态的描述 ( 动态绑定 )
  - 在调用函数的时候, 传入对象作为 this, 每次调用可以传入不同 对象作为 this
- bind 模式: this 与 上下文模式类似, 也是通过参数来确定 ( 静态绑定 )
  - bind 已开启就绑定, 其后在使用的时候就不需要绑定, 每次使用的时候都是一开始绑定的那一个 this
  - 语法:
    - 函数.bind( 对象 ) // 返回已绑定 this 的新函数

上下文语法
1. 函数名.call( 上下文, 参数1, 参数2, ... )     可以有任意个参数
2. 函数名.apply( 上下文, [ 参数, ... ] )        最多两个参数

问题:

1. 有几个参数?
2. 调用的意译: 无论是 函数的正常调用, 还是 call 调用, 还是 apply 调用其实都是在调用函数



技巧: 上下文调用的技巧主要是借用和展开

1. 上下文调用有一个特征可以随意的修改的 this 的含义
  - 数组的借用方法
  - slice( startIndex, length )
  - 可以实现将伪数组转换为真数组( ES3 时代的用法 )
    - arr.slice( 0, arr.length ) 什么意思? 拷贝数组 ( 浅拷贝 )
    - 伪数组.slice( 0, 伪数组的长度 ) 
    - 伪数组没有这个方法, 可以借用
    - Array.prototype.slice.call( 伪数组 )  
    - Array.prototype.slice.apply( 伪数组 )  

  - 在页面中将歌曲数据找出来
    - title="你要找的名字"
    - 找到该元素的 父元素 的子元素 ( class="rank-list-box" )
    - rank-list-box 里面有 a 标签, title 是歌曲名字, a 里面还有 img 是图片

    function getMusitInfo( typeName ) {
      var songsContainer = Array.prototype.slice.call( document.querySelectorAll( 'a' ) )
        .filter( a => a.title == '新歌榜' && a.className.indexOf( 'rank-title' ) > -1 )

      var list = Array.prototype.slice.call( document.querySelectorAll( 'a' ) ).filter( a => a.title == '新歌榜' && a.className.indexOf( 'rank-title' ) > -1 )[ 0 ].parentNode.parentNode.children;

      Array.prototype.call( list ).filter( div => div.className.indexOf( 'rank-list-box' ) > -1 ) 
    }


    var $ = document.querySelectorAll()


箭头函数

1. 箭头函数它不改变 this

面试题


```js
var length = 10;
function fn() {
  console.log( this.length );
}

var obj = {
  length: 5,
  method: function ( fn ) {
    fn();
    arguments[ 0 ]();
  }
};
obj.method( fn, 1, 2, 3 );
```


## 2. 递归的方法论

所谓的递归就是自己调用自己, 有一个很重要的思想, 就是划归

- 函数本身要做一件事情, 调用一个函数其实就是在做一件事
- 自己调用自己是, 要做一件事情, 就要先做 什么什么
  - 如果要做某个事情就是将其转换外已经解决的问题
  - f1 调用 f2: 如果要做 f1, 即先做 f2
  - f2 调用 f3: 如果要做 f2, 就先做 f3
  - ...
  - 何时是一个头??? 临界条件, 就是跳出递归的条件

方法:

1. 首先要假设你已经完成了递归函数
```js
  // 代码可以改写为如下形式
  function func() {
    // ...
    func();
    // ...
  }
```
2. 找出这个转换的条件( 难点 )
3. 找出临界条件
```js
  // 代码可以改写为如下形式
  function func() {
    // ...
    if ( 临界条件 ) return
    // ...
    func();
    // ...
  }
```
临界条件的形式可能有变化
```js
  // 代码可以改写为如下形式
  function func() {
    // ...
    for ( ... ) {
      // ...
      func();
      // ...
    }
    // ...
  }
```


## 3. 案例

- 等差与等比数列
  - 求 第 n 项: 1 3 5 7 9 -> 2n+1
  - 求 第 n 项: 2 5 8 11 14 -> 2 + n * 3
  - 求上面第二个案例中 前 n 项的 和:
    - 2 7 15 26 ...
    - s(n) = s( n - 1) + a(n)
- 差分数列
  - 1 2 4 7 11 16 ...
  -  1 2 3 4  5
- 阶乘
  - n! => n * (n - 1) * ( n - 2 ) * ... * 1
  - n! = n * ( n - 1 )!
- 乘幂
  - pow( 2, 3 ) => pow( 2, 2 ) * 2
- Fibonacci 数列
  - 1 1 2 3 5 8 ...
  - 思考 如何实现

## 4. 应用案例

- 树搜索 ( 算法 )
- 深拷贝 ( 技巧说明 )



问题:

1. 递归怎么实现数组[1,2,3]，打印出数组中数的**所有排列组合**
  - 问题: 可重复, 还是不可重复, 有序还是无序
  - 假设: 不重复, 不考虑顺序
  - 延伸出来的, 单词学习的案例: world => w___d orl lor lro orl

  可取的值为 1 到 arr.length

  如果只取 1 个 
    for ( var i = 0; i < arr.length; i++ ) {
      arr[ i ]
    }
  如果取 2 个
    for ( var i = 0; i < arr.length; i++ ) {
      arr[ i ]
      for ( var j = 0; j < arr.length; j++ ) {
        if ( i != j ) {
          arr[ j ]
        }
      }
    }
  如果取 3 个
    for ( var i = 0; i < arr.length; i++ ) {
      arr[ i ]

      for ( var j = 0; j < arr.length; j++ ) {  // 就在 arr.slice().slice( i, 1 )
        if ( i != j ) {
          arr[ j ]

          for ( var k = 0; k < arr.length; k++ ) { // 就在 arr.slice().slice( i, 1 )
            if ( k != i && k != j ) {
              
              arr[ k ]

            }
          }
        }
      }
    }
  
  function f( 取第 n 个 ) {
    for ( ) {
      if ( n > 0 ) {
        f( 取 n - 1 个 )
      }
    }
  }


