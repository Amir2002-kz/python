n,m=map(int,input().split())
a=[]
b=[]
for i in range(n):
    a.append(0)
for i in range(m):
    x,y= map(int,input().split())
    b.append(x)
    b.append(y)
for i in range(0,len(b)-1,2):
    for j in  range(b[i],b[i+1]+1):
        a[j-1]=1
for i in a:
    if i==0:
        print("I",end="")
    else:
        print(".",end="")