#include <iostream>
using namespace std;

int cnt(int x){
	return (1+x)*x/2;
}

// 阅读理解。。。每一层放多少个，求前100层  一共多少个 
int main (){
	int N = 100;
	int ans;
	for(int i=1;i<=100;i++){
		ans+= cnt(i); 
	}
	cout << ans; 
	return 0;
} 
/*

煤球数目

有一堆煤球，堆成三角棱锥形。具体：
第一层 放 1个，
第二层3个（排列成三角形），
第三层6个（排列成三角形），
第四层10个（排列成三角形），
....
如果一共有100层，共有多少个煤球？

请填表示煤球总数目的数字。
注意：你提交的应该是一个整数，不要填写任何多余的内容或说明性文字。

*/
