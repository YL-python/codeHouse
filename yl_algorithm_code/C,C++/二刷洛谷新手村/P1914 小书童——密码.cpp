#include <cstdio>

int n;
char s[55];

int main() {

	scanf("%d%s",&n,s);

	for(int i=0; s[i]!='\0'; i++) {
		printf("%c",(((s[i] - 'a' + n) % 26) + 'a'));
	}
	return 0;
}
