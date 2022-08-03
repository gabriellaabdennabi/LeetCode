class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        '''
        abcabcbb
        |
           |
        output = 3 
        
        set = (a,b,c)
        check to see if character not in set:
        update the longest substring  
        
        '''
        
        '''
        
        
         abcabcbb
         |
         |
          keep track of string with a set 
        if not in map incremenet right 
        update longestSubstring
        else: 
        incremenet left pointer 
         
         map = {c,a,b}
         longestSubString = 3
            
        
        
        '''
        
        left = 0 
        right = 0 
        track = set()
        longestSubString = 0
        
        while right < len(s):
            if s[right] not in track:
                track.add(s[right])
                longestSubString = max(longestSubString,(right - left) + 1)
                right += 1
                
            else:
                track.remove(s[left])
                left += 1
                
        return longestSubString
                
                
                
            
                
            
        