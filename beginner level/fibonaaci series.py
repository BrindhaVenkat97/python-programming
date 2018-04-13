a=int(input("enter the range"))
b=1
c=1
i=2
if(a<=0):
    print("wrong")
elif(a==1):
    print(a)
else:
    print(b)
    print(c)
    while(i<a):
        d=b+c
        print(d)
        b=c
        c=d
        i+=1
