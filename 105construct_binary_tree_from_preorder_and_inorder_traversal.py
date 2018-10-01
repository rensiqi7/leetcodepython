# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        """
        n = len(preorder)
        if not n:
            return None
        root = TreeNode(preorder[0])
        inorder_index = dict()
        for i in range(n):
            inorder_index[inorder[i]] = i
        queue = [(root, 1, n - 1, 0, n - 1)]
        while len(queue):
            data = queue.pop(0)
            curroot_inorder = inorder_index[data[0].val]
            # left subtree len including left subroot
            len_l = curroot_inorder - data[3]
            # right subtree len including right subroot
            len_r = data[4] - curroot_inorder
            if len_l:
                lchild = TreeNode(preorder[data[1]])
                queue.append(
                    (lchild, data[1] + 1, data[1] + len_l - 1, data[3], curroot_inorder - 1))
                data[0].left = lchild
            if len_r:
                rchild = TreeNode(preorder[data[1] + len_l])
                queue.append(
                    (rchild, data[1] + len_l + 1, data[2], curroot_inorder + 1, data[4]))
                data[0].right = rchild
        return root
