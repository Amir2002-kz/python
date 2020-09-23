n=int(input())
a=list(map(int,input().split()))
cnt=0
b=[]
for i in range(len(a)):
    for j in  range(len(a)):
        if i!=j and  a[i]==a[j]:
            cnt+=1
    b.append(cnt)
    cnt=0
for i in b:
    cnt+=i
t =int(cnt/2)
print(t)