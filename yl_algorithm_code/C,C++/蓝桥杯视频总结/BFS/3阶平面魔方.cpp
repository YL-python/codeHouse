#include <iostream>
#include <string>
#include <map>
#include <queue>

using namespace std;

struct node {
	int a[3][3];
	bool operator < (const node &x) const {
		for(int i=0; i<3; i++) {
			for(int j=0; j<3; j++) {
				if(a[i][j] < x.a[i][j]) {
					return 1;
				}
			}
		}
		return 0;
	}
	bool operator == (const node &x) const {
		for(int i=0; i<3; i++) {
			for(int j=0; j<3; j++) {
				if(a[i][j] != x.a[i][j]){
					return 0;
				}
			}
		}
		return 1;
	}
	void print(){
		for(int i=0; i<3; i++) {
			for(int j=0; j<3; j++) {
				cout << a[i][j] << " ";
			}
			cout << endl;
		}
	}
	int tonum(){
		int res = 0;
		for(int i=0; i<3; i++) {
			for(int j=0; j<3; j++) {
				res = res*10 + a[i][j];
			}
		}
		return res;
	}
} init;

node rotate(node a,int s,int d){
	node res = a;
	if(d == -1){ // ÓÒÒÆ 
		int temp = res.a[s][2];
		res.a[s][2] = res.a[s][1]; 
		res.a[s][1] = res.a[s][0]; 
		res.a[s][0] = temp; 
	}else if(d == 1){ // ×óÒÆ 
		int temp = res.a[s][0];
		res.a[s][0] = res.a[s][1]; 
		res.a[s][1] = res.a[s][2]; 
		res.a[s][2] = temp; 
	}else if(d == -2){  // ÉÏÒÆ 
		int temp = res.a[0][s];
		res.a[0][s] = res.a[1][s]; 
		res.a[1][s] = res.a[2][s]; 
		res.a[2][s] = temp; 
	} else if(d == 2){  // ÏÂÒÆ 
		int temp = res.a[2][s];
		res.a[2][s] = res.a[1][s]; 
		res.a[1][s] = res.a[0][s]; 
		res.a[0][s] = temp; 
	}
	return res;
}

int bfs(node st){
	queue<node> q;
	map<int, int> d;
	q.push(st);
	d[st.tonum()] = 0;
	while(!q.empty()){
		node x = q.front();
		q.pop();
		int tt = x.tonum();
		if(x == init){
			return d[x.tonum()];
		}
		node temp;
		for(int i=0;i<3;i++){
			temp = rotate(x,i,-1);
			if(!d.count(temp.tonum())){
				d[temp.tonum()] = d[tt] + 1;
				q.push(temp);
			}
			temp = rotate(x, i, 1);
			if(!d.count(temp.tonum())){
				d[temp.tonum()] = d[tt] + 1;
				q.push(temp);
			}
		}
		for(int i=0;i<3;i++){
			temp = rotate(x,i,-2);
			if(!d.count(temp.tonum())){
				d[temp.tonum()] = d[tt] + 1;
				q.push(temp);
			}
			temp = rotate(x, i, 2);
			if(!d.count(temp.tonum())){
				d[temp.tonum()] = d[tt] + 1;
				q.push(temp);
			}
		}
	}
	return -1;
}

int main() {
	// ³õÊ¼»¯ 
	for(int i=0; i<3; i++) {
		for(int j=0; j<3; j++) {
			init.a[i][j] = i*3 + j + 1;
		}
	}
	node t;
	for(int i=0;i<3;i++){
		int n;
		cin >> n;
		t.a[i][2] = n %10;
		n/=10;
		t.a[i][1] = n %10;
		n/=10;
		t.a[i][0] = n;
	}
	int ans = bfs(t);
	cout << ans << endl;
	return 0;
}
/*
412
756
389

2
*/



























