class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:

        def dfs(curr_subset, start):
         
            if curr_subset not in result:
                result.append(curr_subset)
                start = 0
            else:
                # 중복 호출 방지
                start +=1
            
                
            for i in range(start, len(curr_subset)):
                curr_num = curr_subset[i]
           
                next_subset = curr_subset[:]
                next_subset.remove(curr_num)
                
                dfs(next_subset, start)
 
        result = []
        
        dfs(nums, 0)

        return result






























