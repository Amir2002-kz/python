n=int(input())
m=int(input())
x=int(input())
a=list()
a.append(n)
a.append(m)
a.append(x)

a.sort()
for x in a:
    print(x,end=" ")