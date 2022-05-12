class Solution:
    def longestPalindrome(self, s: str) -> str:
        
        def expand(l, r):
            
            # 투 포인트 인덱스의 범위내에서 PALINDROME인지 확인
            while l >= 0 and r < len(s) and s[l] == s[r]:
                l -= 1
                r += 1
        
            # while 문이 끝나면 l는 올바른 인덱스-1, R 올바른 인덱스+1인채로 저장됨  
            return s[l+1:r]

        # 문자 길이가 1개거나 문자 전체가 PALINDROME일때 
        if len(s) < 2 or s == s[::-1]:
            return s
        
        
        result = ''
        for i in range(len(s)-1):
            # PALINDROME 문자길이가 짝수일 경우 (i+1), 홀수일 경우(i+2) 확인 
            result = max(result, expand(i, i+1),  expand(i, i+2), key=len)
        return result
    
        