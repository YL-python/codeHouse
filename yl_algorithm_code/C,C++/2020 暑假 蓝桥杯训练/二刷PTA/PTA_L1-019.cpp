#include <iostream>
using namespace std;

int main() {
	int aj,bj,n,ahan,ahua,bhan,bhua;
	cin >> aj >> bj;
	cin >> n;
	int ahe=0,bhe=0;
	for(int i=0;i<n;i++){
		cin >> ahan >> ahua >> bhan >> bhua;
		if(ahua == bhua){
			continue;
		}
		int temp = ahan+bhan;
		ahua == temp ? ahe++ : 1;
		bhua == temp ? bhe++ : 1;
		
		if(ahe > aj){
			cout << "A" << endl << bhe;
			break;
		}
		if(bhe > bj){
			cout << "B" << endl << ahe;
			break;
		}
	}
	return 0;
}
