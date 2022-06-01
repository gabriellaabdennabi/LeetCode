class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        '''
        [1,2,3,4,5] target = 11 
         s
                 e
         start = 0
         currSum = 15
         lenOfMinSub = 0 
         
        
        '''
        
        start = 0
        lenOfMinSub = float('inf') 
        currSum = 0 
        
        for end in range(len(nums)):
            currSum += nums[end]
            
            while currSum >= target:
                lenOfMinSub = min(lenOfMinSub,end - start + 1)
                currSum -= nums[start]
                start += 1 
                
                
        return lenOfMinSub if lenOfMinSub != float('inf') else 0
                
        
        
                
                
            
            
                
            
        