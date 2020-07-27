#include <stdio.h>

int n,m,pep[100005],cnt;

int main() {

	scanf("%d",&n);
	for(int i=0; i<n; i++) {
		scanf("%d",&m);  // m 是人数
		for(int j=0; j<m; j++) {
			scanf("%d",&cnt);  // 当前号码
			if(m!=1) { // 只有一个人的时候是没有朋友圈的
				pep[cnt] = 1;  // 把这个号码标记为有朋友圈
			}
		}
	}
	scanf("%d",&m);  // 要检查的人数
	int flag = 0;
	for(int i=0; i<m; i++) {
		scanf("%d",&cnt);  // 当前检查的号码
		if(pep[cnt] == 0) {  // 这个人没有朋友圈
			if(flag!=0) {  // 防止第一个 空格
				printf(" ");
			}
			printf("%05d",cnt);
			pep[cnt] = 1; // 防止一个人被多次输出
			flag++;
		}
	}
	if(flag==0)  {
		printf("No one is handsome");
	}
	return 0;
}
