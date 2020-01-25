def countPairs(N1,N2,s):
    c=0
    for i in N1:
        if s-i in N2:
            c+=N2.count(s-i)
    return c       
    

N1=list(map(int,input("Enter elements of list1").split()))
N2=list(map(int,input("Enter elements of list2").split()))
s=int(input("Enter sum"))
print(countPairs(N1,N2,s))
