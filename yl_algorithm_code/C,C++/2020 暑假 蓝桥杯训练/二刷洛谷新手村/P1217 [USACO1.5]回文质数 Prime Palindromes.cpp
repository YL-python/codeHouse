#include <cstdio>

int a,b;

bool ss_book[10000001];

void make_ss() {
	ss_book[0]=ss_book[1] = false;
	for(int i=2; i<=9999999; i++) {
		for(int j=i*2; j<=9999999; j+=i) {
			ss_book[j] = true;
		}
	}
}

bool huiwen(int x) {
	int temp = x;
	int cnt=0;
	while(temp) {
		cnt = cnt*10 + temp%10;
		temp /= 10;
	}
	if(cnt == x) {
		return true;
	} else {
		return false;
	}
}

int main() {

	scanf("%d%d",&a,&b);
	//b<=10000000����ж��������ԣ�����11���⣬һ������λ����ż���Ļ���������Ϊ������������
	// ���һ������������λ����ż��������������λ�ϵ����ֺ���ż��λ�ϵ����ֺͱ�Ȼ��ȣ�
	// �����������������ۣ������ж����������϶��ܱ�11�������������Ͳ�������������
	if (b>=10000000)
		b=9999999;
	for(int i=a; i<=b; i++) {
		if(! ss_book[i]) {
			if(huiwen(i)) {
				printf("%d\n",i);
			}
		}
	}
	return 0;
}
