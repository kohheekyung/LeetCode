class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:

                                                                                                                                                                               #중복 호출
#         dfs([1,2,3]) dfs([2,3])  dfs([3]) dfs([])  dfs([2,3]) dfs([2])  dfs([1,2,3]) dfs([1,3]) dfs([3]) dfs([])  dfs([1,3])    dfs([1])  dfs([])  dfs([1,2,3])    dfs([1,2]) dfs([2])   dfs([])
#     i           0       0           0                    1          0       1              0        0        0          1          0                      2            0           0    
# curr_n         1        2           3                    3       2          2             1        3                    3          1                      3            1           2
# curr_s      1,2,3       2,3         3                   2,3     2           1,2,3       1,3        3                  1,3          1                     1,2,3        1,2          2
# next_s       2,3        3           []                  2       []           1,3          3       []                  1           []                      1,2          2           []
#         dfs([2]) dfs([])
#            0        0
#           1
#             2
#             []
                                                                                                                                                        
# result [[1,2,3],[2,3],[3],[],[2],[1,3],[1],[1,2]]

#         def dfs(curr_subset):
 
            
#             if curr_subset not in result:
#                 result.append(curr_subset)
                
#             for i in range(0, len(curr_subset)):
#                 curr_num = curr_subset[i]
#                 # print(curr_num)
#                 # print(curr_subset)
#                 next_subset = curr_subset[:]
#                 next_subset.remove(curr_num)
                
#                 dfs(next_subset)
#                 #curr_subset.pop()
                
            
        
#         result = []
        
#         dfs(nums)
        
#         return result


        def dfs(curr_subset, start):
 
            
            if curr_subset not in result:
                result.append(curr_subset)
                start = 0
            else:
                start +=1
            
                
            for i in range(start, len(curr_subset)):
                curr_num = curr_subset[i]
                # print(curr_num)
                # print(curr_subset)
                next_subset = curr_subset[:]
                next_subset.remove(curr_num)
                
                dfs(next_subset, start)
                #curr_subset.pop()
                
            
        
        result = []
        
        dfs(nums, 0)
        
        
        
        return result






























