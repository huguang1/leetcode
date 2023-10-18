"""
105. 从前序与中序遍历序列构造二叉树
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


def buildTree(preorder, inorder):
    if not preorder:
        return
    val = preorder[0]
    node = TreeNode(val)
    for i, v in enumerate(inorder):
        if v == val:
            node.left = buildTree(preorder[1: i+1], inorder[:i])
            node.right = buildTree(preorder[i+1:], inorder[i+1:])
    return node


def build(inorder, postorder):
    if not postorder:
        return
    val = postorder[-1]
    node = TreeNode(val)
    for i, v in enumerate(inorder):
        if v == val:
            node.left = buildTree(inorder[:i], postorder[:i])
            node.right = buildTree(inorder[i+1:], postorder[i:-1])
    return node


"""
617. 合并二叉树
"""


def mergeTrees(root1, root2):
    if not root1:
        return root2
    if not root2:
        return root1
    root = TreeNode(root1.val + root2.val)
    root.left = mergeTrees(root1.left, root2.left)
    root.right = mergeTrees(root1.right, root2.right)
    return root


"""
700. 二叉搜索树中的搜索
"""


def searchBST(root, val):
    while root:
        if root.val == val:
            return root
        elif root.val > val:
            root = root.left
        else:
            root = root.right
    return


"""
98. 验证二叉搜索树
"""


def isValidBST(root):
    stack, mins = [], float('-inf')
    while root or stack:
        while root:
            stack.append(root)
            root = root.left
        root = stack.pop()
        if root.val <= mins:
            return False
        mins = root.val
        root = root.right
    return True


"""
530. 二叉搜索树的最小绝对差
"""


def getMinimumDifference(root):
    stack, mins, ans = [], float('-inf'), float('inf')
    while stack or root:
        while root:
            stack.append(root)
            root = root.left
        root = stack.pop()
        ans = min(ans, root.val-mins)
        mins = root.val
        root = root.right
    return ans


if __name__ == '__main__':
    # preorder, inorder = [3, 9, 20, 15, 7], [9, 3, 15, 20, 7]
    # root = buildTree(preorder, inorder)
    # print(preorderTraversal(root))
    inorder, postorder = [9, 3, 15, 20, 7], [9, 15, 7, 20, 3]
    ans = build(inorder, postorder)
    print(preorderTraversal(ans))

