from BinarySearchTreeMap import BinarySearchTreeMap
def create_chain_bst(n):
    bst = BinarySearchTreeMap()
    for i in range(n):
        bst.insert(i+1)
    return bst

def create_complete_bst(n):
    bst = BinarySearchTreeMap()
    add_items(bst, 1, n)
    return bst

def add_items(bst, low, high):
    if high==0:
        bst.insert(0)
    if low==high:
        bst.insert(low)
    else:
        root = (low+high)//2
        bst.insert(root)
        add_items(bst, low, root-1)
        add_items(bst, root+1, high)
