from DoublyLinkedList import DoublyLinkedList

class CompactString:
    def __init__(self, orig_str):
        self.data=DoublyLinkedList()
        count=0
        lst=DoublyLinkedList()
        for i in orig_str:
            lst.add_last(i)
        cursor=lst.header.next
        while(cursor.next!=None):
            if cursor.data==cursor.next.data:
                count+=1
            else:
                self.data.add_last((cursor.data, count+1))
                count=0
            cursor=cursor.next

    def __add__(self, other):
        '''result=CompactString('')
        for i in range(self.data.size-1):
            data=self.data.header.next
            result.data.add_last(data.data)
            data=data.next
        if self.data.trailer.prev.data[0]==other.data.header.next.data[0]:
            count=self.data.trailer.prev.data[1]+other.data.trailer.prev.data[1]
            data=(self.data.trailer.prev.data[0], count)
            result.data.add_last(data)
        else:
            for j in (other.data):
                data=other.header.next
                result.add_last(data.data)
                data=data.next
            
        return result.data
'''
        result=DoublyLinkedList()
        for i in self.data:
            result.add_last(i)
        for j in other.data:
            result.add_last(j)
        return result
    def __len__(self):
        length=0
        for i in self.data.size:
            data=self.header.next.data
            length+=data[1]
            data=data.next.data
        return length

    def __lt__(self, other):
        len1=self.data.size
        len2=other.data.size
        if len1<=len2:
            for i in range(len1):
                return self.data[0]<other.data[0]
        return False

    def __le__(self, other):
        len1=self.data.size
        len2=other.data.size
        if len1<=len2:
            for i in range(len1):
                return self.data[0]<=other.data[0]
        return False

    def __gt__(self, other):
        len1=self.data.size
        len2=other.data.size
        if len1>=len2:
            for i in range(len1):
                return self.data[0]>other.data[0]        
        return False

    def __ge__(self, other):
        len1=self.data.size
        len2=other.data.size
        if len1>=len2:
            for i in range(len1):
                return self.data[0]>=other.data[0]        
        return False

    def __repr__(self):
        return "[" + " <--> ".join([str(elem) for elem in self.data]) + "]"
