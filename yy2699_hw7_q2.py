def leaves_list(self):
    if self.is_empty():
        raise Exception("Tree is empty")
    lst=[]
    def subtree_leaves(root):
        if root is None:
            pass
        if root.left is None and root.right is None:
            yield root.data
        else:
            yield from subtree_leaves(root.left)
            yield from subtree_leaves(root.right)
        return lst
    return subtree_leaves(self.root)

def iterative_inorder(self):
    curr = self.root
    while curr is not None:
        if curr.left is None:
            yield curr.data
            curr = curr.right
        else:
            pre = curr.left
            if pre.right is None:
                pre.right = curr
                curr = curr.left
            else:
                pre.right = None
                yield curr.data
                curr = curr.right
            while pre.right is not None and pre.right != current:
                pre = pre.right
