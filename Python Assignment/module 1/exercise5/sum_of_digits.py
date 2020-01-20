print("Enter a 5 digit no.")
a=int(input())
s=0
while(a!=0):
    r=a%10
    s=s+r
    a=a//10
print(s)    

