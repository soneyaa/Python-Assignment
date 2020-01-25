n=int(input("Enter number of rows:"))
i=0
for i in range(2*n+1):
    if(i==n):
        j=1
        for j in range(2*n+1):
            print("*",end=' ')
    else:
        for j in range(2*n):
            print(' ',end='')
        print('6*',end='')
    print()



  
