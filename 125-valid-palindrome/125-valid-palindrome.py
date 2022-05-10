
class Solution:
    
    def isPalindrome(self, s: str) -> bool:
        import re    
        # lower all strings
        s = s.lower()
        
        # filter unecessary char
        #[] :[]안에 들어있는 캐릭터 자체를 나타내며
        # ^ : 맨 앞에 사용될 경우에만 해당 문자 패턴이 아닌 것과 매칭 ex) [^a-d] : a 그리고 b 그리고 c 그리고 d 가 아닌 문자열
        # - : 해당 문자 사이 범위에 속하는 문자 중 하나 ex) [a-d] : a 또는 b 또는 c 또는 d
        s = re.sub('[^a-z0-9]', '', s)
        return s == s[::-1]