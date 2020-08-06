#include <iostream>
using namespace std;
int a[10]= {0},cnt,b,c;
int main() {
	for(int i=123; i<334; i++) {
		cnt=0;
		b=i*2;
		c=i*3;
		a[i%10]=1;
		a[i/10%10]=1;
		a[i/100]=1;
		a[b%10]=1;
		a[b/10%10]=1;
		a[b/100]=1;
		a[c%10]=1;
		a[c/10%10]=1;
		a[c/100]=1;
		for(int j=1; j<=9; j++) {
			cnt+=a[j];
		}
		if(cnt==9) {
			cout << i << " " << i*2 << " " << i*3 << endl;
		}
		cnt=0;
		for(int j=1; j<=9; j++) {
			a[j]=0;
		}
	}
	return 0;
}

