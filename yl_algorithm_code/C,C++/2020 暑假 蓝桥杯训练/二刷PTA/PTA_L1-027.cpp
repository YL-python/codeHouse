#include<iostream>
#include<string>
using namespace std;

string tel;
int arr[10], index[11];

/* 变量解释
arr 数组： 下标是 表示0-9数字，值是这个数字有没有在电话号码里面出现
index 数组： 下标是0-9，值是 这个数字在 arr数组的下标
*/

int main() {
	cin >> tel;
	for(int i=0; i<tel.length(); i++) {
		arr[tel[i] - '0'] = 1;  // 当前电话号码出现了标 1
	}

	int cnt = 0;
	for(int i=tel.length()-1; i>=0; i--) {  // 逆序
		if(arr[i]) {
			index[i] = cnt++;  // i这个数字在arr中排第 cnt 位
		}
	}

	cout << "int[] arr = new int[]{";
	int temp = 1;  // temp标记是否要输出 , 逗号
	for(int i=tel.length()-1; i>=0; i--) {
		if(arr[i]) {
			if(temp) {
				temp = 0;
			} else {
				cout<< ',';
			}
			cout << i;
		}
	}
	cout << "};" << endl;

	cout << "int[] index = new int[]{";
	temp = 1;
	for(int i=0; i<tel.length(); i++) {
		if(temp) {
			temp = 0;
		} else {
			cout<<',';
		}
		cout << index[tel[i] - '0'];
	}
	cout << "};" << endl;
	return 0;
}
