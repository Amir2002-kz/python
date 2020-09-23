n=int(input())
if n==0:
    print(0)
elif n==1:
    print(1)
else:
    a=0
    b=1
    c=0
    cnt=2
    while 1:
        c=a+b
        a=b
        b=c
        cnt+=1
        if b>=n:
            break
        
    if n==b:
        print(cnt-1)
    else:
        print(-1)