#include <cstdio>

int a[105],temp,cnt=0;

int main() {


	while(1) {
		scanf("%d",&temp);
		if(temp == 0) {
			break;
		} else {
			a[cnt++] = temp;
		}
	}

	for(int i=cnt-1; i>=0; i--) {
		printf("%d ",a[i]);
	}
	return 0;
}
