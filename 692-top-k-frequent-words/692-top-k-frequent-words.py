class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        
        frequency = {}
        output = []
        
        for word in words:
            if word not in frequency:
                frequency[word] = 1 
                
            else:
                frequency[word] += 1
                
        #sort by key due to lexcographical ordering
        sortedFrequency  = sorted(frequency.items(), key = lambda x : (-x[1], x[0]))
        
       
        
        for i in range(k):
            output.append(sortedFrequency[i][0])
        
        
        
                
        return output 
        