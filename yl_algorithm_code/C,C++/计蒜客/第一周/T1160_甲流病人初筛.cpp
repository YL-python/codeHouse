#include <iostream>
using namespace std;
string s, vis[205];
double w;
int k, n, ans; 
int main(){
	cin >> n;
	for(int i=0;i<n;i++){
		cin >> s >> w >> k;
		if(w >= 37.5 && k){
			vis[ans++] = s;
		}
	}
	for(int i=0;i<ans;i++){
		cout << vis[i] << endl;
	}
	cout << ans;
	return 0;
} 
