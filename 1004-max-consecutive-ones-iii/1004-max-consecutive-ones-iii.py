class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        
        '''
        [0,0,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,1] k = 3

           s 
                   e 
                count = 3
                maxOnes = 5
                start = 0 
                end = 0 
                
                
                
        sliding window or two pointer 
        
        
        
        
        
        '''
        count = 0 
        maxOnes = 0 
        start = 0 
        
        for end in range(len(nums)): 
            if nums[end] == 0 and count <=k:
                count += 1
            
                
                
            while count > k: 
                if nums[start] == 0:
                    count -= 1 
                start += 1
                    
            maxOnes = max(maxOnes, end - start + 1)
            
                
                    
            
            
            
        return maxOnes
                
        