#include <iostream>
#include <string>

using namespace std;

int mod = 1000007; 

// 递归方法  O(3N方) 而且空间更大 栈空间 
int louti_1(int x){
	if(x < 0){
		return 0;
	}
	if(x == 0 || x == 1){
		return 1;
	}
	if(x == 2){
		return 2;
	}
	return louti_1(x - 1) % mod + louti_1(x - 2) % mod + louti_1(x - 3) % mod;
}

// 迭代方法   O(N) 
int louti_2(int x){
	if(x < 0){
		return 0;
	}
	if(x == 0 || x == 1){
		return 1;
	}
	if(x == 2){
		return 2;
	}
	if(x == 3){
		return 4;
	}
	int x1=1,x2=2,x3=4;
	for(int i=4; i<=x; i++){
		int _x1 = x1;
		x1 = x2 % mod;
		x2 = x3 % mod;
		x3 = ((x1 + x2) % mod + _x1) % mod;
	}
	return x3;
}

int main(){
	
	int n = 7;
	
	cout << louti_1( 7 ) << endl;
	cout << louti_2( 7 ) << endl;
	
	return 0;
}




























