#include<stdio.h>
int main() {
	int start,end,sum=0,cnt=1;
	// ��������� C��printf ������

	scanf("%d %d",&start,&end);
	for(int i=start; i<=end; i++) {
		if(cnt%6==0) {
			printf("\n");
			cnt=1;
		}
		printf("%5d",i);
		cnt++;
		sum+=i;
	}
	printf("\nSum = %d",sum);

	return 0;
}








