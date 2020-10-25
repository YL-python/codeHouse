#include <cstdio>

int runnina(int y){
	return y % 400 == 0 || (y % 4==0 && y % 100 != 0);
} 

int main() {
	printf("%d\n",runnina(2000));
	printf("%d\n",runnina(1999));
	printf("%d\n",runnina(2004));
	return 0;
}
