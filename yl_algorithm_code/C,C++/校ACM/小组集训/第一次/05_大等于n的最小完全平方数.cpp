#include <iostream>
using namespace std;

int main (){
	long long x;
	cin >> x;
	for(long long i=0;i<=10000000000000;i++){
		if(i*i>=x){
			cout << i*i;
			break;
		}
	}
	return 0;
}
/*
��������n����С����ȫƽ������
��һ�����ܱ�ʾ��ĳ����Ȼ����ƽ������ʽ����������Ϊ��ȫƽ����
Tips��ע�����ݷ�Χ
*/
