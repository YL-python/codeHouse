#include <iostream>
using namespace std;

// 理解二叉树，知道每一层有几个节点
// 第一层 1个结点 
// 第二层 2个结点  
// 第三层 4个结点 
// 。。。 
// 第n层 2^(n-1) 个结点 

long long vis[18]; 

// 求x 在哪一层上 
int chen(int x){
	int c=0;
	while(x){
		x/=2;
		c++;
	}
	return c;
}

main(){
	
	int n;
	cin >> n;
	int a[100005];
	for(int i=1;i<=n;i++){
		cin >> a[i];
		vis[chen(i)] += a[i];
	}
	int max_chen = chen(n); 
	int ans = 1;
	int ans_sum = vis[1];
	for(int i=1;i<=max_chen;i++){
		if(ans_sum < vis[i]){
			ans_sum = vis[i];
			ans = i;
		}
	}
	cout << ans;
	return 0;
} 
/*
 给定一棵包含 N 个节点的完全二叉树，树上每个节点都有一个权值，按从
 上到下、从左到右的顺序依次是 A 1 , A 2 , ··· A N ，如下图所示：
 现在小明要把相同深度的节点的权值加在一起，他想知道哪个深度的节点
 权值之和最大？如果有多个深度的权值和同为最大，请你输出其中最小的深度。
 注：根的深度是 1。
 【输入格式】
 第一行包含一个整数 N。
 第二行包含 N 个整数 A 1 , A 2 , ··· A N 。
 【输出格式】
 输出一个整数代表答案。
 【样例输入】
 7
 1 6 5 4 3 2 1
 【样例输出】
 2
  【评测用例规模与约定】
 对于所有评测用例，1 ≤ N ≤ 100000，-100000 ≤ A i ≤ 100000。
*/ 
