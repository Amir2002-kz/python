a=[100,50,25,10,5,2,1]
ans=0
sums=int(input())
for i in range(0,len(a)):
    ans+=int(sums/a[i])
    sums%=a[i]
print(ans)