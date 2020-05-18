// 使用node 样式代码执行步骤
function yl_test(){
  console.log(' yl test js');
}

yl_test()

/*

用node运行这个文件

node demo.js
输出:yl test js
// 上面这个好理解

node --print-code demo.js > demo-code.txt
// 会把 demo.js代码生成的 字节码  输出到demo-code.txt文件中

node --print-bytecode demo.js > demo-bytecode.txt
// 会把 demo.js代码生成的 机器码  输出到demo-bytecode.txt文件中
// 机器码很大，因为把我们代码用到的所有环境都编译了

// 上面的指令可以用 node --help来查看
其中有一个  --v8-options  指令可以看到 node中关于 v8引擎的指令

node --v8-options > v8options.txt
// 可以把关于v8引擎有关的指令输出到 v8options.txt 文件中

*/ 