"""
144. 二叉树的前序遍历
94. 二叉树的中序遍历
145. 二叉树的后序遍历
递归遍历
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


def postorderTraversal(root):
    if not root:
        return []
    return postorderTraversal(root.left) + postorderTraversal(root.right) + [root.val]


def inorderTraversal(root):
    if not root:
        return []
    return inorderTraversal(root.left) + [root.val] + inorderTraversal(root.right)


"""
迭代遍历
"""


def preorder(root):
    stack, ans = [], []
    while root or stack:
        while root:
            ans.append(root.val)
            stack.append(root)
            root = root.left
        root = stack.pop()
        root = root.right
    return ans


def inorder(root):
    stack, ans = [], []
    while root or stack:
        while root:
            stack.append(root)
            root = root.left
        root = stack.pop()
        ans.append(root.val)
        root = root.right
    return ans


def postorder(root):
    stack, ans = [], []
    while root or stack:
        while root:
            ans.append(root.val)
            stack.append(root)
            root = root.right
        root = stack.pop()
        root = root.left
    return ans[::-1]


"""
层序遍历
"""
import collections


def levelOrder(root):
    if not root:
        return []
    queue = collections.deque()
    queue.append(root)
    ans = []
    while queue:
        l = len(queue)
        new = []
        for _ in range(l):
            node = queue.popleft()
            new.append(node.val)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        ans.append(new)
    return ans


if __name__ == '__main__':
    root = TreeNode(val=0, left=TreeNode(1), right=TreeNode(2))
    # ans = preorderTraversal(root)
    # print(ans)
    # ans = postorderTraversal(root)
    # print(ans)
    # ans = inorderTraversal(root)
    # print(ans)
    # ans = inorder(root)
    # print(ans)
    # ans = preorder(root)
    # print(ans)
    # ans = postorder(root)
    # print(ans)
    ans = levelOrder(root)
    print(ans)



