a=int(input(""))
b=len(str(a))
sum=0
temp=a
while(a>0):
    d=a%10
    sum+=d**b
    a//=10
if(temp==sum):
    print("armstrong number")
else:
    print("not armstrong number")
