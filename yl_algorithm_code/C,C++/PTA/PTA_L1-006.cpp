#include <iostream>
#include <cmath>
using namespace std;
int n;
int start = 0;
int maxlen=0;
int len=0;
int main (){
	cin >> n;
	int sqrtn = sqrt(n);
	for(int i=2;i<=sqrtn;i++){
		int j=i;
		int t=n;
		len=0;
		while(t%j==0){
			t=t/j;
			j++;
			len++;
		}
		if(len>maxlen){
			start = i;
			maxlen=len;
		}
	}
	if(maxlen == 0){
		cout << 1 << endl << n;
	}else{
		cout<<maxlen<<endl<<start;
		for(int i=start+1;i<maxlen+start;i++){
			cout << "*" << i;
		}
	}
	
	return 0;
} 
