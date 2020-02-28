#include<iostream>
#include<string> 
using namespace std;

char c[15][105];
string str;
int n;

int main(){
	cin >> n;
	getchar();
	getline(cin,str);
	int len = str.length();
	int row = len/n + len%n == 0 ? 0 : 1;
	
	for(int i=0;i<15;i++)
	{
		for(int j=0;j<105;j++)
			c[i][j]=' ';
	}

	
	int k=0;
	for(int i=row-1;i>=0;i--){
		for(int j=0;j<n;j++,k++){
			if(k>=len){
				c[j][i] = ' ';
			}else{
				c[j][i] = str[k];
			}
		}
	}
	
	for(int i=0;i<n;i++){
		for(int j = 0;j<row;j++){
			cout << c[i][j];
		}
		cout << endl;
	}
	
	return 0;
}

