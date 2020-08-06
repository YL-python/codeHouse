# include <deque>

// 双端队列 支持两端插入和弹出
deque <int> d;

d.push_front(x);
d.push_back(x);

d.pop_front();
d.pop_back();

x = d.front();
x = d.back();

// 双端队列支持 下标访问  不过时间复杂度是 N
d[i]  // d 内第 i 个元素
