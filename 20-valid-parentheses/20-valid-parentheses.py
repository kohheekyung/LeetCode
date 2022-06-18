class Solution:
    def isValid(self, s: str) -> bool:
        '''
        Time O(n) 50 ms
        Memory O(n) 13.9 MB
        pop과 push(append)는 O(1)시간이 든다
        '''
        stack = []
        
        characters_set = { ')' : '(',
                            '}' : '{',
                          ']' : '['
                         } 
        
        for characters in s:
            
            # (, {, [ 는 스택에 넣고
            if characters not in characters_set:
                stack.append(characters)
            # ), }, ] 일 경우는 는 스택에서 pop()한 (, {, [ 중의 값과 set의 value 값과 비교
            else:
                if not stack or stack.pop() != characters_set[characters]:
                    return False
                
        return len(stack) == 0