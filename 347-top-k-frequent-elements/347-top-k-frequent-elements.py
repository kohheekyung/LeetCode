class Solution:
    def topKFrequent_python(self, nums: List[int], k: int) -> List[int]:
 
        # most_commom함수로 k순위로 자주 나오는 요소 반환
        most_k = collections.Counter(nums).most_common(k)
 
        # *로 딕셔러니 언팩후 zip으로 요소 재정합후 맨앞요소만 반환
        return list(zip(*most_k))[0]
    
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        '''
        heap사용하여 개수가 가장 많은 요소를 우선순위에 저장
        
        Time O(N + NlogK) 
        Space O(N+k) N:num hash map k : heap element
        '''
        # 개수 딕셔너리 구하기
        num_freqs = collections.Counter(nums)
 
        # 우선순위 큐에 저장하기
        freqs_heapq = []
        for freq in num_freqs:
            # 개수가 많은 요소가 우선순위에 있도록 함
            # minheap임으로 -를 붙여 큰값이 앞에 위치하도록
            heapq.heappush(freqs_heapq, (-num_freqs[freq], freq))
            
        # 우선순위 큐에서 작은순으로 추출하기
        topK = []
        for _ in range(k):
            # element추출
            topK.append(heapq.heappop(freqs_heapq)[1])
        return topK
    
    