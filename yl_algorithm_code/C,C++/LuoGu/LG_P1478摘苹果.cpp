#include <iostream>
#include <string>

using namespace std;

int x[5005],y[5005];

int main(){
	int n,s,a,b,ans = 0;
	cin >> n >> s;
	cin >> a >> b;
	for(int i=0;i<n;i++){
		cin >> x[i] >> y[i];
	}
	for(int i=0;i<n-1;i++){
		for(int j=i+1;j<n;j++){
			int t,k;
			if(y[j] < y[i]){
				t = y[j];
				k = x[j];
				y[j] = y[i];
				x[j] = x[i];
				y[i] = t;
				x[i] = k;
				
			}
		}
	}
//	cout << "---------\n";
//	for(int i=0;i<n;i++){
//		cout << x[i] << " " << y[i] << endl; 
//	}
	
	for(int i=0;i<n;i++){
		if(x[i] <= a+b && s >= y[i]){
			s -= y[i];
			ans ++;
//			cout << x[i] << " " << y[i] << endl; 
			continue;
		}
		if(s < y[i]){
			break;
		}
	}
	cout << ans;
	
	return 0;
}




























