from AK47 import AK47
from PMakarov import PMakarov
from GunMachineKalashnikov import GunMachineKalashnikow
from AGS import AGS
ak = AK47("AK",3)
pm = PMakarov('PM',5)
gm = GunMachineKalashnikow('GUNMACHINE',25)
ags = AGS('GUNMACHINE',2)
print(" hello it's  ak47 ")
ak.sound()
ak.isQuantity()
ak.giveBullet("all magazine")
ak.removeBullet(12)
ak.isQuantity()
print()
print("hello it's PM")
pm.sound()
pm.isQuantity()
pm.giveBullet("all magazine")
pm.removeBullet(3)
pm.isQuantity()
print()
print("hello it's GM")
gm.sound()
gm.isQuantity()
gm.giveBullet("all magazine")
gm.removeBullet(45)
gm.isQuantity()
print()
print("hello it's ags")
ags.sound()
ags.isQuantity()
ags.giveBullet("10")
ags.removeBullet(5)
ags.isQuantity()



