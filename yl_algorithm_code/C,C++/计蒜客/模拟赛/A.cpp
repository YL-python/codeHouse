#include <iostream>
using namespace std;

int shushu[100005];

void make(){
	for(int i=2;i<100005;i++){
		if(shushu[i]==0){
			for(int j=i+i;j<=100005;j+=i){  // 吧不是0的数的所有倍数去除 
				shushu[j] = 1;
			}
		}
	}
}

bool youqu(int x){
	int cnt;
	while(x){
		cnt = x%10;
		x/=10;
		if(cnt == 5){
			return true;
		}
	}
	return false;
}

int main(){
	make();
	int ans = 0;
	for(int i=5;i<=100000;i++){
		if(shushu[i] == 0){
			if(youqu(i)){
				ans ++;
				cout << i << "-->" << ans << endl;
			}
		}
	}
	
	return 0;
} 
