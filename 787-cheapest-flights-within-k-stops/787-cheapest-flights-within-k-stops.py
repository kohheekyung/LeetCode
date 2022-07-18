# class Solution:
#     def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        
#         # 그래프 인접 리스트 구성
#         graph = collections.defaultdict(list)
#         for u,v,w in flights:
#             graph[u].append((v,w))
            
#         # (비용, 출발지, 남은경유횟수)
#         Q = [(0, src, k)]
     
#         # 우선순위 큐 최솟값 기준으로 도착접까지 최소 비용 판별
#         while Q:
            
#             price, node, stop = heapq.heappop(Q)
            
#             # k번 이내에 도착지 나오면 리턴
#             if node == dst:
#                 return price
            
#             if stop >= 0:
#                 for v, w in graph[node]:
#                     heapq.heappush(Q,( price+w, v, stop-1))
 
                    
#         return -1
class Solution:
    def findCheapestPrice(self, n, flights, src, dst, K):
        graph = collections.defaultdict(dict)
        for s, d, w in flights:
            graph[s][d] = w
        pq = [(0, src, K+1)]
        vis = [0] * n
        while pq:
            w, x, k = heapq.heappop(pq)
            if x == dst:
                return w
            if vis[x] >= k:
                continue
            vis[x] = k
            for y, dw in graph[x].items():
                heapq.heappush(pq, (w+dw, y, k-1))
        return -1