#include <stdio.h>
#include<iostream>
using namespace std;
int a,cnt,n;
char s;
int main(){
	cin>>n>>s;
//	printf("%d  %c\n",n,s);
	for(int i=1;i<50;i++){
		a=i*i*2-1;
		if(a>n){
			a=i-1;	
			break;
		}	
	}
	cnt=n-(a*a*2-1);
	//printf("%d????%d\n",a,cnt); 
	for(int i=1;i<=a;i++){
		for(int j=1;j<i;j++){
			printf(" ");
		}
		for(int k=i;k<=2*a-i;k++){
			printf("%c",s);
		}
			putchar(10);	
	}
	for(int i=1;i<a;i++){
		for(int j=i;j<=a-2;j++){
			printf(" ");
		}
		for(int k=1;k<=2*i+1;k++){
			printf("%c",s);
		}if(i!=a){
			putchar(10);	
		}
	}
	cout << cnt;
	return 0;
}
