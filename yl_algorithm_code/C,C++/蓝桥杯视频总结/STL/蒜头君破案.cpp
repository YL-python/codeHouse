#include <iostream>
#include <string>
#include <set>
using namespace std;

struct pep{
	int h;
	int w;
	int age;
	pep(int _h, int _w, int _age){
		h = _h;
		w = _w;
		age = _age;
	}
	// operator<   表示要重载 < 这个运算符  以此定义排序规则 
	// (const 结构体名 &变量名) const  固定写法 
	bool operator<(const pep &rhs) const{
		if(h !=rhs.h){  // 表示两个h 不同的时候 定义排序方式 
			return h < rhs.h;
		}
		if(w != rhs.w){
			return w < rhs.w;
		}
		return age < rhs.age;  // 表示 h和w都相同的时候用 age 来排序 
	}
};

set<pep> s;

int main(){
	int n,m,h,w,age;
	cin >> n >> m;
	for(int i=0;i<n;i++){
		cin >> h >> w >> age;
		s.insert(pep(h,w,age));
	}
	for(int i=0;i<m;i++){
		cin >> h >> w >> age;
		if(s.count(pep(h,w,age))){  // 时间复杂度是0(logn) 比我们自己遍历要好 
			cout << "YES" << endl;
		}else{
			cout << "NO" << endl;
		}
	}
	return 0;
}

/*
一个城市 n个人
有m个人的信息
现在有 m个盗贼
看看 m个盗贼有没有可能是这个城市的人 

3 2
166 50 30
178 60 23
132 40 15
167 50 30
NO
178 60 23
YES
*/
