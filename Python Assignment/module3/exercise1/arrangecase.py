str=input("Enter a string")
l=u=""
for char in str:
    if char.islower():
        l+=char
    elif char.isupper():
        u+=char
print(l+u)

        
        

        

    

