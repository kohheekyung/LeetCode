class Solution:    
    def letterCombinations_recursive(self, digits: str) -> List[str]:
        '''
        DFS으로 가능한 경우 모두 조합하는 형태로 탐색
        Time O(4^n * N) : 문제에서 4는 digits의 최대길이 69 ms
        Spcae O(n) : digits의 길이에 따라 14 MB
        '''
        def dfs(index, path=""):
            '''
            index : 현재 확인 중인 문자
            path : 현재까지 모은 문자 조합
            '''
            # 전달된 문자열의 길이와 digits의 길이가 같다며 결과에 담아주고 백트래킹
            if len(path) == len(digits):
                result.append(path)
                return # 백트래킹
            
            # digits의 문자 요소를 순서대로 loop돌며
            for i in range(index, len(digits)):
                # 문제조합에 추가
                for j in letters[digits[i]]:
                    # i+1을 통해 문자조합이 중복이 없도록함
                    # path+j를 통해 조합된 문자열이 전달됨
                    dfs(i+1, path+j) 
        # 예외처리
        if not digits :
            return []
        result =[]
        letters = { '2':'abc', '3':'def', '4':'ghi', '5':'jkl', '6':'mno', '7':'pqrs', '8':'tuv', '9':'wxyz'}
        
        dfs(0, "")
        
        return result
    
    def letterCombinations(self, digits: str) -> List[str]:
        '''
        stack을 이용해 iterative하게 풀기
        '''
        
        # 예외처리
        if not digits:
            return []
    
        num2letters = { '2':'abc', '3':'def', '4':'ghi', '5':'jkl', '6':'mno', '7':'pqrs',
                       '8':'tuv', '9':'wxyz'}
        
        stack = [] # 스택에는 현문자 조합을 저장. ""에서 시작
        result = [] # 문자 조합의 리스트 반환
 
        stack.append("")
    
        while len(stack) > 0:
            curr_chars = stack.pop()
        
            # 전달된 문자열의 길이와 digits의 길이가 같다면 결과에 담아주기
            if len(curr_chars) == len(digits):
                result.append(curr_chars)
            else:
                # 전달된 문자열의 길이가 남은 숫자열 시작 인덱스
                i = len(curr_chars)
                # 숫자열에 속한 문자열 파악
                letters = num2letters[digits[i]]
                for letter in letters:
                    stack.append(curr_chars+letter)
                    
        return result  
