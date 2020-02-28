#include <iostream>
#include <string>

using namespace std;

long long jiechen(int x){
	
	// 定义边界条件 
	if(x <= 1){
		return 1;
	}
	
	return x * jiechen(x-1);
}

int main(){
	
	int a = 4;
	cout << jiechen(a) << endl;
	
	return 0;
}




































