fruits={'Apple':{'bionomical name':'Malus Domestica','Major Producers':['China','USA','Turkey'],'nutrition':{'carbohydrates':'13.81g','fat':'0.17g','protein':'6.26g'}}
,'Mango':{'bionomical name':'Mangifera Indica','Major Producers':['India','China','Arab'],'nutrition':{'carbohydrates':'14.61g','fat':'2.17g','protein':'5.26g'}}
,'Banana':{'bionomical name':'Bananica','Major Producers':['Russia','UN','Switzerland'],'nutrition':{'carbohydrates':'43.81g','fat':'0.07g','protein':'2.26g'}}}
p=[]
for i in fruits:
    for j in fruits[i]:
        if j=='nutrition':
            for k in fruits[i][j]:
                if k=='protein':
                    p.append(fruits[i][j][k])

i=p.index(max(p))
count=0
for j in fruits:
    if(i==count):
        print("The fruit with maximum protein value is "+j+" with protein "+max(p))
    count+=1
    
q=[]
for i in fruits:
    for j in fruits[i]:
        if j=='Major Producers':
            if "China" in fruits[i][j]:
                f=1
        if j=='nutrition' and f==1:
            for k in fruits[i][j]:
                if k=='protein':
                    q.append(fruits[i][j][k])

k=q.index(max(q))
count=0
for j in fruits:
    if(k==count):
        print("The fruit with major producer as China is "+j+" with protein "+max(q))
    count+=1
