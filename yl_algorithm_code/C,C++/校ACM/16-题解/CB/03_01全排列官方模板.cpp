#include <iostream>
using namespace std;
int a[] = {1,2,3,4,5,6,7,8,9};
int ans;

bool test(){
	int A = a[0], b = a[1], c = a[2];
	int def = a[3] * 100 + a[4] * 10 + a[5];
	int ghi = a[6] * 100 + a[7] * 10 + a[8];
	if((b * ghi + c * def) % (c * ghi) == 0 && (b * ghi + c * def) / (c * ghi) == (10 - A)){
		return true;
	}else{
		return false;
	}
}

// 递归回溯生成全排列， 适用于没有重复元素的题目 
void f(int k) {
	if(k == 9){
		if(test()){
			ans++;
		}
	}
	for(int i=k; i<9; i++) {
		{int t = a[i]; a[i] = a[k]; a[k] = t;}
		f(k+1);
		{int t = a[i]; a[i] = a[k]; a[k] = t;}
	}
}

int main () {
	f(0);
	cout << ans << endl;
	return 0;
}
/*
凑算式

     B      DEF
A + --- + ------- = 10
     C      GHI

（如果显示有问题，可以参见【图1.jpg】）


这个算式中A~I代表1~9的数字，不同的字母代表不同的数字。

比如：
6+8/3+952/714 就是一种解法，
5+3/1+972/486 是另一种解法。

这个算式一共有多少种解法？

注意：你提交应该是个整数，不要填写任何多余的内容或说明性文字。
*/
