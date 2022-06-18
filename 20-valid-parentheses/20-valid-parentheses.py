class Solution:
    def isValid(self, s: str) -> bool:
        
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