#include <iostream>
#include <string.h>
using namespace std;

int n,a[10000];
int main(){
	cin >> n;
	for(int i=0;i<n;i++){
		cin >> a[i];
	}
	for(int i=0;i<n;i++){
		int ans=0,x=a[i];
		while(x){
			ans = ans*10 + (x%10);
			x/=10;
		}
		cout << ans<<endl;
	}
	return 0;
}
/*
Description
请将一个正整数反转，如果反转之后前面有0，请去除再输出。

Input
第一行为一个T ，代表T组数，随后T行每行一个n(n<=100000)。

Output
输出n反转之后的答案

Sample Input 1 
2
66
660

Sample Output 1
66
66
*/
