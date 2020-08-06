#include <cstdio>

int ans=0,n,m;
// 7 => 0   6 => 6
int map[9] = {0,1,1,1,1,1,0};

int main() {

	scanf("%d%d",&n,&m);
	while(m--) {
		if(map[n%7] == 1) {
			ans+=250;
		}
		n+=1;
	}

	printf("%d",ans);

	return 0;
}
