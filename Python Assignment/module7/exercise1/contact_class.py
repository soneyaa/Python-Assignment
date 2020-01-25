class Contact:
    def __init__(self,p_name,p_no,email_add):
        self.p_name=p_name
        self.p_no=p_no
        self.email_add=email_add
    def get_name(self):
        return input('Enter The Name of The Person')
    def set_name(self):
        self.p_name=self.get_name()
        return self.p_name
    def get_phone(self):
        return input('Enter The Contact Number')
    def set_phone(self):
        self.p_no=self.get_phone()
        return self.p_no
    def get_email(self):
        return input('Enter The E-mail Id of The Person')
    def set_email(self):
        self.email_add=self.get_email()
        return self.email_add
    def __str__(self):
        return f'Person name : {self.p_name}\nPhone : {self.p_no}\nE-mail id : {self.email_add}\n'
def main():
        
    a=Contact('sonia','791312378','sonia1003namdev@gmail')
    while True:
        ch=input('Press 1 to Enter New Record.\nPress 2 to Update Record.\nEnter 3 to View Record.\nPress 0 to Exit.\n')
        if ch=='1':
            a.set_name()
            a.set_phone()
            a.set_email()
            print(a.__str__())
            p=input('Do You Want To Store this Record.\nPress 1 To Yes\nPress 2 To No')
            if p=='1':
                open_file=open('contact.txt','a')
                open_file.write(a.__str__())
                open_file.close()
                c=input('Do You Want TO View The Records.\nPress 1 To Yes.\nPress 0 To Exit.\n')
                if c=='1':
                    in_file=open('contact.txt','r')
                    print(in_file.read())
                    in_file.close()
                if ch=='0':
                    break
        elif ch=='2':
            k=input('Enter the person name You want to Update')
            file=open('contact.txt','r+')
            print(file.read())
        elif ch=='3':
             in_file=open('contact.txt','r')
             print(in_file.read())
             in_file.close()
            
            
            
        elif ch=='0':
            break
main()
