datastore={"office":{"medical":[
{"room-number":100,"use":"reception","sq-ft":50,"price":75},
{"room-number":101,"use":"waiting","sq-ft":250,"price":75},
{"room-number":102,"use":"examination","sq-ft":125,"price":150},
{"room-number":103,"use":"examination","sq-ft":125,"price":150},
{"room-number":104,"use":"office","sq-ft":150,"price":100}],
"parking":{"location":"premium","style":"covered","price":750}
}}

def printer(arg):
    if(arg=='M'):
      n=0
      for i in datastore['office']['medical']:
         print(n,".",i)
         n=n+1 
    if(arg=='P'):
      n=0
      for i,j in datastore['office']['parking'].items():
         print(n,".",i,":",j)
         n=n+1

def add(arg):
   if(arg=='M'):
      datastore['office']["medical"].append({"room-number":input("enter room number : "),"use":input("Enter use of room : "),"sq-ft":input("Enter sq-ft :"),"price":input("Enter price :")})
      printer(arg) 

 
   if(arg=='P'):
      datastore['office']['parking'][input("enter key: ")]=input("Enter value :")      
      printer(arg)

def update(arg):
   if(arg=='M'):
    choice=int(input("Enter 1 to change whole list or enter 2 to change a particular value-key pair of any List : "))
    if(choice==1):
      printer(arg)
      i=int(input("enter field to change : "))
      datastore['office']["medical"][i]={"room-number":input("enter room number : "),"use":input("Enter use of room : "),"sq-ft":input("Enter sq-ft :"),"price":input("Enter price :")}
      printer(arg)
    
    if(choice==2):
      printer(arg)
      i=int(input("enter field to change : "))
      k,j=map(str,input("enter key and value to update : ").split(" "))
      datastore['office']["medical"][i][k]=j
      printer(arg)
 
     

   if(arg=='P'):

    select=int(input("Enter 1 to change whole list or enter 2 to change a particular value-key pair of any List :"))
    if(select==1):
      printer(arg)
      for x in datastore['office']['parking']:
         val=input("enter value of  {0} : ".format(x))
         datastore['office']['parking'][x]=val
         printer(arg)

    if(select==2):
      printer(arg)
      k,j=map(str,input("enter key and value to update : ").split(" "))    
      datastore['office']["parking"][k]=j  
      printer(arg)

def delete(arg):
   if(arg=='M'):
    choice=int(input("Enter 1 to Delete whole list or enter 2 to Delete a particular value-key pair of any List : "))
    if(choice==1):
      printer(arg)
      i=int(input("enter field to delete : "))
      del(datastore['office']['medical'][i])       
      printer(arg)


    if(choice==2):
      printer(arg)
      i=int(input("enter field to delete : "))
      k=input("enter key to delete : ")
      del(datastore['office']['medical'][i][k]) 
      printer(arg)
      


   if(arg=='P'):
    select=int(input("Enter 1 to delete whole list or enter 2 to delete a particular value-key pair of any List :"))
    if(select==1):
      datastore['office']['parking'].clear()

      print(datastore['office']['parking'])

    if(select==2):
      printer(arg)
      k=input("enter key to delete : ")    
      del(datastore['office']["parking"][k])  
      printer(arg)
   

def main():
  while(True):
    print("1.ADD")
    print("2.UPDATE")
    print("3.DELETE")
    print("4.Exit")
    ch=int(input("Enter your choice : "))
    if(ch==1):
       print("Medical [M] or parking [P] -> ")
       c=input("Where you want to add : ")
       add(c)
    if(ch==2):
       print("Medical or parking-> ")
       c=input("Where you want to update : ")
       update(c)
    if(ch==3):
       print("Medical or parking-> ")
       c=input("Where you want to delete : ")       
       delete(c)  
    if(ch==4):
       exit()

main()
