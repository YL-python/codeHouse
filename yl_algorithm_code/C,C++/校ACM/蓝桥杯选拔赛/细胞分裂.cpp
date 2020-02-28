#include <iostream>
#include <string>
using namespace std;

int gcd(int a, int b){
    return b?gcd(b,a%b):a;
}

int lcm(int a,int b){
	return a/gcd(a,b)*b;
}


int main(){
	int a,n;
	cin >> a >> n;
	int ans=1,m=0;
	for(int i=0;i<n;i++){
		if(a>ans){
			m = lcm(a,ans);
		}else{
			m = lcm(ans,a);
		}
		if(m%2 == 0){
			ans+=1;
		}else{
			ans+=ans;
		}
	}
	cout << ans;
	return 0;
}
/*
Description

你正在培养一种细胞，每天给它固定数量的营养液，并且时刻观察细胞的数量，经过了几天的观察你发现了这种细胞有一种奇怪的现象：营养液的数量与细胞数量的最小公倍数是奇数的话，细胞就会分裂成为原来的2倍，如果是偶数的话，细胞总数就只会加1个。现在你想知道1个细胞在a个数量的营养液下，第n天的细胞总数是多少。


Input
只有一行，2个正整数a，n用空格分开。(a<=100,n<=20)


Output
输出对应的数量


Sample Input 1 

5 3
Sample Output 1

6
*/ 
