class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        
        
        rightMax = arr[-1]
        output = [0 for x in arr]

        for i in range(len(arr)-1,-1,-1):
            output[i] = rightMax
            rightMax = max(rightMax,arr[i])
        output[-1] = -1 
        return output 
        
                
            
        