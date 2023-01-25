class Solution:
    def isPalindrome(self, s: str) -> bool:
        '''
        iterate through and remove punctuation 
        create a string 
        convert to lower case 

        check to see if palindrome spelled the same backwards as forward 
        use two pointers one at the end 
        one at the beginning 
        check to see if equal increment pointer 
        '''
       

        s_list = s.split(" ")
        converted_string = ""
       
        
        for word in s_list:
            for c in word:
                if c.isalpha() or c.isdigit():
                    
                    converted_string += c.lower()
                    
        print(converted_string)
                    
        l = 0 
        r = len(converted_string) - 1
        
        while l <= r:
            
            if converted_string[l] == converted_string[r]:
                l += 1 
                r -= 1 
            else:
                return False 
        return True 
                
                
            
                    
                    

        

        