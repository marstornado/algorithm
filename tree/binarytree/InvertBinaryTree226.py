'''
https://leetcode.com/problems/invert-binary-tree/description/
Invert a binary tree.

     4
   /   \
  2     7
 / \   / \
1   3 6   9
to

     4
   /   \
  7     2
 / \   / \
9   6 3   1
'''
from tree.TreeNode import TreeNode


class Solution(object):
    def invertTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        if root:
            root.left, root.right = self.invertTree(root.right), self.invertTree(root.left)
        return root


test_data = [4, 2, 7, 1, 3, 6, 9]
print('Input data is ', test_data)
tree = TreeNode.convert_list_to_tree(test_data)
root = Solution().invertTree(tree)
print('Output data is ', TreeNode.convert_tree_to_list(root))
