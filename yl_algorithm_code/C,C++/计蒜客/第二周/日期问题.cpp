#include <iostream>
using namespace std;

int r(int x){
	if(x % 400 == 0 || (x%4==0 && x%100!=0)){
		return 1;
	}else{
		return 0;
	}
}

int main(){
	int yyyy1,yyyy2,mm1,mm2,dd1,dd2;
	int m[13] = {0,31,28,31,30,31,30,31,31,30,31,30,31};
	int day1=0,day2=0;

	cin >> yyyy1 >> mm1 >> dd1;
	cin >> yyyy2 >> mm2 >> dd2;
	
	for(int i=1;i<mm1;i++){
		day1+=m[i];
	}
	if(mm1 > 2 && r(yyyy1)){
		day1++;
	}
	day1+=dd1;
	
	for(int i=yyyy1;i<yyyy2;i++){
		day2+=365;
		day2 = day2+r(i);
	}
	
	for(int i=1;i<mm2;i++){
		day2+=m[i];
	}
	if(mm2 > 2 && r(yyyy2)){
		day2++;
	}
	day2+=dd2;
	
	cout << day2-day1;
	return 0;
}
