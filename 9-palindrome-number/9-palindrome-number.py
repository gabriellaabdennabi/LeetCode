class Solution:
    def isPalindrome(self, x: int) -> bool:
        
        '''
        121
        reverse the number 
        and compare agains the original 
        
        '''
        
        rev = 0
        copyOfX = x 
        
        if x < 0:
            return False
        
        while x > 0:
            rev = rev * 10 + (x % 10)
            x //= 10 
            
        if rev == copyOfX:
            return True 
        
        else:
            return False 
            
        
        
        