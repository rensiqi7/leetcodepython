# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def levelOrderBottom(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        result = []
        if not root:
            return result
        curr_level = [root]
        while curr_level:
            level_result = []
            next_level = []
            for temp in curr_level:
                level_result.append(temp.val)
                if temp.left:
                    next_level.append(temp.left)
                if temp.right:
                    next_level.append(temp.right)
            result.append(level_result)
            curr_level = next_level
        result.reverse()
        return result


'''
class Solution:
    def levelOrderBottom(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if root==None:
            return []

        frontier = [root]
        ans = []

        while len(frontier) > 0:
            ans.insert(0,[])

            width = len(frontier)
            for i in range(width):
                node = frontier[0]
                del frontier[0]

                ans[0].append(node.val)

                if node.left != None:
                    frontier.append(node.left)
                if node.right != None:
                    frontier.append(node.right)

        return ans
'''
