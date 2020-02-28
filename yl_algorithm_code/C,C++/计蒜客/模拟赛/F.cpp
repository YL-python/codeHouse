#include <iostream>
using namespace std;

long long a[2000005];

int main(){
	long long A, B, C;
	long long cnt = 1;
	bool flag = false;
	
	cin >> A >> B >> C;
	a[0] = 1;
	cnt %= C;
	for(int i=1;i<=2000000;i++){
		cnt %= C;
		cnt = ((A%C) * (cnt%C) + (cnt % B)) % C;
		cnt %= C;
//		cout << cnt << endl;
		if(a[cnt]){
//			cout << "ANS:" << i ;
			cout << i ;
			flag = true;
			break;
		}else{
			a[cnt] = 1;
		}
	}
	if(! flag){
		cout << -1;
	}
	return 0;
} 
