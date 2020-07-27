#include <stdio.h>
int n,k,x,f[1005],cnt,max=-1;
int main(){
	scanf("%d",&n);
	for(int i=0;i<n;i++){
		scanf("%d",&k);
		for(int j=0;j<k;j++){
			scanf("%d",&x);
			f[x]++;
		}
	}
	for(int i=0;i<1001;i++){
		if(f[i]>=max){
			max=f[i];
			cnt=i;
		}
	}
	printf("%d %d",cnt,max);
	return 0;
}
