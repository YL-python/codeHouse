#include<iostream>
using namespace std;

int main(){
	int A,B,n;
	int Asay[105],Bsay[105],Ashow[105],Bshow[105];	
	cin >> A >> B >> n;
	for(int i=0;i<n;i++){
		cin >> Asay[i] >> Ashow[i] >> Bsay[i] >> Bshow[i];
	}
	int countA = A, countB = B;
	for(int i=0;i<n;i++){
		int sum = Asay[i] + Bsay[i];
		if(sum == Ashow[i] && sum != Bshow[i]){
			A--;
		}
		if(sum == Bshow[i] && sum != Ashow[i]){
			B--;
		}
		if(A<0){
			cout << "A" << endl << countB-B;
			break;
		}
		if(B<0){
			cout << "B" << endl << countA-A;
			break;
		}
	}
	return 0;
}
