n=int(input())
i=1
for i in range(n):
    for j in range(n-i):
        print("* ",end='')
    if(i==n-1):
        continue
    else:
        print()
for i in range(n+1):
    for j in range(i):
        print("* ",end='')
    print()
        
        
        
