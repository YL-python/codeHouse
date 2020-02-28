#include <iostream>
using namespace std;
int main(){
	int t,n;
	cin >> t;
	for(int i=0;i<t;i++){
		cin >> n;
		if(n % 7 == 0){
			cout << "Yes." << "\n";
		}else{
			cout << "No." << "\n";
		}
	} 
	return 0;
} 
