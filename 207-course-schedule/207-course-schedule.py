class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        
        
        graph = collections.defaultdict(list)
        for a, b in prerequisites:
            graph[a].append(b)
            
        traced = set()
        visited = set()
        
        def dfs(a):
            
            # 이미 들은 코스면 False 반환
            if a in traced:
                return False
            
            # 이미 방문한 곳이면 True 반환
            if a in visited:
                return True
            
            traced.add(a)
            
            for b in graph[a]:
                if not dfs(b):
                    return False
                
            # 탐색종료 후 순환노드 삭제
            traced.remove(a)
            # 방문 표시
            visited.add(a)
            return True

        # 순환 구조 판별
        for x in list(graph):
         
            if not dfs(x):
                return False
            
        return True