from DoublyLinkedList import DoublyLinkedList
def merge_linked_lists(srt_lnk_lst1, srt_lnk_lst2):
    new=DoublyLinkedList()
    cursor1=srt_lnk_lst1.header.next
    cursor2=srt_lnk_lst2.header.next
    def merge_list(cursor1, cursor2, new):
        if cursor1.data==None and cursor2.data==None:
            return new
        if cursor1.data==None:
            new.add_last(cursor2.data)
            return merge_list(cursor1, cursor2.next, new)
        if cursor2.data==None:
            new.add_last(cursor1.data)
            return merge_list(cursor1.next, cursor2, new)
        if cursor1.data<cursor2.data:
            new.add_last(cursor1.data)
            return merge_list(cursor1.next, cursor2, new)
        if cursor1.data==cursor2.data:
            new.add_last(cursor1.data)
            new.add_last(cursor2.data)
            return merge_list(cursor1.next, cursor2.next, new)
        if cursor1.data>cursor2.data:
            new.add_last(cursor2.data)
            return merge_list(cursor1, cursor2.next, new)
    return merge_list(cursor1, cursor2, new)
