#include <iostream>
#include <climits>
#include <cmath>
using namespace std;

const int N = 1000;
// f1 f2 f3 ��ʾ1 2 3���ֻ�ʱ��1�ɵ��������
int f1[N+1],f2[N+1],f3[N+1];

int main() {
	// ֻ��һ���ֻ�������£���������ֻ���Ǵӵ�һ�㿪ʼһ��һ�����ϲ���
	// �������������� i
	for(int i=1; i<=N; i++) {
		f1[i] = i;
	}

	// �����ֻ������
	for(int i=1; i<=N; i++) {
		int ans = INT_MAX;
		for(int j=1; j<=i; j++) {
			// min �����Ų���  max������
			// ��j����� ˤ������ ��Ҫ���� f1[i-j]  ûˤ����� f2[j-1]
			ans = min(ans,1+max(f1[i-j],f2[j-1]));
		}
		f2[i] = ans;
	}
	// �����ֻ������
	for(int i=1; i<=N; i++) {
		int ans = INT_MAX;
		for(int j=1; j<=i; j++) {
			ans = min(ans,1+max(f2[i-j],f3[j-1]));
		}
		f3[i] = ans;
	}
	printf("%d",f3[1000]);
	return 0;
}
