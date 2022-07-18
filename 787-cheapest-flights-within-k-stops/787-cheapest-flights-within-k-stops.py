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
    
    
import heapq
class Solution:
    
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, K: int) -> int:
        
        # Build the adjacency matrix
        adj_matrix = [[0 for _ in range(n)] for _ in range(n)]
        for s, d, w in flights:
            adj_matrix[s][d] = w
            
        # Shortest distances array
        distances = [float("inf") for _ in range(n)]
        current_stops = [float("inf") for _ in range(n)]
        distances[src], current_stops[src] = 0, 0
        
        # Data is (cost, stops, node)
        minHeap = [(0, 0, src)]     
        
        while minHeap:
            
            cost, stops, node = heapq.heappop(minHeap)
            
            # If destination is reached, return the cost to get here
            if node == dst:
                return cost
            
            # If there are no more steps left, continue 
            if stops == K + 1:
                continue
             
            # Examine and relax all neighboring edges if possible 
            for nei in range(n):
                if adj_matrix[node][nei] > 0:
                    dU, dV, wUV = cost, distances[nei], adj_matrix[node][nei]
                    
                    # Better cost?
                    if dU + wUV < dV:
                        distances[nei] = dU + wUV
                        heapq.heappush(minHeap, (dU + wUV, stops + 1, nei))
                        current_stops[nei] = stops
                    elif stops < current_stops[nei]:
                        #  Better steps?
                        heapq.heappush(minHeap, (dU + wUV, stops + 1, nei))
                        
        return -1 if distances[dst] == float("inf") else distances[dst]