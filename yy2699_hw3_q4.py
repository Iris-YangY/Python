def remove_all(lst, value):
    '''return [elem for elem in lst if elem!=value]'''
    for i in range(lst.count(value)):
        lst.remove(value)
    return lst
