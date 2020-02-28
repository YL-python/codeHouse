#include <iostream>
#include <string>
using namespace std;

int main(){
	float m = 0.1;
	printf("%d\n",int(m));
	if(int(m) == m){
		printf("1");
	}else{
		printf("2");
	}
	return 0;
}

