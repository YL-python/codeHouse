#include <iostream>
#include <string>
#include <stack>
#include <vector>
using namespace std;

int main() {

	int n;
	cin >> n;

	vector<int > a(n);

	// ������� a ����
	for(int i=0; i<n; i++) {
		cin >> a[i];
	}

	stack<int > s;
	int cur = 1;  // ��¼λ�ñ���
	int f = 1;   // �Ƿ���԰� a ˳���ջ

	// һ��ջ ���ǿ�  
	for(int i=0; i<n; i++) {
		// ��ջ���ǲ��� a[i] ���ǾͰ� cur ��ջ 
		// while ѭ���ҵ�ջ����a[i]��ʱ���ֹͣ��վ�����ҿ������� n ���� 
		while((s.empty() || s.top() != a[i]) && cur<=n){
			s.push(cur);
			cur++;  // �� 1~n ��˳���վ 
		}
		// ��վ�������֮�� ���ջ������ a[i] �����ǿ�ջ��ʾ���ܰ� a ˳���վ 
		if (s.empty() || s.top()!=a[i]){
			f = 0;
			break;
		}else{
			s.pop();
		}
	}

	if(f){
		cout << "����    �� a ˳���վ" << endl;
	}else{
		cout << "������    �� a ˳���վ" << endl;
	}

	return 0;
}
/*
�� n ��������ջ˳���� 1��2��3...n
�ٸ�һ������ a
�жϳ�ջ˳���Ƿ������ a
*/



























