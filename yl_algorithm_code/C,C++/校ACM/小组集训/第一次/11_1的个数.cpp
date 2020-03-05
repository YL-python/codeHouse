#include <iostream>
using namespace std;

int ans = 0;

void js(int x){
	while(x){
		if(x%10 == 1){
			ans++;
		}
		x/=10;
	}
}

int main (){
	int n;
	cin >> n;
	for(int i=1;i<=n;i++){
		js(i);
	} 
	cout << ans;
	return 0;
}
/*
输入正整数n，判断从1到n之中，数字1一共要出现几次。
例如1123这个数，则出现了两次1。
例如15，那么从1到15之中，一共出现了8个1。
*/
