class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        
        # 그래프 인접 리스트 구성
        graph = collections.defaultdict(list)
        for u,v,w in flights:
            graph[u].append((v,w))
            
        # (비용, 출발지, 남은경유횟수)
        Q = [(0, src, k)]
        vis = [0] * n
        # 우선순위 큐 최솟값 기준으로 도착접까지 최소 비용 판별
        while Q:
            
            price, node, stop = heapq.heappop(Q)
            
            # k번 이내에 도착지 나오면 리턴
            if node == dst:
                return price
            
            if vis[node] > stop:
                continue
            vis[node] = stop
            
    
            if stop >= 0:
                for v, w in graph[node]:
                    heapq.heappush(Q,( price+w, v, stop-1))
           
        return -1
    
