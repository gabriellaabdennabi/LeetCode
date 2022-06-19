class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        '''
        [0,1,2,3,4,2,2,3,3,4]
                 s 
                           e
           if not equal 
           increment start by 1
           arr[start] = arr[end]
           
           increment end by 1 
       
        
        '''
        start = 0 
        end = 1
        counter = 1 
    
     
        while end < len(nums):
            
            if nums[start] != nums[end]:
                start += 1 
                nums[start] = nums[end]
                counter += 1 
            
                
                
            end += 1 
        print(counter)
        print(start+1)
               
        return start + 1
            
        