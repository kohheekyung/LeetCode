class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        
        def dfs(remain, curr_comb, start):
            
            # 더이상 남는게 없으면 result에 추가
            if remain == 0:
                result.append(curr_comb[:])
                return
            # 더해진 값이 target을 초과하면 더이상 dfs 호출 안함
            elif remain < 0:
                return 

            for i in range(start, len(candidates)):              
                curr_candidate = candidates[i]
                curr_comb.append(curr_candidate)
                print(remain - curr_candidate, curr_comb,i, '호출')
                dfs(remain - curr_candidate, curr_comb,i)
                print(remain - curr_candidate, curr_comb,i, '반환')
                curr_comb.pop()
    
        result = []
        
        dfs(target, [], 0)
        
        return result