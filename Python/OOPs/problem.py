"""
warrior_name = 'Thor'
warrior_health = 100
warrior_attack = 50

mage_name = 'Gandalf'
mage_health = 80
mage_attack = 70

def attack_warrior():
    print(f"warrior attack with power",warrior_attack)

def attack_mage():
    print(f"mage attack with power",mage_attack)

attack_warrior()
attack_mage()"""

'''
Problems with the above code :
1.Redundant code
2.Hard to expand
3.No structure
'''

#solution of same problem using OOPs 

class Characters:
    def __init__(self,name,health,attack):
        self.name = name
        self.health = health
        self.attack = attack
    
    def attack_enemy(self):
        print(f"{self.name} attack with power {self.attack}")

warrior = Characters('Thor',100,50)
mage = Characters('Gandalf',80,70)

warrior.attack_enemy()
mage.attack_enemy()
