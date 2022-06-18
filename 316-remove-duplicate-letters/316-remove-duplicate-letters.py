class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        '''
        Time O(n) 46 ms
        Space O(1)13.8 MB
        '''
        # 카운터를 통해 문자별 갯수 파악한다
        # 0 보다 큰 문자는 뒤에 더 붙일 문자가 있다
        counter = collections.Counter(s)
        
        # 처리된 문자여부를 파아하기 위해 사용
        seen = set()
        stack = []
        
        for letter in s:
            # 문자 개수 하나 줄이기
            counter[letter] -= 1
            
            # 이미 스택에 문자가 있다면 패스
            if letter in seen:
                continue
            
            # 0 보다 큰 문자는 뒤에 더 붙일 문자가 있다
            # 현 문자가 스택의 마지막 값보다 앞에 있어야 하고 스택의 마지막 값이 1개 이상이면
            while stack and letter < stack[-1] and counter[stack[-1]] > 0:
                # 스택의 마지막 값 제거
                seen.remove(stack.pop())
            stack.append(letter)
            seen.add(letter)
        
        return ''.join(stack)