#include <iostream>
#include <string>

using namespace std;

int n;

int f(int x){
	if(x == n){
		return 1;
	}else{
		return (f(x + 1) + 1) * 2;
	}
}

int main(){
	
	scanf("%d",&n);
	printf("%d\n",f(1)); 
	
	return 0;
}
/*
��ͷ������һ�����Ӳ�֪���������� 1 �����һ��.
�����ӣ�������񫣬�ֶ����һ�����Ժ���ÿ���
ʣ�µ����ӵ� 1�� ����һ������ n ��ֻʣ��һ����
���ˡ���ͷ����֪�� 1 ��ʼ���˶������ӡ�
*/ 



























