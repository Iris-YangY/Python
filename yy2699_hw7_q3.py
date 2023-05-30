from LinkedBinaryTree import LinkedBinaryTree
def is_height_balanced(bin_tree):
    def subtree_height(root):
        if (root.left is None and root.right is None):
            return (1, True)
        elif (root.right is None):
            height=subtree_height(root.left)[0]+1
            right=1
            diff=height-right
            if diff>1:
                return (height, False)
            else:
                return (height, subtree_height(root.left)[1])
        elif (root.left is None):
            height=subtree(root.right)[0]+1
            left=1
            diff=height-left
            if diff>1:
                return (height, False)
            else:
                return (height, subtree_height(root.right)[1])
        else:
            height=max(subtree_height(root.left)[0], subtree_height(root.right)[0])+1
            res=subtree_height(root.left)[1] and subtree_height(root.right)[1]
            return (height, res)
    return subtree_height(bin_tree.root)[1]
