class Solution:
    def countSubstrings(self, s: str) -> int:
          
        
        def countPalindrome(s,lo,hi):
                ans = 0 
                while(lo>=0 and hi < len(s)):
                    if s[lo] == s[hi]:
                        lo -=1 
                        hi += 1 

                        ans +=1 
                    else:
                        break 

                return ans 
                
        count = 0 
        for i in range(len(s)):
            
            count += countPalindrome(s,i,i)
            
            count += countPalindrome(s,i,i+1)
            
        return count
        