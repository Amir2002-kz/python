def check(a1,b1,a2,b2):
    if  abs(a1-a2)==0 or abs(b1-b2)==0:
        return "YES" 
    else: return "NO"

a1=int(input())
b1=int(input())
a2=int(input())
b2=int(input())
print(check(a1,b1,a2,b2))