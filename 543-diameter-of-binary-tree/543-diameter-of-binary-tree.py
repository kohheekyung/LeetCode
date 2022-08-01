# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
    longest = 0
    
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        # DFS로 리프 노드까지 탐색한 후 부모까지 반환하면서 거리 계산

        def dfs(node):
            
            if not node:
                return -1
            
            # 재귀호출을 통해 왼쪽, 오른쪽 각 리프 노드까지 DFS로 탐색
            left = dfs(node.left) 
            right = dfs(node.right) 
        
            # 최종결과가 될 경로 저장 
            self.longest = max(self.longest, left + right + 2) # 루트에서 총경로 거리
            
            
            # 현 위치에서의 리프노드와 거리
            return max(left, right) + 1
        
        
        dfs(root)
        return self.longest
