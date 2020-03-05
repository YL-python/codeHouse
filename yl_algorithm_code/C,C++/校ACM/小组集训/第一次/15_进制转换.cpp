#include <iostream>
using namespace std;

long long ten = 0;  // �м� 10 ������
int ans[1000];
int xiabiao = 0;
char i2s[17] = {'0','1','2','3','4','5','6','7','8','9','A','B','C','D','E','F','G'};

// �ַ���ת int
int str2int(char x) {
	if(x - '0' >=0 && x - '0'<=9) {
		return x - '0';
	} else {
		switch(x) {
			case 'A':case 'a':return 10;break;
			case 'B':case 'b':return 11;break;
			case 'C':case 'c':return 12;break;
			case 'D':case 'd':return 13;break;
			case 'E':case 'e':return 14;break;
			case 'F':case 'f':return 15;break;
			case 'G':case 'g':return 16;break;
		}
	}
}

int main () {
	int a,b;
	string num;
	cin >> a >> num >> b;
	
	// n ����ת 10 ����
	for(int i=0;i<num.length();i++){
		ten = ten*a + str2int(num[i]);
	}
	
	// 10 ����ת n ����  ÿһλֵ�浽 ans������ 
	while(ten) {
		ans[xiabiao++] = ten % b;
		ten /= b;
	}
	
	for(int i = xiabiao-1; i>=0;i--){
		cout << i2s[ans[i]]; // �ɶ�Ӧλ��ֵ ת�� �ַ������ 
	}
	return 0;
}
