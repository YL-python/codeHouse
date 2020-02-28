#include<iostream>
using namespace std;

int n;
float pep[15][2];
char c;

int main(){
	cin >> n;
	for(int i =0;i<n;i++){
		cin >> c;
		if(c == 'M'){
			pep[i][0] = 1.0;
		}else{
			pep[i][0] = 0.0;
		}

		cin >> pep[i][1];
	}
	for(int i=0;i<n;i++){
		if(pep[i][0] == 1.0){
			printf("%.2f\n",pep[i][1]/1.09);
		} else{
			printf("%.2f\n",pep[i][1]*1.09);
		}
	}
	
	return 0;
}
