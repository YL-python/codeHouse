#include <stdio.h>

float a,b;

int main() {
	scanf("%f%f",&a,&b);
	if(b<0) {
		printf("%.0f/(%.0lf)=%.2f",a,b,a/b);
	} else if(b == 0) {
		printf("%.0f/%.0f=Error",a,b,a/b);
	} else {
		printf("%.0f/%.0lf=%.2f",a,b,a/b);
	}
	return 0;
}

