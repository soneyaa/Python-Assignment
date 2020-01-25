matrix=[[j for j in range(5)]for i in range(5)]
print(matrix)
flatten_matrix=[val for sublist in matrix for val in sublist]
print(flatten_matrix)
print()

matrix=[[j for j in range(10)]for i in range(5)]
print(matrix)
print()
flatten_even=[val for sublist in matrix for val in sublist if val%2==0]
print(flatten_even)
