#include <iostream>
using namespace std;

int main(){
	int n,m;
	cin >> n;
	int ans1=0,ans5=0,ans10=0;
	for(int i=0;i<n;i++){
		cin >> m;
		if(m == 1){
			ans1++;
		}
		if(m == 5){
			ans5++;
		}
		if(m == 10){
			ans10++;
		}
	}
	cout << ans1 << endl << ans5 << endl << ans10;
	return 0;
} 
