class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        '''
        jewels: 보석인 돌의 종류들
        stones 내가 가지고 있는 돌들
        
        내가 가지고 있는 돌들 중 몇개가 보석인지 알고싶다.
        Time O(n) : 39 ms
        Space O(n) : 13.8 MB  보석 길이 만큼
        '''
        result = 0

        jewels_dict = collections.defaultdict(int)
        
        # 돌들 중 보석이면 딕셔너리에 개수추가 
        for stone in stones:    
            jewels_dict[stone] += 1
        # 보석 개수 합
        for jewel in jewels:
            result += jewels_dict[jewel]
        
        return result
    
    def numJewelsInStones_counter(self, jewels: str, stones: str) -> int:
        '''
        Counter 사용해서 간단하게 풀기
        '''
        freqs = collections.Counter(stones) # 돌의 빈도수 구하기 
        count = 0
        
        for jewel in jewels:
            count += freqs[jewel]
            
        return Counter
        
    def numJewelsInStones_python(self, jewels: str, stones: str) -> int:
        '''
        Python 한줄로 풀기
        '''
        return sum(stone in jewels for stone in stones)