def Sum(x,y,**kwarg): # kwarg is just a variable name
    print("x:",x)
    print("y:",y)
    print("kwarg:",kwarg)
    print(x+y+kwarg["b"])

Sum(2,3,a=10,b=20,c=30)