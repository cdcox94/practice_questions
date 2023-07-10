from typing import List, Dict, Optional
import cProfile

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if root == None:
            return 0

        global_minima = 999999999
        current_depth = 1
        if root.left != None:
            local_minima = self.maybe_recursion(root=root.left, current_depth=current_depth+1, global_minima=global_minima)
            if local_minima<global_minima:
                global_minima = local_minima
        if root.right!=None:
            local_minima = self.maybe_recursion(root=root.right, current_depth=current_depth+1, global_minima=global_minima)
            if local_minima<global_minima:
                global_minima = local_minima

        if global_minima==999999999:
            return 1
        return global_minima

    def maybe_recursion(self, root:TreeNode, current_depth, global_minima):
        if current_depth>global_minima:
            return 9999999999
        if root.left == None and root.right == None:
            global_minima = current_depth
        else:
            if root.left!=None:
                local_minima = self.maybe_recursion(root=root.left, current_depth=current_depth+1, global_minima=global_minima)
                if local_minima<global_minima:
                    global_minima = local_minima
            if root.right!=None:
                local_minima = self.maybe_recursion(root=root.right, current_depth=current_depth+1, global_minima=global_minima)
                if local_minima<global_minima:
                    global_minima = local_minima
        return global_minima

def test():
    
    sol = Solution()
    
    root = [3,9,20,None,None,15,7]
    tree = build_tree(root)
    solution = sol.minDepth(tree)
    print(solution)
    assert solution == 2


if __name__ == "__main__":
    cProfile.run('test()')