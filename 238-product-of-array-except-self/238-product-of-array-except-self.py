class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        '''
        왼쪽부터 곱하고, 오른쪽부터 곱함
        '''
        out = []

        # 왼쪽 곱셈
        p = 1
        for i in range(0, len(nums)):
            out.append(p)
            p = p*nums[i]

        # 왼쪽 곱셈 결과에 오른쪽 마지막 값부터 차례대로 곱해나감
        p = 1
        for i in range(len(nums)-1, -1,  -1):
            out[i] = out[i] * p
            p = p*nums[i]                                                                                                                                                                                                                                                                                                                                                                                  
        return out
        
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                