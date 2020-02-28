#include <iostream>
#include <string>
#include <set>   // set 头文件 
using namespace std;

int main(){
	set<int> a;  // set 集合不会有重复元素  并且会自动排序 
	
	a.insert(0); 
	a.insert(1); 
	a.insert(2);  // insert() 插入方法 
	a.insert(2);  // 不会重复 
	
	a.erase(0);  // 删除元素   不存在的时候不进行操作 没有报错 

	cout << a.count(1) << endl;  // 查找元素  找到返回  1  没找到返回 0	
	
	// 遍历需要用到迭代器  写法很固定 
	for(set<int>::iterator i=a.begin(); i != a.end(); i++){
		cout << *i <<endl ;
	} 
	
	a.clear();  // 清空集合 同时会清空内存 
	
	/*  set  底层实现原理是 红黑树 
	insert()  插   O(logn)
	erase()  删   O(logn)
	count()  统计个数    O(logn)
	size()  获取元素个数    O(1)
	clear()   清空    O(n)
	*/ 
	
	return 0;
}

