#include <iostream>
#include <string>
#include <stack>
using namespace std;

stack<int > s[3];  // ��ʾ�������� 

void move(int x, int y){
	int temp = s[x].top();
	s[x].pop();
	s[y].push(temp);
	cout << x << " --> " << y << endl;
}

// �� A �� C ���� B �ƶ� N ��Բ�� 
void hanoi(int A, int B, int C, int n){
	if(n == 1){
		move(A, C);
		return;
	} 
	hanoi(A, C, B, n-1);  // �� N-1 �����Ӵ� A ���� C �ƶ��� B �� 
	move(A, C);  // �� A �����һ�������ƶ��� C �� 
	hanoi(B, A, C, n-1);  // �� B�� n-1�� ���ӽ��� A �ƶ��� C ��  
} 

int main(){
	
	int n;
	cin >> n;
	for (int i=n;i>=1;i--){
		s[0].push(i);    // �� n ��Բ�̷��ڵ�һ�������� 
	}
	
	hanoi(0, 1, 2, n);
	cout << endl << "C�����ϵ�Ԫ���ǣ�" << endl;
	
	while(!s[2].empty()){
		cout << s[2].top() << " ";
		s[2].pop();
	} 
	
	// �ƶ�n�����ӻ���n������   ���ƶ�n������Ҫ�Ĳ���������
	long long f[65],g[65]
	f[1] = 1,g[1] = 1;
	for(int i=2;i<=n;i++){
		f[i] = 2 * f[i - 1] + 1;
	} 
	for(int i=2;i<=n;i++){
		g[i] = 2 * g[i - 1] + i;
	} 
	printf("\n%lld %lld\n", f[n], g[n]);
	
	return 0;
}
/*
�ƶ����� 
f[1] = 1

n �����ӣ����� n-1 �������ƶ�һ�� ���ƶ� n-1�� 
f[n] = f[n-1] + 1 + f[n-1] 
f[n] = pow(2, n-1) - 1 
f[n] = (1LL << n) - 1   // λ����

���ѵ�����
g[n] = g[n-1] + n + g[n-1] 

 
*/



























