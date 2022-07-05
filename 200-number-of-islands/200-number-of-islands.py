class Solution:
    
    def numIslands(self, grid: List[List[str]]) -> int:
        
        
        def dfs(m,n):
           
            # 예외처리
            if m < 0 or m >= len(grid) or n<0 or n>=len(grid[0]):
                return 
            
            # 섬이면
            if grid[m][n] == '1':
                #방문 표시
                grid[m][n] = '0'
                
                # 상하좌우 방문하여 섬이면 방문처리
                dfs(m, n+1) #우
                dfs(m, n-1) #좌
                dfs(m+1, n) #하
                dfs(m-1, n) #상
            # 섬아니면 반환
            else: 
                return
              
         
    
        num = 0
        
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                # 섬이면 
                if grid[i][j] == '1':
                    # 섬 개수 추가 후 dfs로 상하좌우 방문하여 섬 방문 표시
                    num +=1
                    dfs(i,j)
        return num