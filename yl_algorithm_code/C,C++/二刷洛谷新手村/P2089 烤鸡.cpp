#include <cstdio>

using namespace std;

int n,ans[10005][10],temp,a[10];

void dfs(int index,int sum,int cnt) {
	if(cnt == 10) {
		if(sum == n) {
			for(int i=0; i<10; i++) {
				ans[temp][i] = a[i];
			}
			temp++;
		}
		return ;
	}
	a[index] = 1;
	dfs(index+1,sum+1,cnt+1);
	a[index] = 2;
	dfs(index+1,sum+2,cnt+1);
	a[index] = 3;
	dfs(index+1,sum+3,cnt+1);
}

int main() {
	scanf("%d",&n);
	if(n > 30 || n<10) {
		printf("0");
		return 0;
	} else {
		dfs(0,0,0);
	}
	printf("%d\n",temp);
	for(int i=0; i<temp; i++) {
		for(int j=0; j<10; j++) {
			printf("%d ",ans[i][j]);
		}
		printf("\n");
	}
	return 0;
}
