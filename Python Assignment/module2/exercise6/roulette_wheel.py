p=int(input("Enter the pocket number"))
if p>36:
    print("Error! The pocket number is out of range")
else:
    if p==0:
        print("Pocket is GREEN")
    elif p>=1 and p<=10:
        if p%2==0:
            print("Pocket is BLACK")
        else:
            print("Pocket is RED")
    elif p>=11 and p<=18:
        if p%2==0:
            print("Pocket is RED")
        else:
            print("Pocket is BLACK")
    elif p>=19 and p<=28:
        if p%2==0:
            print("Pocket is BLACK")
        else:
            print("Pocket is RED")
    elif p>=29 and p<=36:
        if p%2==0:
            print("Pocket is RED")
        else:
            print("Pocket is BLACK")     
    
   
        
