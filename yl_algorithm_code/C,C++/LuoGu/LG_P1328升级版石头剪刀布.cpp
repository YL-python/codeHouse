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




























