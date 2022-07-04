class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        '''
        DFS으로 가능한 경우 모두 조합하는 형태로 탐색
        Time O(4^n * N) : 문제에서 4는 digits의 최대길이
        Spcae O(n) : digits의 길이에 따라
        '''
        def dfs(index, path=""):
            '''
            index : 현재 확인 중인 문자
            path : 현재까지 모은 문자 조합
            '''
            
            # 끝까지 탐색했다면 백트래킹
            if len(path) == len(digits):
                result.append(path)
                return # 백트래킹
            
            # digits의 문자 요소를 순서대로 loop돌며
            for i in range(index, len(digits)):
                # 문제조합에 추가
                for j in letters[digits[i]]:
                    dfs(i+1, path+j)
        
        
        # 예외처리
        if not digits :
            return []
        result =[]
        letters = {
            '2':'abc',
            '3':'def',
            '4':'ghi',
            '5':'jkl',
            '6':'mno', 
            '7':'pqrs',
            '8':'tuv',
            '9':'wxyz'
        }
        
        dfs(0, "")
        
        return result