class Solution {
public:
    int rob(vector<int>& nums) {
        if(nums.size() == 0){
            return 0;
        }
        if(nums.size() == 1){
            return nums[0];
        }else if(nums.size() == 2){
            return std::max(nums[0],nums[1]);
        }else{
            std::vector<int> dp(nums.size(), 0);
            dp[0] = nums[0];
            dp[1] = max(nums[0],nums[1]);
            for(int i=2;i<nums.size();i++){
            	
                dp[i] = std::max(dp[i-2]+nums[i],dp[i-1]);
            }
            return dp[nums.size() - 1];
        }
    }
};
/*
����һ��רҵ��С͵���ƻ�͵���ؽֵķ��ݡ�ÿ�䷿�ڶ�����һ�����ֽ�Ӱ����͵�Ե�Ψһ��Լ���ؾ������ڵķ���װ���໥��ͨ�ķ���ϵͳ������������ڵķ�����ͬһ���ϱ�С͵���룬ϵͳ���Զ�������

����һ������ÿ�����ݴ�Ž��ķǸ��������飬�������ڲ���������װ�õ�����£��ܹ�͵�Ե�����߽�

����: [1,2,3,1]
���: 4
����: ͵�� 1 �ŷ��� (��� = 1) ��Ȼ��͵�� 3 �ŷ��� (��� = 3)��
͵�Ե�����߽�� = 1 + 3 = 4 ��

dp ���� dp[i] = max(dp[i-2]+nums[i], dp[i-1])
*/
