"""
257. 二叉树的所有路径
"""


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def binaryTreePaths(root):
    ans = []

    def dfs(root, path):
        if not root:
            return
        if not root.left and not root.right:
            ans.append(path + str(root.val))
        path = path + str(root.val) + '->'
        if root.left:
            dfs(root.left, path)
        if root.right:
            dfs(root.right, path)
    dfs(root, '')
    return ans


"""
404. 左叶子之和
"""


def sumOfLeftLeaves(root):
    ans = 0
    if not root:
        return 0
    if root.left and not root.left.left and not root.left.right:
        ans += root.left.val
    ans += sumOfLeftLeaves(root.left)
    ans += sumOfLeftLeaves(root.right)
    return ans


"""
112. 路径总和, 需要查看所有的路径，以及对节点进行操作
"""


def hasPathSum(root, targetSum):
    if not root:
        return False
    if not root.left and not root.right and root.val == targetSum:
        return True
    return hasPathSum(root.left, targetSum - root.val) or hasPathSum(root.right, targetSum - root.val)


if __name__ == '__main__':
    root = TreeNode(val=0, left=TreeNode(1), right=TreeNode(2))
    ans = sumOfLeftLeaves(root)
    print(ans)







