'''
Binary search tree: all left keys are smaller than all right keys
'''
class BinarySearchTreeMap:
    class Item:
        def __init__(self, key, value=None):
            self.key = key
            self.value = value
    class Node:
        def __init__(self, item):
            self.item = item
            self.left = None
            self.right = None
            self.parent = None
        def num_children(self):
            count = 0
            if (self.left is not None):
                count+=1
            if (self.right is not None):
                count+=1
            return count
        def disconnect(self):
            self.item = None
            self.left = None
            self.right = None
            self.parent = None

    def __init__(self):
        self.root = None
        self.size = 0

    def __len__(self):
        return self.size

    def is_empty(self):
        return (len(self)==0)

    def __getitem__(self, key):
        node = self.find(key)
        if (node is not None):
            return node.item.value
        else:
            raise KeyError(str(key) + " not found.")
        
    def find(self, key):
        curr = self.root
        while (curr is not None):
            if (key==curr.item.key):
                return curr
            elif (key<curr.item.key):
                curr = curr.left
            elif (key>curr.item.key):
                curr = curr.right
        return None
        
    def __setitem__(self, key, value):
        node = self.find(key)
        if (node is not None):
            node.item.value = value
        else:
            self.insert(key, value)

    def insert(self, key, value):
        new_item = BinarySearchTreeMap.Item(key, value)
        new_node = BinarySearchTreeMap.Node(new_item)
        parent = self.root
        if (key<self.root.item.key):
            curr = self.root.left
        else:
            curr = self.root.right
        while (curr is not None):
            parent = curr
            if (key<self.root.item.key):
                curr = curr.left
            else:
                curr = curr.right
        if (key<parent.item.key):
            parent.left = new_node
        else:
            parent_right = new_node
        new_node.parent = parent
        self.size+=1

    def __delitem__(self, key):
        node = self.find(key)
        if(node is None):
            raise KeyError(str(key)+" not found.")
        else:
            self.delete(node)

    def delete(self, node_to_delete):
        item = node_to_delete.item
        num_of_children = node_to_delete.num_children()
        
        if node_to_delete is self.root:
            if num_of_children == 0:
                self.root = None
                node_to_delete.disconnect()
                self.size-=1
            elif num_of_children ==1:
                if self.root.left is not None:
                    self.root = self.root.right
                else:
                    self.root = self.root.right
                self.root.parent = None
                node_to_delete.disconnect()
                self.size -= 1
            else:
                max_of_left  = self.subtree_max(node_to_delete.left)
                node_to_delete.item = max_of_left.item
                self.delete(max_of_left)
        else:
            if (num_of_children == 0):#leaves
                parent = node_to_delete.parent
                if parent.left is noede_to_delete:
                    parent.left = None
                else:
                    parent.right = None
                self.size-=1
                node_to_delete.disconnect()
                
            elif (num_of_children == 1):
                parent = node_to_delete.parent
                if node_to_delete.left is not None:
                    child = node_to_delete.left
                else:
                    child = node_to_delete.right
                if parent.left is node_to_delete:
                    parent.left = child
                else:
                    parent.right = child
                child.parent = parent
                self.size-=1
                node_to_delete.disconnect()
                
            elif (num_of_children == 2):#max in left or min in right
                max_in_left = self.subtree_max(node_to_delete.left)
                node_to_delete.item = max_in_left.item
                self.delete(max_in_left)
        return item

    def subtree_max(self, subtree_root):
        curr = subtree.root
        while (curr.right is not None):
            curr = curr.right
        return curr

    def inorder(self):
        def subtree_inorder(root):
            if (root is None):
                return
            else:
                yield from subtree_inorder(root.left)
                yield root
                yield from subtree_inorder(root.right)
        yield from subtree_inorder(self.root)

    def __iter__(self):
        for node in self.inorder():
            yield node.item.key
