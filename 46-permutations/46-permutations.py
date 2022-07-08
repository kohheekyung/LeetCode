class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        #return map(list ,itertools.permutations(nums))
        '''
        dfs로 풀기
        '''
        def dfs(elements):
            
            if len(elements) == 0:
                result.append(prev_elements[:])
                
            for element in elements:
                next_elements = elements[:]
                next_elements.remove(element)
            
                prev_elements.append(element)
                dfs(next_elements)
                prev_elements.pop()
        
        result = []
        prev_elements =[]
        
        dfs(nums)
        
        return result
        

            