class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        
      
        start = 0 
        end = len(nums) - 1
        output = [0] * len(nums)
        
        for i in range(len(output)-1,-1,-1):
            if abs(nums[start]) >= abs(nums[end]):
                output[i] = nums[start] * nums[start]
                start += 1
            else:
                output[i] = nums[end] * nums[end]
                end -= 1 
            
                
        return output
        
        