#include <cstdio>

double a,b,c,d;

double f(double x) {
	return a*x*x*x+b*x*x+c*x+d;
}

void BinarySearch(double l,double r) {
	if(r-l <= 0.001) {
		printf("%.2lf ",l);
		return ;
	}

	double mid = l + (r-l) / 2;
	if(f(mid) == 0) {
		printf("%.2lf ",mid);
		return ;
	}
	// ֻҪ������ߵ�ֵ����  �ұߵ�ֵ����һ��ѭ����
	if(f(l) == 0) {
		printf("%.2lf ",l);
		return ;
	}
	if(f(l)*f(mid) < 0) {
		BinarySearch(l,mid);
	} else if(f(r)*f(mid)<0) {
		BinarySearch(mid,r);
	}
}

int main() {
	scanf("%lf%lf%lf%lf",&a,&b,&c,&d);
	for(double i=-100; i<=100; i++) {
		if( f(i)*f(i+1.0) <= 0 ) {
			BinarySearch(i,i+1.0);
		}
	}
	return 0;
}
