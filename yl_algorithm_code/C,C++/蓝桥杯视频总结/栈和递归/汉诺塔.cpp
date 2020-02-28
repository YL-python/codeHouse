#include <iostream>
#include <string>
#include <stack>
using namespace std;

stack<int > s[3];  // 表示三根柱子 

void move(int x, int y){
	int temp = s[x].top();
	s[x].pop();
	s[y].push(temp);
	cout << x << " --> " << y << endl;
}

// 从 A 到 C 经过 B 移动 N 个圆盘 
void hanoi(int A, int B, int C, int n){
	if(n == 1){
		move(A, C);
		return;
	} 
	hanoi(A, C, B, n-1);  // 把 N-1 个盘子从 A 借助 C 移动到 B 上 
	move(A, C);  // 把 A 上最后一个盘子移动到 C 上 
	hanoi(B, A, C, n-1);  // 把 B上 n-1个 盘子借助 A 移动到 C 上  
} 

int main(){
	
	int n;
	cin >> n;
	for (int i=n;i>=1;i--){
		s[0].push(i);    // 把 n 个圆盘放在第一根柱子上 
	}
	
	hanoi(0, 1, 2, n);
	cout << endl << "C柱子上的元素是：" << endl;
	
	while(!s[2].empty()){
		cout << s[2].top() << " ";
		s[2].pop();
	} 
	
	// 移动n号盘子花费n点体力   求移动n个盘子要的步数和体力
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
移动步数 
f[1] = 1

n 个盘子，先移 n-1 个，在移动一个 在移动 n-1个 
f[n] = f[n-1] + 1 + f[n-1] 
f[n] = pow(2, n-1) - 1 
f[n] = (1LL << n) - 1   // 位运算

花费的体力
g[n] = g[n-1] + n + g[n-1] 

 
*/



























