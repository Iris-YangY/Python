def count_up(start,end):
    if (start==end):
        print(end)
    else:
        count_up(start,end-1)
        print(end)

def count_up(start,end):
    if (start==end):
        print(start)
    else:
        print(start)
        count_up(start+1,end)
'''
When calling count_up on a smaller range, it would print the numbers
of that range in an ascending order.
'''
def count_up(start,end):
    if (start==end):
        print(start)
    else:
        mid=(start+end)//2
        count_up(start,mid)
        count_up(mid+1,end)

def count_down(start,end):#start<=end
    if (start==end):
        print(start)
    else:
        count_down(start+1,end)
        print(start)
'''
When calling count_down on a smaller range, it would print the numbers
of that range in a descending order.
'''
def count_up_and_down(start,end):
    if (start==end):
        print(start)
    else:
        print(start)
        count_up_and_down(start+1,end)
        print(start)
count_up_and_down(2,5)
'''
When calling count_up_and_down on a smaller range, it would print the numbers
of that range in an ascending order followed by these numbers in a descending
order.
'''
def count_appearances(lst, low, high, val):
    if(low==high):
        if(lst[low]==val):
            return 1
        else:
            return 0
    else:
        rest_count=count_appearances(lst, low+1, high, val)
        if(lst[low]==val):
            return 1+rest_count
        else:
            return rest_count

lst=[7,5,3,2,6,3,8]
x=count_appearances(lst,0,len(lst)-1,3)
