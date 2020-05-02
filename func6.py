def Sum(x,y,*arg): # arg is just a variable name
    print("x:",x)
    print("y:",y)
    print("arg:",arg)
    print(x+y+arg[::-1][0])

#~ Sum(2,3,4)
#~ Sum(2,3,4,5,6,789)
Sum(2,3,10,20,30)