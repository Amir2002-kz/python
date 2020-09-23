n=int(input())
m=int(input())
x=int(input())
y=int(input())
t=0
o=0
if x>n/2:
    t=n-x
else: t=x

if y>m/2:
    o=m-y
else:  o=y
if t>o:
    print(o)
else:
    print(t)