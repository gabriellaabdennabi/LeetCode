class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        
        maxSum = float('-inf')
        for i in range(0,len(nums)):
            if nums[i] < nums[i] + nums[i-1] and i != 0:
                nums[i] = nums[i] + nums[i-1]
                
            maxSum = max(maxSum,nums[i])
            
        return maxSum 
                
                
                
            
        
        
        
        