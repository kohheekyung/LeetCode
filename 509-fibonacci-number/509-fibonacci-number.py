class Solution:
    def fib_recursive(self, n: int) -> int:
        '''
        Time Complexity O(2^n)
        Space Complexity O(n)
        
        '''
        if n <= 1:
            return n
        
        return self.fib(n-1) + self.fib(n-2)

    
    
          
    # create a map
    cache = {0: 0, 1: 1}    
        
    def fib(self, n: int) -> int:
        '''
        Top-down approach using memoization
        
        Time Complexity O(n) starting at 2 upt to n
        Space Complexity O(n) size of the stack in memory is proportional to N
        '''
        
        # if n exists in the map return the cached value
        if n in self.cache:
            return  self.cache[n]
        # otherwise set the key n and value fib(n-1) + fib(n-2)
        self.cache[n] = self.fib(n-1) + self.fib(n-2)
        return self.cache[n]
        

  