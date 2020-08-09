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
	map<int, int> cnt;  // ��¼ id�������ֵĴ���
	for(int i=0; i<N; i++) {
		cin >> records[i].ts >> records[i].id;
	}
	sort(records.begin(), records.end(), cmp);// ����ʱ�� �Խṹ���Զ�������
	int j=0;  // ��ȡ�� ̽��ָ��
	set<int > ans; // ��¼������Զ�ȥ�غ�����
	for(int i=0; i<N; i++) {  // i �ǳ�ȡ�������
		while( j < N && records[j].ts - records[i].ts < D) {
			cnt[records[j].id] ++ ;  // �Ӽ�
			if(cnt[records[j].id] >= K) {
				ans.insert(records[j].id);
			}
			j++;
		}
		cnt[records[j].id] -- ;  // ��ȥ��ӵ�
	}
	for(set<int>::iterator i=ans.begin(); i!=ans.end(); i++) {
		cout << *i << endl;
	}
	return 0;
}

















