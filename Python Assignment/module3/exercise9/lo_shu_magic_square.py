def isMagicSquare( mat) : 
    diagonal1= 0
    for i in range(0, N) :
        diagonal1 = diagonal1 + mat[i][i] 
  
    diagonal2= 0
    for i in range(0, N) : 
        diagonal2 = diagonal2 + mat[i][N-i-1] 
  
    if(diagonal1!=diagonal2) : 
        return False
  

    for i in range(0, N) : 
        rowSum = 0;      
        for j in range(0, N) : 
            rowSum += mat[i][j] 

        if (rowSum != diagonal1) : 
            return False

    for i in range(0, N): 
        colSum = 0
        for j in range(0, N) : 
            colSum += mat[j][i] 
        if (diagonal1!= colSum) : 
            return False
  
    return True
N=int(input('Enter the order of matrix'))
mat=[]
print('Elements of matrix') 
for i in range(N):
    mat.append([int(j) for j in input().split()])
      
if (isMagicSquare(mat)) : 
    print( "Magic Square") 
else : 
    print( "Not a magic Square")
