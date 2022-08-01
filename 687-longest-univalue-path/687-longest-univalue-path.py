# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    result = 0
    def longestUnivaluePath(self, root: Optional[TreeNode]) -> int:
        '''
        DFS로 리프노드까지 탐색해 내려간 후 동일한 값의 거리 취합
        '''
        def dfs(node):
            
            # 노드가 존재하지 않으면 0 반환
            if node is None:
                return 0
            
            # 리프 노드에 이르러서 값 반환
            left = dfs(node.left)
            right = dfs(node.right)
            
            if node.left and node.left.val == node.val:
                left += 1
            else:
                left = 0
            if node.right and node.right.val == node.val:
                right +=1
            else:
                right = 0
            
            # 양쪽노드 거리의 합
            self.result = max(self.result, left+right)
            
            # 현재까지의 거리 리턴
            return max(left, right)
            
            
            
        dfs(root)
        
        return self.result