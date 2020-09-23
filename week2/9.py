a=int(input())
b=int(input())
c=int(input())
d=int(input())
e=int(input())
f=int(input())
if (a>=d and b>=e and c>=f and a*b*c>d*e*f):
    print("second box can be covered")
elif(a<=d and b<=e and c<=f and a*b*c<d*e*f):
    print("first box can be covered ")
else:
    print("boxes are equal")