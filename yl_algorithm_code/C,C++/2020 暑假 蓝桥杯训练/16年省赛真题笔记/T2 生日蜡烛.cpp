#include<cstdio>
int main() {
	for(int i=0; i<=150; i++) {
		int temp = i,sum = 0;
		while(sum < 236) {
			sum+=temp;
			temp++;
		}
		if(sum == 236) {
			printf("%d��%d��֮��һ������236������",i,temp-1);
		}
	}
	return 0;
}
