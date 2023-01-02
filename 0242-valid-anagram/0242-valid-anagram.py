class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        dic ={}
        
        if len(s) != len(t):
            return False
        
        for i in range(len(s)):
            if s[i] not in dic:
                dic[s[i]] = 1 
                
            else:
                dic[s[i]] += 1 
                
        for j in range(len(t)):
            if t[j] not in dic:
                return False 
            
            else:
                dic[t[j]] -= 1 
                
        
        for val in dic.values():
            
            if val != 0:
                return False
            
        return True 
            
        