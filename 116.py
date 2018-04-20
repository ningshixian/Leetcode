'''
116. Populating Next Right Pointers in Each Node
Given a binary tree

    struct TreeLinkNode {
      TreeLinkNode *left;
      TreeLinkNode *right;
      TreeLinkNode *next;
    }
Populate each next pointer to point to its next right node. If there is no next right node, the next pointer should be set to NULL.

Initially, all next pointers are set to NULL.

这题需要在一棵完全二叉树中使用next指针连接旁边的节点， 我们可以发现一些规律。
如果一个子节点是根节点的左子树， 那么它的next就是该根节点的右子树， 譬如上面例子中的4， 它的
next就是2的右子树5。
如果一个子节点是根节点的右子树， 那么它的next就是该根节点next节点的左子树。 譬如上面的5， 它
的next就是2的next（ 也就是3） 的左子树。

For example,
Given the following perfect binary tree,
         1
       /  \
      2    3
     / \  / \
    4  5  6  7
After calling your function, the tree should look like:
         1 -> NULL
       /  \
      2 -> 3 -> NULL
     / \  / \
    4->5->6->7 -> NULL
'''
# Definition for binary tree with next pointer.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
        self.next = None

class Solution:
    # @param root, a tree link node
    # @return nothing
    def connect(self, root):
        if not root:
            return
        # # 层级遍历方法
        # Q=[root]
        # while Q:
        #     length=len(Q)
        #     while length:
        #         a = Q[0]
        #         Q=Q[1:]
        #         length-=1
        #         a.next = Q[0] if length else None
        #         if a.left:
        #             Q.append(a.left)
        #         if a.right:
        #             Q.append(a.right)

        # 高级方法
        p = root
        first = None
        while p:
            if not first:
                first = p.left
            if p.left:
                p.left.next = p.right
            else:
                break
            if p.next:
                p.right.next = p.next.left
                p = p.next
            else:
                p = first
                first = None


s = Solution()
root = TreeNode(1)
a = TreeNode(2)
b=TreeNode(3)
c = TreeNode(4)
d=TreeNode(5)
e = TreeNode(6)
f=TreeNode(7)

root.left = a
root.right = b
a.left = c
a.right = d
b.left = e
b.right = f
print(s.connect(root))