from LinkedBinaryTree import LinkedBinaryTree
def create_expression_tree(prefix_exp_str):
    prefix_exp = prefix_exp_str.split(" ")
    operations="+-*/"
    start_pos=0
    def create_expression_tree_helper(prefix_exp, start_pos):
        elem = prefix_exp[start_pos]
        start_pos+=1
        node = None
        size=0
        if elem in operations:
            lsize = create_expression_tree_helper(prefix_exp, start_pos)[1]
            rsize = create_expression_tree_helper(prefix_exp, start_pos+lsize)[1]
            left = create_expression_tree_helper(prefix_exp, start_pos)[0]
            right = create_expression_tree_helper(prefix_exp, start_pos+lsize)[0]
            size = lsize+rsize+1
            node = LinkedBinaryTree.Node(elem, left, right)
        else:
            node = LinkedBinaryTree.Node(int(elem))
        return (node, size)
    return LinkedBinaryTree(create_expression_tree_helper(prefix_exp, start_pos)[0])

def prefix_to_postfix(prefix_exp_str):
    tree = create_expression_tree(prefix_exp_str)
    def subtree_postfix(root):
        if (root is None):
            pass
        else:
            yield from subtree_postfix(root.left)
            yield from subtree_postfix(root.right)
            yield root.data
    return " ".join(list(str(subtree_postfix(tree.root))))
