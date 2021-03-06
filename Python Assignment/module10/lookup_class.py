import pickle
import tkinter as tk
from functools import partial     
window=tk.Tk()
window.geometry('400x400+200+300')  
window.title('Look Up') 
class Contact:
    def __init__(self,__name,__phone,__email):
        self.__name=__name
        self.__phone=__phone
        self.__email=__email
    def get_name(self):
        return self.__name
    def get_phone(self):
        return self.__phone
    def get_email(self):
        return self.__email
    def set_name(self,n):
        self.__name=n
    def set_phone(self,p):
        self.__phone=p
    def set_email(self,e):
        self.__email=e
    def __str__(self):
        return f'name : {self.__name} phonenumber : {self.__phone} emailaddress : {self.__email}'



o=open('contact.txt','rb')
b=pickle.load(o)
o.close()
m=1
for i in b:
   if i>m:
       m=i
q_=m
i=0
print(b)
def value(l,name,phone,email):
    global q_
    global b
    a=Contact((name.get()),(phone.get()),(email.get()))
    b[q_]=a
    q_+=1
    s="record num"+str(q_)+(name.get())+str((phone.get()))+(email.get())
    print(s)
    return
    
def NewRec():
    n = tk.StringVar()  
    p = tk.IntVar()  
    e=tk.StringVar()  
    labelNum1 = tk.Label(window, text="Enter name").grid(row=7)
    name = tk.Entry(window, textvariable=n).grid(row=8)
    labelNum2 = tk.Label(window, text="Enter phone").grid(row=9)
    phone = tk.Entry(window, textvariable=p).grid(row=10)
    labelNum2 = tk.Label(window, text="Enter email").grid(row=11)
    l = tk.Label(window).grid(row=15)
    email = tk.Entry(window, textvariable=e).grid(row=12)
    v = partial(value,l,n,p,e)  
    save = tk.Button(window, text="Save", command=v).grid(row=20)


def update(i,n,p,e):
   c=b[(i.get())]
   c.set_email((e.get()))
   c.set_phone((p.get()))
   c.set_name((n.get()))
   print(c.__str__())
    
def UpdateRec():
    n = tk.StringVar()  
    p = tk.IntVar()  
    i= tk.IntVar()  
    e=tk.StringVar()  
    l0= tk.Label(window, text="Enter RECORD number").grid(row=7,column=10)
    name = tk.Entry(window, textvariable=i).grid(row=8,column=10)
    labelNum1 = tk.Label(window, text="Enter name").grid(row=9,column=10)
    name = tk.Entry(window, textvariable=n).grid(row=10,column=10)
    labelNum2 = tk.Label(window, text="Enter phone").grid(row=11,column=10)
    phone = tk.Entry(window, textvariable=p).grid(row=12,column=10)
    labelNum2 = tk.Label(window, text="Enter email").grid(row=13,column=10)
    #l = tk.Label(window).grid(row=15,column=5)
    email = tk.Entry(window, textvariable=e).grid(row=14,column=10)
    u= partial(update,i,n,p,e)  
    save = tk.Button(window, text="Update", command=u).grid(row=20,column=10)
   
  
def ViewAllRec():
    #tk.Label(window,text=b[0].__str__).pack()
    global b
    global i
    for d in b:
        a=b[d].__str__()
        tk.Label(window,text=a).grid(row=14+i)
        i+=1
def show(i):
    a=(i.get())
    a=b[(i.get())].__str__()
    tk.Label(window,text=a).grid(row=17,column=1000)
    
def ViewRec():
    global b
    i= tk.IntVar()  
    l0= tk.Label(window, text="Enter RECORD number").grid(row=7,column=1000)
    recs = tk.Entry(window, textvariable=i).grid(row=8,column=1000)
    u= partial(show,i)  
    save = tk.Button(window, text="View", command=u).grid(row=20,column=1000)
    
def delet(i):
    a=(i.get())
    del b[(i.get())]
    
def DeleteRec():
    global b
    i= tk.IntVar()  
    l0= tk.Label(window, text="Enter RECORD number").grid(row=7,column=2000)
    recs = tk.Entry(window, textvariable=i).grid(row=8,column=2000)
    u= partial(delet,i)  
    save = tk.Button(window, text="Delete", command=u).grid(row=20,column=2000)
def DeleteAllRec():
    global b
    del b
    b={}

r = partial(NewRec)
tk.Button(window,text="Enter new record",command=r).grid(row=0)
s = partial(UpdateRec)
tk.Button(window,text="Update record",command=s).grid(row=1)  
t = partial(ViewAllRec)  
tk.Button(window,text="View all records",command=t).grid(row=2)   
u = partial(ViewRec)  
tk.Button(window,text="View a record",command=u).grid(row=3)
v = partial(DeleteRec)  
tk.Button(window,text="Delete a record",command=v).grid(row=4)  
w= partial(DeleteAllRec)  
tk.Button(window,text="Delete all records",command=w).grid(row=5) 
print()
o=open('contact.txt ','wb')
pickle.dump(b,o)
o.close()

window.mainloop()