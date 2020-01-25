import random
class Coin:
    def __init__(self):
        self.sideup='Heads'
    def toss(self):
        if random.randint(0,1)==0:
            self.sideup='Heads'
        else:
            self.sideup='Tails'
    def get_sideup(self):
        return self.sideup
def main():
    c=Coin()
    print('This side is up:',c.get_sideup())
    print("I am tossing a coin...")
    c.toss()
    print('Now this side is up:',c.get_sideup())
    

main()

