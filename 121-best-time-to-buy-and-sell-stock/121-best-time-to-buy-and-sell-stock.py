class Solution:
    def maxProfit_bruteforce(self, prices: List[int]) -> int:
        '''
        Time limit exceede O(n^2)
        '''
        
        max_price = 0
        
        for i in range(len(prices)):
            price = prices[i]
            for j in range(i+1, len(prices)):
                
                max_price = max(prices[j]-price, max_price)
                
        return max_price
    
    def maxProfit(self, prices: List[int]) -> int:
        '''
        '''
        min_price = sys.maxsize
        profit = 0
        
        for price in prices:
            min_price = min(price, min_price)
            profit = max(profit, price - min_price)
        return profit