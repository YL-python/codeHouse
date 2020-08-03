#include <cstdio>

int n,a,b,yina,yinb,pin;
int na[205],nb[205];

int map[5][5]= {
	2,0,1,1,0,
	1,2,0,1,0,
	0,1,2,0,1,
	0,0,1,2,1,
	1,1,0,0,2
};



int main() {

	scanf("%d%d%d",&n,&a,&b);
	for(int i=0; i<a; i++) {
		scanf("%d",&na[i]);
	}
	for(int i=0; i<b; i++) {
		scanf("%d",&nb[i]);
	}
	int _a = 0,_b = 0,_n = n;
	while(_n--) {
		if(map[na[_a]][nb[_b]] == 1) {
			yina++;
		}
		if(map[na[_a]][nb[_b]] == 2) {
			pin++;
		}
		_a++;
		_b++;
		if(_a == a) {
			_a = 0;
		}
		if(_b == b) {
			_b = 0;
		}
	}
	printf("%d %d",yina,n-yina-pin);
	return 0;
}

/*
#include <iostream>
#include <string>

using namespace std;

int n,a,b,pin,ans_a;
int na[205];
int nb[205];

void bisai(int x, int y){
	if(x == y){
		pin ++;
	}else if(x == 0 && y == 2 ){
		ans_a ++;
	}else if(x == 0 && y == 3){
		ans_a ++;
	}else if(x == 1 && y == 0){
		ans_a ++;
	}else if(x == 1 && y == 3){
		ans_a ++;
	}else if(x == 2 && y == 1){
		ans_a ++;
	}else if(x == 2 && y == 4){
		ans_a ++;
	}else if(x == 3 && y == 2){
		ans_a ++;
	}else if(x == 3 && y == 4){
		ans_a ++;
	}else if(x == 4 && y == 1){
		ans_a ++;
	}else if(x == 4 && y == 0){
		ans_a ++;
	}
}

int main(){
	cin >> n >> a >> b;
	for(int i=0;i<a;i++){
		cin >> na[i];
	}
	for(int i=0;i<b;i++){
		cin >> nb[i];
	}
	for(int i=0;i<n;i++){
		bisai(na[i%a], nb[i%b]);
	}
	cout << ans_a << " " << n - pin - ans_a;
	return 0;
}

*/
