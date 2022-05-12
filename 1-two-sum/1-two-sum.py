class Solution:
    
    def twoSum_bruteforce(self, nums: List[int], target: int) -> List[int]:
        '''
        Runtime: 4500 ms
        Memory: 14.9 MB
        '''
        
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]
                
    def twoSum_usingIn(self, nums: List[int], target: int) -> List[int]:
        '''
        Runtime: 916 ms
        Memory: 14.9 MB
        '''
        for i in range(len(nums)):
            
            # 타겟에서 현재 값 빼서 필요한 값 파악
            complement = target - nums[i]
            
            # 남은 리스트에서 필요한 값 존재하면 반환
            if complement in nums[i+1:]:
                return [i, nums[i+1:].index(complement) + (i+1)]
            
    def twoSum_usingDict(self, nums: List[int], target: int) -> List[int]:
        '''
        Runtime: 136 ms
        Memory: 15.4 MB
        '''
        # 키를 num 값을 index로 딕셔너리 저장
        nums_map = {}
        for i, num in enumerate(nums):
            nums_map[num] = i

        # 타겟에서 첫번째 수를 뺀 결과를 키로 조회
        for i, num in enumerate(nums):
            if target - num in nums_map and i != nums_map[target-num]:
                return i, nums_map[target-num]
    
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        nums_map = {}
        for i, num in enumerate(nums):
                if target - num in nums_map:
                    return nums_map[target - num], i
                nums_map[num] = i