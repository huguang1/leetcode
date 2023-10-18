"""
701. 二叉搜索树中的插入操作
"""


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def preorderTraversal(root):
    if not root:
        return []
    return [root.val] + preorderTraversal(root.left) + preorderTraversal(root.right)


def insertIntoBST(root, val):
    if not root:
        return TreeNode(val)
    if root.val < val:
        root.right = insertIntoBST(root.right, val)
    else:
        root.left = insertIntoBST(root.left, val)
    return root


"""
450. 删除二叉搜索树中的节点
"""


def deleteNode(root, key):
    if not root:
        return
    if root.val == key:
        if not root.right:
            return root.left
        cur = root.right
        while cur.left:
            cur = cur.left
        cur.val, root.val = root.val, cur.val
    root.left = deleteNode(root.left, key)
    root.right = deleteNode(root.right, key)
    return root


"""
669. 修剪二叉搜索树
"""


def trimBST(root, low, high):
    if not root:
        return
    if root.val < low:
        return trimBST(root.right, low, high)
    if root.val > high:
        return trimBST(root.left, low, high)
    root.left = trimBST(root.left, low, high)
    root.right = trimBST(root.right, low, high)
    return root


"""
538. 把二叉搜索树转换为累加树
"""


def convertBST(root):
    count = 0

    def dfs(root):
        nonlocal count
        if not root:
            return
        dfs(root.right)
        count += root.val
        root.val = count
        dfs(root.left)
        return root
    return dfs(root)





