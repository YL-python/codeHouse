#include <stdio.h>

int main() {
	int h,m,temp;
	scanf("%d:%d",&h,&m);
	temp = h;
	temp-=12;
	m?temp+=1:1;

	if(temp>0) {
		for(int i=0; i<temp; i++) {
			printf("Dang");
		}
	} else {
		printf("Only %02d:%02d.  Too early to Dang.",h,m);
	}

	return 0;
}
