#include <iostream>
#include <string>
using namespace std;

int only(int x){
	int ans=0;
	while(x>=10){
		ans+=x%10;
		x/=10;
	}
	ans+=x;
	return ans;
}

int main(){
	int n,m;
	cin >>n;
	for(int i=0;i<n;i++){
		cin >>m;
		while(m>=10){
			m = only(m);
		}
		cout << m << endl;
	} 
	return 0;
}
/*
Description
第一行有1个正整数 t(1<=t<=1000)，t代表测试组数；接下来每行一个n(0<n<1000000)，如果n> 10，则将这个n的各个位数的值相加，如果相加的和ans还大于10，则继续如此操作，直到ans <10 ，将答案输出
例如n = 1234，则1 + 2 + 3 + 4 = 10，重复这个操做，1 + 0 = 1 <10，输出的结果为1

Input
第一行输入一个正整数t
接下来t行每行一个正整数n（0<n<1000000）

Output
每个n对应一个输出，答案一定小于10

Sample Input 1 
4
1234
123
12345
1

Sample Output 1
1
6
6
1
*/ 
