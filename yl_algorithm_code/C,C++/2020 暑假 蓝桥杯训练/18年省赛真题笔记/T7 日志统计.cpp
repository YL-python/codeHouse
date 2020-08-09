#include <iostream>
#include <vector>
#include <set>
#include <map>
#include <algorithm>
using namespace std;

struct R {
	int ts,id;
};

bool cmp (R r1,R r2) {
	return r1.ts < r2.ts;
}
int N,D,K;

int main() {
	cin >> N >> D >> K;
	vector<R> records(N);
	map<int, int> cnt;  // 记录 id和他出现的次数
	for(int i=0; i<N; i++) {
		cin >> records[i].ts >> records[i].id;
	}
	sort(records.begin(), records.end(), cmp);// 按照时间 对结构体自定义排序
	int j=0;  // 尺取法 探测指针
	set<int > ans; // 记录结果，自动去重和排序
	for(int i=0; i<N; i++) {  // i 是尺取法的起点
		while( j < N && records[j].ts - records[i].ts < D) {
			cnt[records[j].id] ++ ;  // 加加
			if(cnt[records[j].id] >= K) {
				ans.insert(records[j].id);
			}
			j++;
		}
		cnt[records[j].id] -- ;  // 减去多加的
	}
	for(set<int>::iterator i=ans.begin(); i!=ans.end(); i++) {
		cout << *i << endl;
	}
	return 0;
}

















