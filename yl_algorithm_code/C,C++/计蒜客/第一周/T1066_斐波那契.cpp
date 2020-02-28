#include <iostream>
using namespace std;
int a[50];
void fb(){
	a[1] = 1;
	a[2] = 1;
	for(int i=3;i<=46;i++){
		a[i] += a[i-1] + a[i-2];
	}
}
int main(){
	int n;
	fb();
	cin >> n;
	cout << a[n];
	return 0;
} 
