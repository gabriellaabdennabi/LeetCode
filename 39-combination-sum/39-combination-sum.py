class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        output = []
        
        
        def dfs(i,cur,total):
            if total == target:
                output.append(cur.copy())
                return
            
            if i >= len(candidates) or total > target:
                return 
            cur.append(candidates[i])
            dfs(i,cur,total + candidates[i])
            
            cur.pop()
            dfs(i+1,cur,total)
            
        
        dfs(0,[],0)
        return output 
      
            
            
            
            
    