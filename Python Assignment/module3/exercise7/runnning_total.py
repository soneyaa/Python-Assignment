n,m=map(int,input().split())
l=list(map(int,input().split()))
s=0
for i in range(n):
    if(i+m<=n):
        if s<sum(l[i:i+m]):
            s=sum(l[i:i+m])
    else:
        if s<(sum(l[i:])+sum(l[0:m+i-n])):
            s=sum(l[i:])+sum(l[0:m+i-n])
print(s)
