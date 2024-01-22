class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)

        if n <=2:
            return max(nums)

        dp = [0] * n 
        for i in range(n):
            # Rob this house and add it to the total from two houses ago,
            # or don't rob this house and take the total from the previous house.
            dp[i]= max(nums[i]+ dp[i-2], dp[i-1])
            
        return dp[-1]   

        
