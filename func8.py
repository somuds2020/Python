def Sum(x,y,*arg,**kwarg):
    """
    Usage of Sum
    x = <int>
    y = <int>
    etc.
    """
    print("x:",x)
    print("y:",y)
    print("arg:",arg)
    print("kwarg:",kwarg)
    print(x+y+arg[0]+kwarg["b"])

Sum(2,3,10,20,a=10,b=20,c=30)
print(Sum.__doc__)