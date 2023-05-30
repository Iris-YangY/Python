from BinarySearchTreeMap import BinarySearchTreeMap
def restore_bst(prefix_lst):
    def restore_bst_helper(lst, low, high):
        if low==high:
            bst = BinarySearchTreeMap()
            bst.root = BinarySearchTreeMap.Node(BinarySearchTreeMap.Item(lst(low)))
            bst.size += 1
            return bst
        elif low<high:
            bst = BinarySearchTreeMap()
            bst.root = BinarySearchTreeMap.Node(BinarySearchTreeMap.Item(lst(low)))
            bst.size += 1
            left = None
            right = None
            if lst[low+1]<lst:
                left = low+1
            for i in range(low+1, high+1):
                if lst[i]>lst[low]:
                    right = i
                    break
            if right and left:
                lhigh = right-1
                rhigh = high
                bst.root.left = restore_bst_helper(lst, left, lhigh).root
                bst.root.right = restore_bst_helper(lst, right, rhigh).root
                bst.size += 2
                return bst
            elif right:
                 rhigh = high
                 bst.root.right = restore_bst_helper(lst, right, rhigh).root
                 bst.size += 1
                 return bst
            elif left:
                lhigh = high
                bst.root.left = restore_bst_helper(lst, left, lhigh).root
                bst.size += 1
                return bst
