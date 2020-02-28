class Solution {
public:
    int lengthOfLIS(vector<int>& nums) {
        if(nums.size() == 0){
            return 0;
        }
        vector<int> dp(nums.size(), 1);
        int lis = dp[0];
        for(int i=1; i< nums.size(); i++){
            for(int j=0; j<i; j++){
                if(nums[i] > nums[j] && dp[i] < dp[j] + 1){
                    dp[i] = dp[j] + 1;
                }
            }
            lis = lis < dp[i] ? dp[i] : lis;
        }
        return lis;
    }
};



/*
����һ��������������飬�ҵ���������������еĳ��ȡ�

ʾ��:

����: [10,9,2,5,3,7,101,18]
���: 4 
����: ���������������?[2,3,7,101]�����ĳ����� 4��



״̬���壺dp[i] ��ʾ��i �����������������
dp[i] ��ֵ�� dp[0] ��dp[i-1] ��ֵ�й� ���ֵ��һ
ֻ�� nums[i] > nums[j] ������� dp[i] �Ż��� dp[j] + 1
 
����һ��ֵ��� dp��������ֵ����
 
*/
