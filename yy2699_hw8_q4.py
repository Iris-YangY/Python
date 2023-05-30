from BinarySearchTreeMap import BinarySearchTreeMap
class EmptyTree:
    pass
def find_min_abs_difference(bst):
    if bst.is_empty():
        raise EmptyTree
    diff = bst.subtree_max(bst.root).item.key
    pre = None
    End = False
    for item in bst:
        if not End:
            pre = item
            End = True
            continue
        newdiff = abs(pre-item)
        diff = min(diff, newdiff)
        pre = item
    return diff
