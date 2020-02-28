#include <iostream>
using namespace std;
int main(){
	int f[15];
	f[1] = 1;
	f[2] = 2;
	f[3] = 4;
	f[4] = 8;
	f[5] = 0;
	f[7] = 0;
	
	for(int i=6;i<=10;i++){
		if(i == 7){
			f[7] = 0;
			continue;
		}else{
			f[i] = f[i-1] + f[i-2] + f[i-3] + f[i-4]; 
		}
	}
	cout << f[10] ;
	return 0;
} 
