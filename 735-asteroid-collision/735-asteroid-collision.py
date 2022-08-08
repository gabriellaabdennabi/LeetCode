class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        '''
        [-1,3,2,-3]
          i 
        i = -3
        stack = [-1,3,2]
        
        if abs(i) > stack[-1]:
            pop from stack 
            
        elif abs(i) < stack[-1]:
            break 
        elif abs(i) == stack[-1]:
        pop from stack and break 
        
        
        
        
        
        
        '''
        stack = []

        for i in asteroids: 
             
            while stack and i < 0 and stack[-1] > 0:
                
                diff = i + stack[-1]

                if diff < 0: 
                    stack.pop()
                    
                elif diff > 0:
                    i = 0 
                        
                        
                elif diff == 0:
                    stack.pop()
                    i = 0 
            if i:
                stack.append(i)
                
                        
            
                    
        return stack 
                    