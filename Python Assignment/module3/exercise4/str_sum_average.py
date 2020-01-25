s=input().split(" ")
l=[int(s[i]) for i in range(2,len(s),3)]
print("sum ",sum(l)," Percentage ",round(sum(l)/len(l),2))
