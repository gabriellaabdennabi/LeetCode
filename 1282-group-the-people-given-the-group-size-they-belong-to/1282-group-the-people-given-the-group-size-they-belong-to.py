class Solution:
    def groupThePeople(self, groupSizes: List[int]) -> List[List[int]]:
        
        
        '''
        [3,3,3,3,3,1,3]
           i
        
        bucket each value at index 
        
        {3:[0,1,2],3:[3,4,6]}
        '''
        
        mapping = {}
        output = []
        
        for i in range(len(groupSizes)):
            
            if groupSizes[i] in mapping:
                mapping[groupSizes[i]].append(i)
                
            else:
                mapping[groupSizes[i]] = [i]

                
            if len(mapping[groupSizes[i]]) == groupSizes[i]:
                output.append(mapping[groupSizes[i]])
                mapping[groupSizes[i]] = []
                
                
            
            
        return output
        