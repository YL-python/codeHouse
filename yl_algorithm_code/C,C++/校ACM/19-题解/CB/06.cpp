#include <iostream>
using namespace std;

long long ans=0;

bool have(int x){
	int temp;
	while(x){
		temp = x%10;
		if(temp == 2 || temp == 0 || temp == 1 || temp == 9){
			return true;
		}
		x/=10;
	}
	return false;
}

main(){
	int n;
	cin >> n;
	for(int i=1;i<=n;i++){
		if(! have(i)){
			ans += i;
		}
	}
	cout << ans;
	return 0;
} 
/*
 С������λ�к��� 2��0��1��9 �����ֺܸ���Ȥ��������ǰ�� 0�� ���� 1 ��
 40 �������������� 1��2��9��10 �� 32��39 �� 40���� 28 �������ǵĺ��� 574��
 ���ʣ��� 1 �� n �У��������������ĺ��Ƕ��٣�
*/ 
