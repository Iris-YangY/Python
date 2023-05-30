from DoublyLinkedList import DoublyLinkedList

def copy_linked_list(lnk_lst):
    lnk_lst2=DoublyLinkedList()
    lnk_lst2.header.next=lnk_lst.header.next
    lnk_lst2.trailer.prev=lnk_lst.trailer.prev
    return lnk_lst2

def deep_copy_linked_list(lnk_lst):
    lnk_lst2=DoublyLinkedList()
    cursor=lnk_lst.header.next
    print(type(cursor.data)==int)
    while cursor is not lnk_lst.trailer:
        if type(cursor.data)==int:
            lnk_lst2.add_last(cursor.data)
        else:
            lnk_lst2.add_last(deep_copy_linked_list(cursor.data))
        cursor=cursor.next
    return lnk_lst2
