#include <iostream>
#include <string>
using namespace std;

int gcd(int x, int y){
    while(y^=x^=y^=x%=y);
    return x;
}

int lcm(int a,int b){
	return a/gcd(a,b)*b;
}

int main(){
	int a,b;
	cin >>a>>b;
	int m=0;
	for(int i=1;i<1000000;i++){
		m=lcm(a,b);
		m%2==0?a+=1:a+=a;
//		cout << "m="<<m<<endl; 
		if(a>=b){
			cout<<i;
			break;
		}
	} 
	return 0;
}


/*
Description

还是那个奇怪的细胞，营养液的数量与细胞数量的最小公倍数是奇数的话，细胞就会分裂成为原来的2倍，如果是偶数的话，细胞总数就只会加1个。每天给的营养液总是相同的，现在你想知道a个细胞在一定量的培养液下面最少多少天细胞总数才能不少于b个。


Input
只有一行，2个正整数a,b，用空格隔开（0<a<b<=2e9）


Output
输出细胞总数不少于b个至少要多少天。


Sample Input 1 

3 5
Sample Output 1

1
*/ 
