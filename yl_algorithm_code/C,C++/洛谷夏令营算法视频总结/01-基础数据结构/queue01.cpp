#include <cstdio>

int a[100005],fnt,end;

#define push(x) s[++end]=x
#define pop() fnt++
#define size() end-fnt+1
#define front() s[fnt]

// 自己手写队列就会出现浪费空间的问题
// 想要不浪费空间就用循环队列
// 循环队列是下标去 % 数组的长度
// queue库中帮我们实现了
