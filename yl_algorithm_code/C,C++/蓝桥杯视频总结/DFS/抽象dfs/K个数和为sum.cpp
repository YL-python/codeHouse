#include <iostream>
#include <string>

using namespace std;

int n, k, sum, ans;
int a[40];

// i表示当前正在选取第几个数，-个cnt表示选取了几个数，-个s表示选取的数的和值。
void dfs(int i,int cnt,int s){
	if(i == n){
		if(cnt == k && s == sum){
			ans++;
		}
		return;
	}
	if(cnt > k || s > sum){
		return;
	}
	dfs(i+1, cnt, s);
	dfs(i+1, cnt+1, s+a[i]);
}

int main(){
	
	cin >> n >> k >> sum;
	for(int i=0;i<n;i++){
		cin >> a[i];
	}
	ans = 0;
	dfs(0, 0, 0);
	cou << ans << endl;
	return 0;
}
/*
给定n个整数，要求选出K个数，使得选出来的K个数的和为sum。

对于每一个数， 枚举选或者不选两种情况，我们可以用dfs思想来完成这样的枚举过程。
我们在搜索的过程中，用S来记录当前选择的数值总和，k来记录选择的数的个数，
deep 表示当前正在枚举第几个数是否选择。
在第一层dfs的时候，我们可以枚举是否选第一个数，如果选第一个数则让S加上第一个数且k加一，dfs进入到下一层;否
则dfs直接进入到下一层。当然，这里我们还需要借助全局变量、参数或修改数组中元素的值等方式来标识出当前的层数，为
了减少篇幅，在下文中就直接忽略掉了。.
在第二层，对第二个数做同样的处理，dfs 的过程中记录已经选取的数的个数，如果已经选取了k个数，判断S值是否等于
sum。对于每一-层，我们都有两个选择一选和不选。 不同的选择，都会使得搜索进入完全不同的分支继续搜索。

5 3 9
1 2 3 4 5

2
*/



























