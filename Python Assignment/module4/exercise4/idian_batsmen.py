n=int(input("Enter the no of batsmen"))
batsmen={}
print()
for i in range(1,n+1):
    print("Enter the details of player:"+str(i))
    batsmen[i]={'type':input("type"),'name':input("name"),'matches':input("no.of matches played"),'runs':input("runs scored"),'average':input("average score"),'highest score':input('highest score')}
    print()
print(batsmen)

