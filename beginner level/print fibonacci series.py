x=int(input("enter the range"))
y=1
z=1
i=2
if(x<=0):
    print("wrong")
elif(x==1):
    print(x)
else:
    print(y)
    print(z)
    while(i<x):
        a=y+z
        print(a)
        y=z
        z=a
        i+=1
