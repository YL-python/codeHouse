#include <iostream>
using namespace std;

int CompactIntegers(int a[],int n){
	int temp = 0;
	for(int i=0;i<n;i++){
		if(a[i] != 0){
			a[temp++] = a[i];
		}
	}
	return temp;
}

int main() {
	int n;
	cin >> n; 
	int *a = new int[n];  // �����볤��Ϊn������ 
	// int *a = new int(n);   ����n��ʼ������
	
	for(int i=0;i<n;i++){
		cin >> a[i]; 
	}
	
	int cnt = CompactIntegers(a, n);
	cout << cnt << endl;
	for(int i =0 ;i<cnt;i++){
		cout << a[i] << " ";
	}
	return 0;
}




