from Weapon import Weapon
class AGS(Weapon):
    bullet = 0
    def removeBullet(self,bullet):
        self.bullet -= bullet
    def sound(self):
        print("piu piu")

    def giveBullet(self,bullet):
        if((bullet =="all magazine")):
            self.bullet += 16
        else:
            print("it's Not my lovely full Ags magazine")
    def isQuantity(self):
        if(self.bullet>8):
            print("I have enough bullets")
        else:
            print("Give me bullets")