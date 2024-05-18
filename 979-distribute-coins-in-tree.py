# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def distributeCoins(self, root: Optional[TreeNode]) -> int:
        self.moves = 0

        def dfs(node):
            if node is None:
                return 0

            left_diff = dfs(node.left)
            right_diff = dfs(node.right)

            self.moves += abs(left_diff) + abs(right_diff)

            return node.val + left_diff + right_diff - 1

        dfs(root)

        return self.moves
