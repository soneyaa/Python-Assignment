import pickle
class Details:
    def __init__(self,name):
        self.name=name
    def get_name(self):
        return self.name
    def get_phone(self):
        return self.phone
    def get_email(self):
        return self.email
    def get_address(self):
        return self.address
    def setName(self): 
        self.name = input('Enter the name here')
    def setPhone(self):
        self.phone=input('Enter the phone number here')
    def set_email(self):
        self.email=input('Enter the email here')
    def set_address(self):
        self.address=input('Enter the address here')
    def __str__(self):
        return f'User details are \nname: {self.name} \nphone: {self.ph_no}\n email: {self.email} \naddress: {self.address}\n'

def main():
    d=Details('sonia')
    p={}
    d=Details('dad ')
    d.setName()
    p['Name']=(d.get_name())
    d.setPhone()
    p['Phone']=(d.get_phone())
    d.set_email()
    p['Email']=(d.get_email())
    d.set_address()
    p['Address']=(d.get_address())
    print(p)
    f_o=open('contact.txt','wb')
    pickle.dump(p,f_o)
    f_o.close()
    f_i=open('contact.txt','rb')
    pickle.load(f_i)
    f_i.close()
             
    
    
main()

                                                                              
