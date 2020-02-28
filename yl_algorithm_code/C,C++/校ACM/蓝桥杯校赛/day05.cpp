#include <iostream>
#include <string>
using namespace std;

int main(){
	int n,a[10005],max=-1;
	cin >> n;
	for(int i=0;i<n;i++){
		cin >> a[i];
	}
	
	for(int i=0;i<n;i++){
		int count=0;
		for(int j=i+1;j<n;j++){
			if(a[j]>a[j-1]){
				count++;
			}else{
				break;
			}
		}
		if(count>max){
			max=count;
		}
	}
	
	cout << max+1;
	
	return 0;
}

