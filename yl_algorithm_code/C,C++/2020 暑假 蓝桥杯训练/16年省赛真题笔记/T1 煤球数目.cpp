#include<cstdio>
int main() {
	int now=0,ans=0,temp=1;
	for(int i=1; i<=100; i++) {
		now += temp;
		temp ++ ;
		ans += now;
	}
	printf("%d",ans);
	return 0;
}
