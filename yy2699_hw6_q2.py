from DoublyLinkedList import DoublyLinkedList

class Integer:
    def __init__(self, num_str):
        self.data = DoublyLinkedList()
        for i in num_str:
            self.data.add_last(int(i))

    def __add__(self, other):
        selflen=self.data.size
        otherlen=other.data.size
        lendif=abs(selflen-otherlen)
        if selflen>otherlen:
            for i in range(lendif):
                other.data.add_first(0)
        if otherlen>selflen:
            for i in range(lendif):
                self.data.add_first(0)    
        extra=0
        digit=0
        result=Integer('')
        last1=self.data.trailer.prev
        last2=other.data.trailer.prev
        while (last1 is not self.data.header) and (last2 is not other.data.header):
            int1=last1.data
            int2=last2.data
            res=int1+int2
            digit=res%10
            digit+=extra
            extra=0
            if res>=10:
                extra=1
            if digit==10:
                digit=0
                extra=1
            result.data.add_first(str(digit))
            last1=last1.prev
            last2=last2.prev
        if extra!=0:
            result.data.add_first('1')
        while result.data.header.next.data=='0':
            result.data.delete_first()
        return result
    '''def __mul__(self, other):
        selflen=self.data.size
        otherlen=other.data.size
        if selflen<=otherlen:
            snum=self.data
            lnum=other.data
        else:
            snum=other.data
            lnum=self.data
    '''
    def __repr__(self):
        return "".join(str(elem) for elem in self.data)
