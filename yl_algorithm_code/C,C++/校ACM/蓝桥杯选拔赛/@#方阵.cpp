#include <iostream>
#include <string>
using namespace std;
char s[5][5]; 
int main(){
	for(int i=0;i<5;i++){
		for(int j=0;j<5;j++){
			s[i][j] = '#';
		}
	}
	
	int n,a[25][2];
	cin>>n;
	for(int i=0;i<n;i++){
		cin>>a[i][0]>>a[i][1];
		s[a[i][0]-1][a[i][1]-1] = '@';
	}
	for(int i=0;i<5;i++){
		for(int j=0;j<5;j++){
			cout << s[i][j];
		}
		cout << endl;
	}
	
	return 0;
}

