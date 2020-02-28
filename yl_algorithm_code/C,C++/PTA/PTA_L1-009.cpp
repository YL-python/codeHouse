#include<iostream>
using namespace std;

int numup[105],numdown[105],n;
char c;

int gcd(int a,int b){
	return b?gcd(b,a%b):a;
} 

int main(){
	cin >> n;
	for(int i=0;i<n;i++){
		cin >> numup[i] >> c >> numdown[i];
	}
	
	int up = numup[0], down = numdown[0];
	for(int i=1;i<n;i++){  // ��˷���� 
	
		up = up*numdown[i] + numup[i]*down;
		down = down*numdown[i];
		
		int x = gcd(up,down);  // ��ֹ��̫�󳬹�int���� 
		if(x < 0){  // �������� 
			x*=-1;
		}
		up /= x;
		down /= x;
	}
	
	if(up == 0){  // ����0���� 
		cout<< 0;
		return 0;
	}
	
	if(up<0){  // ���Ǹ������� 
		cout<<"-";
		up*=-1;
	}
	
	int x = gcd(up,down);  // �𰸻��� 
	up = up/x;
	down = down/x;

	if(up>down){  // ���Ӵ��ڷ�ĸ 
		int A = up/down;
		if(up%down == 0){  // �����Ƿ�ĸ�������� 
			cout<<A;
		}else{  // ���Ӳ��Ƿ�ĸ�������� 
			cout<<A<<" "<< up-(A*down)<< "/"<<down;
		}
	}else{  // ����С�ڷ�ĸ����� 
		cout<< up << "/"<<down;
	}
	return 0;
} 
