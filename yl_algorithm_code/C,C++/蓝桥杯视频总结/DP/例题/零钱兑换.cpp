class Solution {
public:
    int coinChange(vector<int>& coins, int amount) {
        vector<int> dp;
        for(int i=0;i<=amount;i++){
            dp.push_back(-1);
        }
        dp[0] = 0;
        for(int i=1;i<=amount;i++){
            for(int j=0;j<coins.size();j++){
                if(i-coins[j] >=0 && dp[i-coins[j]] != -1){
                    if(dp[i] == -1 || dp[i] > dp[i-coins[j]] + 1){
                        dp[i] = dp[i-coins[j]] + 1;
                    }
                }
            }
        }
        return dp[amount];
    }
};
/*
������ͬ����Ӳ�� coins ��һ���ܽ�� amount����дһ��������������Դճ��ܽ����������ٵ�Ӳ�Ҹ��������û���κ�һ��Ӳ�����������ܽ�����?-1��

ʾ�� 1:

����: coins = [1, 2, 5], amount = 11
���: 3 
����: 11 = 5 + 5 + 1

1��2��5
dp[11] = min(dp[11 - 1], dp[11 - 2], dp[11 - 5]) + 1 

*/ 
