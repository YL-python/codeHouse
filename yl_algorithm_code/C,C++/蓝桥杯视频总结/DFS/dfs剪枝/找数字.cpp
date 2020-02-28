#include <iostream>
#include <string>

using namespace std;

int n;
bool ok=false;

void dfs(long long x, int cnt){
	if(cnt >= 19){
		return;
	}
	if(ok){
		return;
	}
	if(x % n == 0){
		ok = true;
		cout << x << endl;
		return;
	}
	dfs(x * 10 + 0, cnt + 1);
	dfs(x * 10 + 1, cnt + 1);
}

int main(){
	cin >> n;
	dfs(1,0);
	return 0;
}
/*
��һ����n,�����ҳ�һ��ֻ��0, 1��ɵ�ʮ����
��m��Ҫ�����������m���Ա�n������
�����ʽ
����-������n(1��n < 200)��
�����ʽ
������������n��ÿһ��ֵ�����m����Ӧֵ, .
��֤��-�����ֳ���С��19λ�����֡������-
������ֵn�ж���⣬�����κ�һ�����ǿ��Խ���
�ġ�

*/



























