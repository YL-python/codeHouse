#include <iostream>
#include <cstdio>
#include <algorithm>
#include <cmath>
#include <cstring>
#define init long long
using namespace std;
init n,m;
struct node {
	init l,r,data;
	init lt;
} tree[1000010];
init arr[1000010];
void build(init l,init r,init index,init arr[]) {
	tree[index].lt=0;
	tree[index].l=l;
	tree[index].r=r;
	if(l==r) {
		tree[index].data=arr[l];
		return ;
	}
	init mid=(l+r)/2;
	build(l,mid,index*2,arr);
	build(mid+1,r,index*2+1,arr);
	tree[index].data=tree[index*2].data+tree[index*2+1].data;
	return ;
}
void push_down(init index) {
	if(tree[index].lt!=0) {
		tree[index*2].lt+=tree[index].lt;
		tree[index*2+1].lt+=tree[index].lt;
		init mid=(tree[index].l+tree[index].r)/2;
		tree[index*2].data+=tree[index].lt*(mid-tree[index*2].l+1);
		tree[index*2+1].data+=tree[index].lt*(tree[index*2+1].r-mid);
		tree[index].lt=0;
	}
	return ;
}
void up_data(init index,init l,init r,init k) {
	if(tree[index].r<=r && tree[index].l>=l) {
		tree[index].data+=k*(tree[index].r-tree[index].l+1);
		tree[index].lt+=k;
		return ;
	}
	push_down(index);
	if(tree[index*2].r>=l)
		up_data(index*2,l,r,k);
	if(tree[index*2+1].l<=r)
		up_data(index*2+1,l,r,k);
	tree[index].data=tree[index*2].data+tree[index*2+1].data;
	return ;
}
init search(init index,init l,init r) {
	if(tree[index].l>=l && tree[index].r<=r)
		return tree[index].data;
	push_down(index);
	init num=0;
	if(tree[index*2].r>=l)
		num+=search(index*2,l,r);
	if(tree[index*2+1].l<=r)
		num+=search(index*2+1,l,r);
	return num;
}

int fun(init x) {
	int end = x%10;
	init y = x/10;
	int temp;
	while(y) {
		temp = y%10;
		if(end < temp) {
			return 0;
		}
		y/=10;
	}
	return 1;
}
int main() {
	cin>>n;
	init temp;
	for(init i=1; i<=n; i++) {
		cin >> temp;
		arr[i] = fun(temp);
	}
	build(1,n,1,arr);
	cin >> m;
	for(init i=1; i<=m; i++) {
		init a,b;
		cin>>a>>b;
		printf("%lld\n",search(1,a,b));
	}
}
