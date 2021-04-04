# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: TreeNode, targetSum: int) -> List[List[int]]:

        result = []

        def dfs(node, cur_path, target):

            if node:

                if not node.left and not node.right:

                    if target == node.val:
                        result.append(cur_path[::] + [node.val])
                else:
                    dfs(node.left, cur_path + [node.val], target - node.val)
                    dfs(node.right, cur_path + [node.val], target - node.val)
            return

        dfs(node=root, cur_path=[], target=targetSum)

        return result