#include <iostream>
#include <cmath> 
using namespace std;
int main(){
	int n;
	double ans,r,d,x,y;
	cin >> n;
	for(int i=0;i<n;i++){
		cin >> x >> y >> r;
		d = 0.04 * sqrt(x*x + y*y);
		ans += (d + r*1.5);
	}
	cout << ceil(ans)<< endl;
	return 0;
} 
