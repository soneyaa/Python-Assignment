squad={'Batsmen':{'Rohit Sharma':{'Matches':206,'Runs':[8010,7089],'Average':47.89,'Highest Score':264},
                  'Virat Kohli':{'Matches':306,'Runs':[8010,7089,8907],'Average':80.89,'Highest Score':289},
                  'Ashish Sharma':{'Matches':250,'Runs':[2010,7989],'Average':77.89,'Highest Score':280}}}
#print(squad['Batsmen']['Virat Kohli']['Runs'][1])
p=[]
for i in squad:
    for j in squad[i]:
        if 'Highest Score' in squad[i][j]:
            p.append(squad[i][j]['Highest Score'])
#print(max(p))
count=0
q=[]
i=p.index(max(p))
for j in squad:
    for k in squad[j]:
        q.append(k)
#print(q)
for l in q:
        count+=1
        if i+1== count:
            print(l+":"+str(max(p)))
        
        

    





