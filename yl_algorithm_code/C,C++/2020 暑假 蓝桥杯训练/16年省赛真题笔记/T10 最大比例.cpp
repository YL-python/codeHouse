#include <stdio.h>
#include <iostream>
#include <algorithm>
#include <vector>
#include <map>
using namespace std;
typedef long long LL;
int n;
LL data[100];

struct Ratio {
	LL x,y;
	Ratio(LL _x,LL _y):x(_x),y(_y) {
		LL _gcd = gcd(x,y);
		x/=_gcd;
		y/=_gcd;
	}
	LL gcd(LL a,LL b) {
		return b?gcd(b,a%b):a;
	}
};

vector<Ratio> ratio;
map<LL, map<LL,LL> > all_ex;
map<LL, map<LL,LL> > all_log;

void init() {
	for(int i=2; i<1e6; i++) {
		LL cur = (LL) i*i;
		int pow = 2;
		while(cur < 1e12) {
			all_ex[cur][pow] = i;
			all_log[cur][i] = pow;
			pow ++;
			cur*=i;
		}
	}
}

LL extract(LL x,LL pow) {
	if(pow == 1) return x;
	if(x == 1) return 1;
	if(all_ex[x].find(pow) != all_ex[x].end())
		return all_ex[x][pow];
	else
		return -1;
}
LL log(LL base,LL x) {
	if(base == x) return 1;
	if(all_log[x].find(base) != all_log[x].end())
		return all_log[x][base];
	else
		return -1;
}

int main() {
	init();
	scanf("%d",&n);
	for(int i=0; i<n; i++) {
		scanf("%lld",&data[i]);
	}
	sort(data,data+n);
	if(n == 2) {
		Ratio ans = Ratio(data[1],data[0]);
		printf("%lld/%lld",ans.x,ans.y);
		return 0;
	}
	// 求两两比值 用分数形式存储，存到 vector中
	for(int i=0; i<n-1; i++) {
		if(data[i+1] != data[i])
			ratio.push_back(Ratio(data[i+1],data[i]));
	}
	for(int pow=0; pow<41; pow++) {
		Ratio ra0 = ratio[0];
		LL x = ra0.x;
		LL y = ra0.y;
		LL base_x = extract(x,pow);  // x求 pow次方
		LL base_y = extract(y,pow);
		if(base_x == -1 || base_y == -1)continue;
		bool all_match = true;
		for(int i=1; i<ratio.size(); i++) {
			LL xx = ratio[i].x;
			LL yy = ratio[i].y;
			LL log_x = log(base_x,xx);  // x求 pow次方
			LL log_y = log(base_y,yy);
			if(log_x == -1 || log_y == -1 || log_x!=log_y) {
				all_match = false;
				break;
			}
		}
		if(all_match) {
			Ratio ans = Ratio(base_x,base_y);
			printf("%lld/%lld",ans.x,ans.y);
			return 0;
		}
	}
	return 0;
}
