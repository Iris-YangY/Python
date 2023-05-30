def print_triangle(n):
    res=''
    if n==1:
        res="*"+"\n"
    else:
        res=print_triangle(n-1)
        res+=str(n*"*"+"\n")
    return res

def print_oposite_triangles(n):
    res=''
    if n==0:
        return ''
    else:
        res+="*"*n+"\n"
        res+=print_oposite_triangles(n-1)
        res+="*"*n+"\n"
    return res

def print_ruler(n):
    res=''
    if n==1:
        res="-"+"\n"
    else:
        res+=print_ruler(n-1)
        res+=n*"-"+"\n"
        res+=print_ruler(n-1)
    return res
#print(print_triangle(4))
#print(print_oposite_triangles(4))
#print(print_ruler(3))
