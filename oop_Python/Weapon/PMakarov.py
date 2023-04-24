from Weapon import Weapon
class PMakarov(Weapon):
    bullet = 0
    def removeBullet(self,bullet):
        self.bullet -= bullet
    def sound(self):
        print("pach")

    def giveBullet(self,bullet):
        if((bullet =="all magazine")):
            self.bullet += 8
        else:
            print("it's Not my lovely full pm magazine")
    def isQuantity(self):
        if(self.bullet>4):
            print("I have enough bullets")
        else:
            print("Give me bullets")