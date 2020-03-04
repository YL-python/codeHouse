#include <iostream>
using namespace std;

int main (){
	long long x;
	cin >> x;
	for(long long i=0;i<=10000000000000;i++){
		if(i*i>=x){
			cout << i*i;
			break;
		}
	}
	return 0;
}
/*
输出大等于n的最小的完全平方数。
若一个数能表示成某个自然数的平方的形式，则称这个数为完全平方数
Tips：注意数据范围
*/
