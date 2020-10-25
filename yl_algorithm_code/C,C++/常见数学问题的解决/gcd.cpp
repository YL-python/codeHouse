#include<bits/stdc++.h>  // 万能头文件 
using namespace std;

// 最大公因数 
int gcd(int a,int b){     
    return b?gcd(b,a%b):a;    //递归法求最大公约数
}

// 最小公倍数 
int lcm(int a,int b){
	// 这个写法比a*b/gcd(a,b)要好 
	return a/gcd(a,b)*b;  
} 

int main(){
	int a, b;
	cin >> a >> b;
	cout << gcd(a,b);
	
	return 0;
}
