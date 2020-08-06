#include <cstdio>

int n,x,ans=0;

int main() {

	scanf("%d%d",&n,&x);

	for(int i=1; i<=n; i++) {
		int temp = i;
		while(temp) {
			if(temp % 10 == x)
				ans++;
			temp /=10;
		}
	}
	printf("%d",ans);
	return 0;
}
