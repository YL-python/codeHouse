#include<iostream>
#include<string>
using namespace std;
int main(){
	int y,n;
	int a[10];
	cin >> y>>n;
	for(int i =y;y<=3000;i++){
		for(int j=0;j<10;j++){
			a[j] = 0;
		}
		int num = i;
		if(i<1000){
			a[0]=1;
		} 
		while(num>0){
			a[num%10] = 1;
			num = num / 10;
		}
		int sum=0;
		for(int j=0;j<10;j++){
			sum += a[j];
		}
		if(sum == n){
			printf("%d %04d",i-y,i);
			break;
		}
	}
	
	return 0;
}

