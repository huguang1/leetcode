"""
226. 翻转二叉树
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


def invertTree(root):
    if not root:
        return
    left = invertTree(root.left)
    right = invertTree(root.right)
    root.left, root.right = right, left
    return root


"""
101. 对称二叉树
"""


def isSymmetric(root):
    def check(p, q):
        if not p or not q:
            return p == q
        return p.val == q.val and check(p.left, q.right) and check(p.right, q.left)
    return check(root.left, root.right)


"""
104. 二叉树的最大深度
"""


def maxDepth(root):
    if not root:
        return 0
    return max(maxDepth(root.left), maxDepth(root.right)) + 1


"""
111. 二叉树的最小深度
"""


def minDepth(root):
    if not root:
        return 0
    if not root.left and not root.right:
        return 1
    mins = float('inf')
    if root.left:
        mins = min(mins, minDepth(root.left))
    if root.right:
        mins = min(mins, minDepth(root.right))
    return mins + 1


"""
222. 完全二叉树的节点个数
"""


def countNodes(root):
    if not root:
        return 0
    return countNodes(root.left) + 1 + countNodes(root.right)


"""
110. 平衡二叉树
"""


def isBalanced(root):
    if not root:
        return True

    def height(root):
        if not root:
            return 0
        return max(height(root.left), height(root.right))+1
    return abs(height(root.left)-height(root.right)) <= 1 and isBalanced(root.left) and isBalanced(root.right)


if __name__ == '__main__':
    root = TreeNode(val=0, left=TreeNode(1), right=TreeNode(1))
    # ans = invertTree(root)
    # print(preorderTraversal(ans))
    # ans = isSymmetric(root)
    # print(ans)
    # ans = minDepth(root)
    # print(ans)
    # ans = countNodes(root)
    # print(ans)
    ans = isBalanced(root)
    print(ans)




