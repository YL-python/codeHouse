#include <iostream>
#include <string>
using namespace std;

int main(){
	int a=5,b=10;
	swap(a,b);    // 交换两个整数的地址   std内的函数 std::swap(a,b); 
	cout << a << endl << b;
	return 0;
}

