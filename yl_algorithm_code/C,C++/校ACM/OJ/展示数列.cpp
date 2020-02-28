#include <iostream>
using namespace std;
int main(){
	int a1,n,d;
	cin >> a1 >> d >> n;
	for(int i=1;i<=n;i++){
		cout << a1+d*(i-1) << " ";
	} 
	return 0;
} 
