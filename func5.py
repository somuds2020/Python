def product(x,y):
    print("x:",x)
    print("y:",y)
    print("OP:",str(x)+y)

#~ product(2,3)
#~ product(2,"abc")
#~ product("abc",2) # will not work due to position of 2nd argument
#~ product(x=2,y="abc")
#~ product(y="abc",x=2)
#~ product("abc",x=2)
product(2,y="abc")