a=int(input("Enter a 5 digit number"))
s=0
while(a!=0):
    r=a%10
    s=s*10+r
    a//=10
print(s)
    
    
