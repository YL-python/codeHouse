#include <iostream>
#include <string>

using namespace std;

long long fb(int x){
	if(x == 1 || x == 2){
		return 1; 
	} 
	return fb(x-1) + fb(x-2);
}

int main(){
	
	int a=5;
	cout << fb(a) << endl;
	system("pause");
	return 0;
}





























