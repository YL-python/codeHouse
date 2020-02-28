#include <iostream>
using namespace std;

long long ans=0;

bool have(int x){
	int temp;
	while(x){
		temp = x%10;
		if(temp == 2 || temp == 0 || temp == 1 || temp == 9){
			return true;
		}
		x/=10;
	}
	return false;
}

main(){
	int n;
	cin >> n;
	for(int i=1;i<=n;i++){
		if(! have(i)){
			ans += i;
		}
	}
	cout << ans;
	return 0;
} 
/*
 小明对数位中含有 2、0、1、9 的数字很感兴趣（不包括前导 0） ，在 1 到
 40 中这样的数包括 1、2、9、10 至 32、39 和 40，共 28 个，他们的和是 574。
 请问，在 1 到 n 中，所有这样的数的和是多少？
*/ 
