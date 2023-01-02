class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        
        '''
        [1,2,3,1] -> 1 
        
        dic = {}
        
        
        '''
        dic = {}
        
        for i in range(len(nums)):
            current_count = dic.get(nums[i],0) + 1
            if current_count == 2:
                return True
            else:
                dic[nums[i]] = current_count
                
        return False