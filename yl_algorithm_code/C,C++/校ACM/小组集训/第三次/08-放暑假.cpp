#include <iostream>
#include <stack>
using namespace std;

stack<long long> s;
long long n;
long long ans=-1,a[100005];

// นýมห9ื้ ing 
int main() {
	cin >> n;
	for(int i=0;i<n;i++){
		cin >> a[i];
	}
	for(int i=0;i<n;i++){
		long long cnt=a[i];
		s.push(a[i]);
		int left=i-1,right=i+1;
		while(left>=0 && a[left]>a[i]){
			s.push(a[left]);
			left--;
		}
		while(right<n && a[right]>a[i]){
			s.push(a[right]);
			right++;
		}
		long long sum=0;
		while(!s.empty()){
			sum += s.top();
			s.pop();
		}
		cnt *=sum;
		if(cnt>ans){
			ans = cnt;
		}
	}
	cout << ans;
	return 0;
}
