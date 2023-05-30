from BinarySearchTreeMap import BinarySearchTreeMap
def min_max_BST(bst):
    curr_min = bst.root
    curr_max = bst.root
    while curr_min!=None:
        curr_min = curr_min.left
    while curr_max!=None
        curr_max = curr_max.right
    return (curr_min, curr_max)

def glt_n(bst, n):
    curr = bst.root
    num = -1
    while curr.left is not None or curr.right is not None:
        if curr.data == n:
            num = curr.item.key
            return
        elif curr.data>n:
            curr = curr.left
        elif curr.data<n:
            num = curr.item.key
            curr = curr.right
    return num

def compare_BST(bst1, bst2):
    lst1 = bst1.inorder()
    lst2 = bst2.inorder()
    for elem1 in lst1:
        for elem2 in lst2:
            if elem1==elem2:
                lst1.pop(elem1)
                lst2.pop(elem2)
    if len(lst1)>0 or len(len2)>0:
        return False
    return True


