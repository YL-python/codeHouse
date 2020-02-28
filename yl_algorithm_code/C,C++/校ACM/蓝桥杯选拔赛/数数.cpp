#include <iostream>
#include <string>
using namespace std;

long long T,n[15],ans[1000005][10000000000000]; 

int main(){
	int cnt;
	cin >> T;
	for(int i=0;i<T;i++){
		cin >> n[i];
		for(int j=0;j<n[i];j++){
			cin>>cnt;
			ans[i][cnt]++;
		}
	}
	for(int i=0;i<T;i++){
		int temp = n[i]/2;
		for(int j=0;j<n[i];j++){
			if(ans[i][j]>=temp){
				cout << j << endl;
				break;
			}
		}
	}
	return 0;
}

