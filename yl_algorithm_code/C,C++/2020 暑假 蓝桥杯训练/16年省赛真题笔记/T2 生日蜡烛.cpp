#include<cstdio>
int main() {
	for(int i=0; i<=150; i++) {
		int temp = i,sum = 0;
		while(sum < 236) {
			sum+=temp;
			temp++;
		}
		if(sum == 236) {
			printf("%d到%d岁之间一共吹了236根蜡烛",i,temp-1);
		}
	}
	return 0;
}
