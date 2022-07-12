class Solution:
    def subsets_heekyung(self, nums: List[int]) -> List[List[int]]:

        def dfs(curr_subset, start):
            '''
            dfs 인자를 index와 현 subsets으로 잡으나 subsets이 줄어드는 방향
            '''    
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

    def subsets(self, nums: List[int]) -> List[List[int]]:
        '''
        dfs 인자를 index와 현 subsets으로 잡으나 subsets이 늘어나는 방향
        '''    
        def dfs(index, path):
            result.append(path)
            
            for i in range(index, len(nums)):
                dfs(i+1, path+[nums[i]]) # 중복하지 않기 때문에 i+1
                
        result = []
        
        dfs(0, [])

        return result


























