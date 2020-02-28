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
	for(int i=1;i<n;i++){  // 碾乘法求和 
	
		up = up*numdown[i] + numup[i]*down;
		down = down*numdown[i];
		
		int x = gcd(up,down);  // 防止数太大超过int类型 
		if(x < 0){  // 负数处理 
			x*=-1;
		}
		up /= x;
		down /= x;
	}
	
	if(up == 0){  // 答案是0处理 
		cout<< 0;
		return 0;
	}
	
	if(up<0){  // 答案是负数处理 
		cout<<"-";
		up*=-1;
	}
	
	int x = gcd(up,down);  // 答案化简 
	up = up/x;
	down = down/x;

	if(up>down){  // 分子大于分母 
		int A = up/down;
		if(up%down == 0){  // 分子是分母的整数倍 
			cout<<A;
		}else{  // 分子不是分母的整数倍 
			cout<<A<<" "<< up-(A*down)<< "/"<<down;
		}
	}else{  // 分子小于分母的情况 
		cout<< up << "/"<<down;
	}
	return 0;
} 
