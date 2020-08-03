#include <cstdio>

int n,s,a,b,ans;
int x[5005];
int y[5005];

int main() {

	scanf("%d%d",&n,&s);
	scanf("%d%d",&a,&b);
	int h = a+b;

	for(int i=0; i<n; i++) {
		scanf("%d%d",&x[i],&y[i]);
		if(x[i] > h) {
			y[i] = 10000;
		}
	}

	for(int i=0; i<n-1; i++) {
		for(int j=i+1; j<n; j++) {
			int t,k;
			if(y[j] < y[i]) {
				t = y[j];
				k = x[j];
				y[j] = y[i];
				x[j] = x[i];
				y[i] = t;
				x[i] = k;
			}
		}
	}
//	printf("-------------\n");
//	for(int i=0; i<n; i++) {
//		printf("%d %d\n",x[i],y[i]);
//	}

	for(int i=0; i<n; i++) {
		if(x[i]<=h && s>=y[i]) {
			s-=y[i];
			ans++;
		}
		if(s < y[i]) {
			break;
		}
	}

	printf("%d",ans);
	return 0;
}
