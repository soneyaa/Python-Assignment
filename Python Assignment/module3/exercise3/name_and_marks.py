stu=input().split(',')
l=list(map(int,stu[1:]))
print(stu[0]+" obtained "+str(sum(l[0:5]))+" out of 500 in theory and "+str(sum(l[5:]))+" marks out of 150 in practical and successfully passed the exam with "+str("{0:.2f}".format((sum(l)*100/650))+" percentage,Many Many Congratulations!")
