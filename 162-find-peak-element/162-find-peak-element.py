class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        
        '''
        [1,2,3,1]
         
        peak element is greater than its neighbors 
        binary search problem 
        
        
        '''
        if len(nums) == 1:
            return 0 
        
        for i in range(len(nums)-1):
            if i == 0 and nums[i] > nums[i+1]:
                return i
            
            elif nums[i] > nums[i-1] and nums[i] > nums[i+1]:
                return i
            
            
        return len(nums) -1 
        