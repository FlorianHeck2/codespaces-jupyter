from random import *
def NahkampfA(dammageboost, dammageboostArmor, Level): #Berechne den Angriffswert des Spielers (Wird gegen Rüstung gerechnet)
    basedammage = (int(dammageboost) + int(dammageboostArmor)) * (1+Level/10)
    Würfel = randint(0, 6)
    dammage = Würfel * basedammage
    return dammage

def VernkampfA(dammageboost, dammageboostArmor, Level): #Berechne den Angriffswert des Spielers (Wird gegen Rüstung gerechnet)
    basedammage = (int(dammageboost) + int(dammageboostArmor)) * (1+Level/10)
    Würfel = randint(0, 6)
    dammage = Würfel * basedammage
    return dammage



def PlayerAttack(weapontype, dammageboost, dammageboostArmor, Level):
    if weapontype == "Nahkampf":
        NahkampfA(dammageboost, dammageboostArmor, Level)
    else:
        VernkampfA(dammageboost, dammageboostArmor, Level)

def Kampf(weapontype, dammageboost, dammageboostArmor, Level):
    dead = False
    i = 1
    while dead != True:
        if i%2 == 1:
            PlayerAttack(weapontype, dammageboost, dammageboostArmor, Level)
