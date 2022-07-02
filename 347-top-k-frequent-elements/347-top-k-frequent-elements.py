class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
 
        # most_commom함수로 k순위로 자주 나오는 요소 반환
        most_k = collections.Counter(nums).most_common(k)
 
        # *로 딕셔러니 언팩후 zip으로 요소 재정합후 맨앞요소만 반환
        return list(zip(*most_k))[0]
 
        
    