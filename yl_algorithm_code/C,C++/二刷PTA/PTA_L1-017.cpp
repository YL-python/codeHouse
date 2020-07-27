#include <stdio.h>
#include <string.h>

// 对输出格式有要求的 果断用 C
char s[55];

int main() {
	scanf("%s",s);
	int len = strlen(s);
	float cnt = 0.0,ans=0.0;

	for(int i=0; i<len; i++) {
		if(s[i] == '2') {
			cnt += 1.0;
		}
	}

	if(s[len-1]%2==0) {
		cnt*=2.0;
	}
	if(s[0]=='-') {
		cnt*=1.5;
		ans=cnt/(len-1);
	} else {
		ans=cnt/len;
	}

	printf("%.2f%%",ans*100.0);

	return 0;
}
