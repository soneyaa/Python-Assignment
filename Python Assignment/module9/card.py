import random
class Card:   
    def __init__(self,face,suit,value):
        self.face=face
        self.suit=suit
        self.value=value
        
    def __str__(self):
        return f'{self.face} {self.suit} {self.value}'
        
class Deck:
    def __init__(self):
        a=''
    def shuffle(self,l):
        a=random.shuffle(l)
    def next_card(self):
        a=random.choice(l)
        print(a)
        return a
    def return_cards(self):
        return l
    def addCard(self,l,c):
        l.append(c)  

class Hand:
    def __init__(self):
        self.b=''
        self.l=l
        self.t=0
    def drawn_from(self,hc,d):        
        self.b=d.next_card()
        hc.append(self.b)
        l.remove(self.b)
        self.t=int(self.b.split()[2])
        return self.t
    def return_to(self):
        l.append(self.b)
        hc.remove(self.b)
        self.t=int(self.b.split()[2])
        return self.t

class Player:
    def __init__(self,credit):
        self.name=input("Enter your name")
        self.credit=credit
    def play(self):
        return(int(input("Do you want to play? Enter 1 for yes and 0 for no")))
    def show_hand(self,h):
        print("Cards in hand",h)
    def stand(self):
        pass
        
        
                

l=[]
hc=[]
t=0
d=Deck()


for i in ['Club','Diamond','Spade','Heart']:
    for j in range(2,11):
        c=Card('No',i,j)
        d.addCard(l,c.__str__())
for i in ['Club','Diamond','Spade','Heart']:
    for j in ['Jack','Queen','King','Ace']:
        if j=='Ace':
            v=1
        elif j=='King':
            v=13
        elif j=='Queen':
            v=12
        else:
            v=11
        c=Card(j,i,v)
        d.addCard(l,c.__str__())

p=Player(t)
h=Hand()

while(p.play()):
    d.shuffle(l)
    t+=h.drawn_from(hc,d)
    if(int(input("Do you want to return it back in deck? Enter 1 or 0"))):
        t-=h.return_to()       
        p.show_hand(hc)
    print(t)
    if t>21:
        print("Hurray!!! You won")
        t=0
