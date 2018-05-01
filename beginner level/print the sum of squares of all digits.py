a=int(input(""))
sum=0
while(a>0):
    d=a%10
    sum+=d**2
    a//=10
print(sum)
