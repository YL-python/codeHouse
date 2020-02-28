#include <iostream>

using namespace std;

double s,x,a,b,m=0.0,v=7.0; 


int main(){
	cin >> s>> x;
	a = s-x;
	b = s+x;
	while(1){
		if(m > b){
			cout << "n";
		}else if(m>a){
			m= m + v;
			if(m>b){
				cout << "n";
				break;
			}else{
				cout << "y";
				break;
			}
		}
		m += v;
		v*=0.98;
	}
	return 0;
}




























