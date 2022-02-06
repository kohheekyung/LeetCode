class Solution(object):
    
    # time complexity O(N) go entire list
    # space complexity O(1) constant -
    def totalFruit(self, fruits):
        """
        :type fruits: List[int]
        :rtype: int
        """
        start = 0
        end = 0
        max_len = 0
        d = {} # key : fruit_case value : index
        
        while end < len(fruits):
            d[fruits[end]] = end
            if len(d) >= 3:
                # get index which is the most in front of as we want to    get the longest len 
                min_val = min(d.values())
                 # we don't want to store more than 2 types of fruit
                del d[fruits[min_val]]
                start = min_val + 1
            max_len = max(max_len, end-start + 1) 
            end +=1
        return max_len
 
        
        
        


            
            

            
            
        
        
        
        