from Weapon import Weapon
class AK47(Weapon):
    bullet = 0
    def removeBullet(self,bullet):
        self.bullet -= bullet
    def sound(self):
        print("piu piu")

    def giveBullet(self,bullet):
        if((bullet =="all magazine")):
            self.bullet += 30
        else:
            print("it's Not my lovely full AK magazine")
    def isQuantity(self):
        if(self.bullet>15):
            print("I have enough bullets")
        else:
            print("Give me bullets")
