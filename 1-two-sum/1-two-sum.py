class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        '''
        1. Happy case examples
        2. possible edge cases
        3. solution suggest
        4. time complexity
        5. code 
        6. test 
        
        [9,10,11,2] target = 12 return [1,3]
        [1,2,3,4,5] target = 5 return [1,2]
        [1,4,2,3] target = 5 return [1,4]
        [1,2,3,4] target = 0 return []
        [1] target = 1 return []
        
    
        '''
        
        dic = {} 
        
        for i in range(len(nums)):
            if (target - nums[i]) in dic:
                return [i,dic[target - nums[i]]]
            
            else:
                dic[nums[i]] = i 
                
        return [-1,-1]
        
        
        
      
        