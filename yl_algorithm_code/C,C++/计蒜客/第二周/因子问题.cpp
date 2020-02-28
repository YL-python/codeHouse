#include <iostream>
using namespace std;
long long n,m,a;
int main() {
	cin >> n >> m;
	for(int i=1;i<=n;i++){
		if(m == i){
			continue;
		}
		if(n % i == 0 && n % (m-i) == 0){
			a=i;
			break;
		}
	}
	if(a!=0){
		cout << a;
	}else{
		cout << -1;
	}
	
	return 0;
}
