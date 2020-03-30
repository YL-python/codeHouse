#include <iostream>
using namespace std;

int a[1000];

int main() {
	int n,j,b=0;
	cin >> n;
	a[999] = 1;
	for(int i=0;i<n;i++){  // n´Î·½ 
	 	j = 999;
	 	while(j>=0){
	 		int k = a[j] * 2 + b;
	 		a[j] = k % 10;
	 		b = k / 10;
	 		j --;
		}
	}
	int count;
	for (int i=0; i<1000; i++){
        if(a[i] != 0){
        	count =i;
        	break;
		}
    }
    for (int i=count; i<1000; i++){
        cout << a[i];
    }
    cout << endl;
	return 0;
}
