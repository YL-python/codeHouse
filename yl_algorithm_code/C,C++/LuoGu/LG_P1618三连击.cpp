#include <iostream>
#include <algorithm>

using namespace std;

int a,b,c,k,sum,flag;
int vis[10];

void caijie(int x){
	while(x){
		vis[x%10] = 1;
		x/=10;
	}
}

int main(){
	
	cin >> a >> b >> c;
	int k = __gcd(a,__gcd(b,c));
	a/=k,b/=k,c/=k;
	for(int i=1;i<1000;i++){
		if(i*a>=1000 || i*c>=1000 || i*b>=1000 ){
			break;
		}
		for(int j=0;j<10;j++){
			vis[j] = 0;
		}
		caijie(i*a);
		caijie(i*b);
		caijie(i*c);
		sum = 0;
		for(int j=1;j<10;j++){
			sum += vis[j];
		}	
		if(sum == 9){
			cout << i*a << " " << i*b << " " << i*c << endl;
			flag = 1;
		}
	}
	
	if(!flag){
		cout << "No!!!";
	}
	return 0;
}




























