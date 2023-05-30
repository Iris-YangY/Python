from LinkedBinaryTree import LinkedBinaryTree
class EmptyTree(Exception):
    pass
def min_and_max(bin_tree):
    if bin_tree.is_empty():
        raise EmptyTree
    minnum=root.data
    maxnum=root.data
    def subtree_min_and_max(root):
        if (root.left is None and root.right is None):
            return (root.data, root.data)
        elif root.left is None:
            minnum=min(minnum, root.data, subtree_min_and_max(root.right))
            maxnum=max(maxnum, root.data, subtree_min_and_max(root.right))
        elif root.right is None:
            minnum=min(minnum, root.data, subtree_min_and_max(root.left))
            maxnum=max(maxnum, root.data, subtree_min_and_max(root.left))
        else:
            minnum=min(minnum, root.data, subtree_min_and_max(root.left), subtree_min_and_max(root.right))
            maxnum=max(maxnum, root.data, subtree_min_and_max(root.left), subtree_min_and_max(root.right))
        return (minnum, maxnum)
    return subtree_min_and_max(bin_tree.root)
