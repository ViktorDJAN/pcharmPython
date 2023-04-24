from Weapon import Weapon
class GunMachineKalashnikow(Weapon):
    bullet = 0
    def removeBullet(self,bullet):
        self.bullet -= bullet
    def sound(self):
        print("ta tat ta ta")

    def giveBullet(self,bullet):
        if((bullet =="all magazine")):
            self.bullet += 120
        else:
            print("it's Not my lovely full machine magazine")
    def isQuantity(self):
        if(self.bullet>60):
            print("I have enough bullets")
        else:
            print("Give me bullets")
