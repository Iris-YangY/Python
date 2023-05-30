'''
preorder: ABDCEGF
inorder: BDAGECF
postorder: DBGEFCA
ABCDEFG
3
1 1 0
'''
from LinkedBinaryTree import LinkedBinaryTree
def binary_tree_even_sum(root):
    for node in root:
        if node.data==None:
            return
        elif node.data%2==0:
            right=binary_tree_even_sum(node.right)
            left=binary_tree_even_sum(node.left)
            return node.data+right+left
        else:
            right=binary_tree_even_sum(node.right)
            left=binary_tree_even_sum(node.left)
            return right+left

def binary_tree_has_val(root, val):
    for data in root.data:
        if data==val:
            return True
    return False

from ArrayQueue import ArrayQueue
def invert_binary_tree1(root):
    if not (root.data==None):
        root.right, root.left=root.left, root.right
        invert_binary_tree1(root.right)
        invert_binary_tree1(root.left)

def invert_binary_tree2(root):
    '''using queue to add as each layer, and dequeue accordingly'''

def is_full(root):
    if not (root.data==None):
        has_2=root.right!=None and root.left!=None
        has_0=root.right==None and root.left==None
        return has_2 or has_0 and is_full(root.left) and is_full(root.right)

def is_complete(root):
    '''breadth first search:
if each level the number of elements==2^level power
the tree is complete, or otherwise.'''
    q=ArrayQueue()
    q.enqueue(root)
    while q is not None:
        if len(q)!=2**depth:
            return False
        for i in range(len(q)):
            node=q.dequeue()
            if not (root.right==None):
                q.enqueue(root.right)
            if not (root.left==None):
                q.enqueue(root.left)
        depth+=1
    return True

def preorder_with_stack(root):
    stack=ArrayStack()
    s.push(root)
    while s is not None:
        node=s.pop()
        yield node.data
        if (node.left!=None):
            s.push(node.left)
        if (node.left!=None):
            s.push(node.right)
