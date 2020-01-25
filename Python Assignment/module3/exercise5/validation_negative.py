f=1
while(f):
    w=input("Enter wholesale price")
    if('-' in w):
        continue
    retail=float(w)*0.5/100
    print('Retail= ',retail)
    print("Do you want to enter more values?..if yes press 1 and for no press 0")
    f=int(input())


