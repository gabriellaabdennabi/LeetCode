class Solution {
    public int longestOnes(int[] nums, int k) {
        
        /*
        nums = [1,1,1,0,0,0,1,1,1,1,0], k = 2
                s 
                  i 
                start = 0 
                maxOnes = 2
                count = 0 
        
        */
        
        int start = 0;
        int maxOnes = 0;
        int count = 0; 
        
        for(int i = 0; i< nums.length; i++) {
            
            if (nums[i] == 0 && count <= k){
                count += 1;
                
            
            }
            
            while(count > k){
                if(nums[start] == 0){
                    count -=1;
                }
                start += 1;
            }
            
            
            
            
            maxOnes = Math.max(maxOnes, (i - start) + 1);
            
            
        }
        
        
        return maxOnes;
        
    }
}