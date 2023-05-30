from ArrayQueue import ArrayQueue
def preorder(self):
    def subtree_preorder(root):
        if (root is None):
            return
        else:
            yield root#gives more freedom cause root.data could not access the node
            yield from subtree_preorder(root.left)
            yield from subtree_preorder(root.right)
    yield from subtree_preorder(self.root)

def inorder(self):
    def subtree_inorder(root):
        if (root is None):
            return
        else:
            yield from subtree_inorder(root.left)
            yield root
            yield from subtree_inorder(root.right)
        yield from subtree_inorder(self.root)

def postorder(self):
    def subtree_postorder(root):
        if (root is None):
            return
        else:
            yield from subtree_postorder(root.left)
            yield from subtree_postorder(root.right)
            yield root
        yield from subtree_postorder(self.root)

def breadth_first(self):#linear time operation, runtime theta=n
    if (self.root is None):
        return
    line = ArrayQueue()
    line.enqueue(self.root)
    while (not line.is_emprty()):
        curr_node = line.dequeue()
        yield curr_node
        if (curr_node.left is not None):
            line.enqueue(curr_node.left)
        if (curr_node.right is not None):
            line.enqueue(curr_node.right)

def __iter__(self):
    for node in self.inorder():
        yield node.data
    
'''
preorder: root L R
inorder: L root R
postorder: L R root
'''
from LinkedBinaryTree import LinkedBinaryTree
r_c1=LinkedBinaryTree.Node(2)
l_c1=LinkedBinaryTree.Node(3)
r_c2=LinkedBinaryTree.Node('+', l_c1, r_c1)
l_c2=LinkedBinaryTree.Node(4)
exp_root=LinkedBinaryTree.Node('*', l_c2, r_c2)

exp_tree=LinkedBinaryTree(exp_root)

def eval_exp_tree(exp_tree):
    def eval_subtree_exp(root):
        if (root.left is None) and (root.right is None):
            return root.data
        else:
            left_arg=eval_subtree_exp(root.left)
            right_arg=eval_subtree_exp(root.right)
            if (root.data=="+"):
                return left_arg+right_arg
            elif (root.data=="-"):
                return left_arg-right_arg
            elif (root.data=="*"):
                return left_arg*right_arg
            elif (root.data=="/"):
                if (right_arg==0):
                    raise ZeroDivisionError()
                return left_arg/right_arg
            else:
                raise Exception('Unsupported operation '+root.data)
    return eval_subtree_exp(exp_tree.root)
