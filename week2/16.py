a=[]
while 1:
    n=int(input())
    if n==0:
        break
    a.append(n)
cnt=0
for i in range(1,len(a)-1):
    if a[i]>a[i-1] and a[i]>a[i+1]:
        cnt+=1
print(cnt)