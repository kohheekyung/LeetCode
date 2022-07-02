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