#include <iostream>
#include <string>

using namespace std;

int a[20005], n; 
void ss(){
	a[0] = a[1] = 0;
	for(int i=2;i<20005;i++){
		a[i] = i;
	}
	for(int i=2;i<20005;i++){
		if(a[i] != 0){
			for(int j=i+i;j<20005;j+=i){
				a[j] = 0;
			}
		}
	}
}

int main(){
	ss();
	cin >> n; 
	for(int i=2;i<n-2;i++){
		if(a[i]){
			for(int j=2;j<n-2;j++){
				if(a[j]){
					int x = n-a[i]-a[j];
					if(a[x]){
						cout << a[i] << " " << a[j] << " " << a[x];
						return 0;
					}
				}
			}
		}
	}
	
	
	return 0;
}




























