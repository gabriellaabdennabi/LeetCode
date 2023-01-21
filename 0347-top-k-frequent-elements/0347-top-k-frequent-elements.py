class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        '''
        [1,1,1,2,2,3], k = 2 
        [1,2]
        
        
        [1,2,3]  k = 3 
        [1,2,3]
        
        [1,1,3,2,3,2] k = 2 
        
        [1,3]
        
        [] k = 1
        [1,2] k = 3 what do we return in this case 
        
         
        Engineering method understand the problem 
        Examples 
        Edge Cases 
        Possible solutions 
        Code 
        Test 
        
        
        Clarification:
        K most frequent meaning the top two for example k = 2 
        Will the array always be in order 
        Will there always be k elements or do we need to check 
        If not k frequent just return the output array 
        
        Possible solutions:
        use a heap
        insert into the heap the heap gets sorted which means the most frequent elements will be in the front of the heap 
        counter that keeps track of frequency and check to see if the counter is equal to k 
        Everytime we come across a new element add to the counter 
        if the current item is not new dont add to the counter 
        add to our output when the item is new 
        
        Pseudocode:
        if array is empty return empty array output 
        if k exceeds the size of the array return empty or the output 
        
        
        '''
        
        frequency = Counter(nums)
        
        
        
        
            
        output = heapq.nlargest(k,frequency.keys(),key= frequency.get)
        
        return output 
    
        