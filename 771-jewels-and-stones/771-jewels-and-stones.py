class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        '''
        jewels: 보석인 돌의 종류들
        stones 내가 가지고 있는 돌들
        
        내가 가지고 있는 돌들 중 몇개가 보석인지 알고싶다요.
        '''
        result = 0

        jewels_dict = collections.defaultdict(int)
        
        for stone in stones:    
            jewels_dict[stone] += 1
            
        for jewel in jewels:
            result += jewels_dict[jewel]
        
        return result