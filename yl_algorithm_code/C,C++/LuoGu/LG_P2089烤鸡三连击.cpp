#include <iostream>
#include <string>

using namespace std;

int a,b,c,d,e,f,g,h,i,j,in,x=0;
int ans[10000][10]; 

int main(){
	
	cin>>in;
	if(in > 30 || in < 10){
		cout << 0;
		return 0;
	}
	for (a=1;a<=3;a++){  
        for (b=1;b<=3;b++){  
            for (c=1;c<=3;c++){  
                for (d=1;d<=3;d++){  
                    for (e=1;e<=3;e++){  
                        for (f=1;f<=3;f++){  
                            for (g=1;g<=3;g++){  
                                for(h=1;h<=3;h++){  
                                    for (i=1;i<=3;i++){  
                                        for (j=1;j<=3;j++){  
                                            if (a+b+c+d+e+f+g+h+i+j==in){
                                            	ans[x][0] = a;
                                            	ans[x][1] = b;
                                            	ans[x][2] = c;
                                            	ans[x][3] = d;
                                            	ans[x][4] = e;
                                            	ans[x][5] = f;
                                            	ans[x][6] = g;
                                            	ans[x][7] = h;
                                            	ans[x][8] = i;
                                            	ans[x][9] = j;
                                                x++;
                                            }
                                        }  
                                    }  
                                }  
                            }  
                        }  
                    }  
                }  
            }  
        }  
    }  
    cout << x << endl;
    for(int i=0;i<x;i++){
    	for(int j= 0;j<10;j++){
    		cout << ans[i][j] << " ";
		}
		cout << endl;
	}
    
	return 0;
}




























