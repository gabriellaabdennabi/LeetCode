class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        '''
        nums = [1,2,3]
        Output: [[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]
        
        [], [1],[2],[3],[1,2],[3],[1,3],[2,3],[1,2,3]
        
        
       
        
        '''
        
        
        output = []
        
        subset = []
        
        def dfs(i):
            if i>=len(nums):
                output.append(subset.copy())
                return
            
            subset.append(nums[i])
            dfs(i+1)
            
            
            subset.pop()
            dfs(i+1)
            
        dfs(0)
            
        return output 
        
        
        
        