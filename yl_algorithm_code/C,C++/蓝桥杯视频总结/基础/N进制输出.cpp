#include <iostream>
#include <string>
#include<cstring>
using namespace std;

/*
进制转换，输入一个整数N 和R进制
输入整数对应的R进制 
*/ 

int N,R;
char c[20] = {'0','1','2','3','4','5','6','7','8','9','A','B','C','D','E','F','G'}; 
char ans[105];
int main(){
	cin >> N >>	R;
	int m=0,now;
	if(N < 0){
		cout << "- ";
		N *= -1;
	}
	while(N){
		now = N%R;
		ans[m++] = c[now];
		N /= R;
	} 
	if(m == 0){
		cout << 0;
	}
	for(int i=m-1;i>=0;i--){
		cout << ans[i] << " "; 
	} 
	return 0;
}

