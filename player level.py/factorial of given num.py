x=int(input(""))
y=1
if(x==0):
    print("1")
else:
    while(x>0):
        y=x*y
        x-=1
    print(y)
