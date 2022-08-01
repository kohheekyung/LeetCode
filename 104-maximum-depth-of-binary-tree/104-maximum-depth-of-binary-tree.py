# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        # BFS로 풀이함으로 큐사용

        if root is None:
            return 0
        # 현재 큥에는 현재 깊이(depth)에 해당하는 모든 노드가 들어가게 됨
        queue = collections.deque([root])
        depth = 0
        
        while queue:
            # while의 반복횟수가 깊이와 동일
            depth += 1
            
            # 부모 노드의 수만큼 반복하여 자식 노두 삽입
            for _ in range(len(queue)):
                curr_root = queue.popleft()
            
                #자식노드가 있으면 queue에 삽입
                if curr_root.left:
                    queue.append(curr_root.left)
                if curr_root.right:
                    queue.append(curr_root.right)
            
        return depth