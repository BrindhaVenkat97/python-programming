a=int(input())
b=int(input())
if(a<=100000 and b<=100000):
  while(a!=b):
    if(a>b):
      a-=b
    else:
        b-=a
  print(a)
