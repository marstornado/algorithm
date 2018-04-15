from collections import deque


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        """
        :type x: int
        :rtype: TreeNode
        """
        self.val = x
        self.left = None
        self.right = None

    @staticmethod
    def convert_list_to_tree(list):
        """
        :type list: List
        :rtype: TreeNode
        """
        n = iter(list)
        root = TreeNode(next(n))
        treenode_list = deque([root])
        while True:
            head = treenode_list.popleft()
            try:
                head.left = TreeNode(next(n))
                treenode_list.append(head.left)
                head.right = TreeNode(next(n))
                treenode_list.append(head.right)
            except StopIteration:
                break
        return root

    @staticmethod
    def convert_tree_to_list(tree):
        """
        :type tree: TreeNode
        :rtype: List
        """
        list = []
        if tree:
            treenode_list = deque([tree])
            while treenode_list:
                head = treenode_list.popleft()
                if head:
                    list.append(head.val)
                    if head.left:
                        treenode_list.append(head.left)
                    if head.right:
                        treenode_list.append(head.right)
                else:
                    list.append(None)
        return list
