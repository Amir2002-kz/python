p = True
mn=10e6
l=[]
cnt=0
while p:
    a=int(input())
    if a==0:
        break
    if(a<=mn):
        mn=a
        l.append(mn)
for i in l:
    if i==mn:
        cnt+=1
print(cnt)