#include <cstdio>

double s,x,temp=7.0,cnt=0.0;
int ans=1;

int main() {

	scanf("%lf%lf",&s,&x);

	while(true) {
		if(cnt > s+x) { // 直接游出去了
			printf("n");
			return 0;
		} else if(cnt >= s-x && cnt <= s+x) {// 游到了
			// 再游一下看看
			cnt += temp;
			if(cnt > s+x) {
				printf("n");
				return 0;
			} else {
				printf("y");
				return 0;
			}
		}
		cnt+=temp;
		temp*=0.98;
	}
	return 0;
}
