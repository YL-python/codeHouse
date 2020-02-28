#include<bits/stdc++.h>  // 万能头文件 
using namespace std;

int gcd(int a,int b){     
    return b?gcd(b,a%b):a;    //递归法求最大公约数
}
int main(){
	int a, b;
	cin >> a >> b;
	cout << gcd(a,b);
	
	return 0;
}
