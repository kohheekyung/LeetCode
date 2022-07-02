class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        '''
        슬라이딩 윈도우 기번 사용하여
        좌측 포인터 start
        우측 포인터 idx
        중복되는 문자가 있을시 start를 갱신하거나
        중복되는 문자가 없을시 substring의 길이를 갱신해가는문제
        Time O(n) 71 ms
        Space O(n) 	14.2 MB
        '''
        chars_used = {} # 등장한 단어들
        max_length = 0 # substring의 최대길이 저장 
        start = 0 # substring의 시작위치
        
        for idx, char in enumerate(s) :
            
            #만약 중복되면
            if char in chars_used and start <= chars_used[char]: 
                # substring의 시작 위치를 한칸 앞으로 이동
                start = chars_used[char]+1
            else:
                # 최대길이 갱신
                max_length = max(max_length, idx - start + 1)
            
            #현위치 저장
            chars_used[char] = idx
            
        return max_length
            
                
            