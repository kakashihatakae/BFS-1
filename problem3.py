class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    def rightSideView(self, root: TreeNode) -> List[int]:
        ans = []
        
        def helper(root, level):
            if root == None:
                return 
            
            if len(ans) < level:
                ans.append(root.val)
            else:
                ans[level-1] = root.val
            
            helper(root.left, level+1)
            helper(root.right, level+1)
        
        helper(root,1)
        return ans