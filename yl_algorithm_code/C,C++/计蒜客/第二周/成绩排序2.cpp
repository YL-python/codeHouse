#include <iostream>
#include <string.h>
using namespace std;

char name[20][100];
int score[20];

int main() {
	int n;
	cin >> n;
	for(int i=0;i<n;i++){
		cin >> name[i] >> score[i];
	}
	
	int temp;
	char stemp[20];
	for(int i=0;i<n-1;i++){
		for(int j=i+1;j<n;j++){
			if(score[j] > score[i]){
				temp = score[j],score[j]=score[i],score[i]=temp;
				strcpy(stemp,name[i]);
				strcpy(name[i],name[j]);
				strcpy(name[j],stemp);
			}
			if(score[j] == score[i] && strcmp(name[i],name[j])>0){
				strcpy(stemp,name[i]);
				strcpy(name[i],name[j]);
				strcpy(name[j],stemp);
			}
		}
	}
	
	for(int i=0;i<n;i++){
		cout << name[i] << " " << score[i] << endl;
	}
	return 0;
}
