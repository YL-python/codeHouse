#include <cstdio>

int a,b,c;
int map[10] = {0},flag=1;

void fun(int x,int y,int z) {
	int _x=x, _y=y, _z=z;
	int temp = 0;
	for(int i=0; i<10; i++) {
		map[i] = 0;
	}
	while(x) {
		map[x%10] = 1;
		x/=10;
	}
	while(y) {
		map[y%10] = 1;
		y/=10;
	}
	while(z) {
		map[z%10] = 1;
		z/=10;
	}
	for(int i=0; i<10; i++) {
		temp+=map[i];
	}
	if(temp == 9) {
		flag = 0;
		printf("%d %d %d\n",_x,_y,_z);
	}
}

int main() {

	scanf("%d%d%d",&a,&b,&c);

	for(int i=111; i<=333; i++) {
		if(i*c < 1000) {
			fun(i*a,i*b,i*c);
		}
	}
	if(flag)
		printf("No!!!");

	return 0;
}
