import fighting
class color:
        PURPLE = '\033[95m'
        CYAN = '\033[96m'
        DARKCYAN = '\033[36m'
        BLUE = '\033[94m'
        GREEN = '\033[92m'
        YELLOW = '\033[93m'
        RED = '\033[91m'
        BOLD = '\033[1m'
        UNDERLINE = '\033[4m'
        ITALIC = '\x1B[3m'
        END = '\033[0m'
def leave():
        print("")
        print(color.ITALIC + "Du hast das Wirtshaus mit den Wachen verlassen und hast dich nun als Soldat seiner Majestät eingeschrieben. " + color.END)
def Tavern():
        print("")
        print(color.ITALIC + "Du hast dich entschieden noch im Wirtshaus zu bleiben und die Soldaten verlassen den Schankraum, um dich vor der Türe zu erwarten. " + color.END)
        print(color.ITALIC + "Aus dem Schatten der Taverne nähert sich dir nun eine Gestalt. " + color.END)
        print(color.ITALIC + "Sie kommt auf dich zu und sagt: " + color.END)
        print(color.BOLD + color.RED + "Du Bauer wagst es, dich hier im Gasthaus zu begnügen, während Dunkelheit das Reich bedroht?!?  " + color.END)
        print(color.ITALIC + "Du siehst die Gestalt einen Dolch zücken und auf dich zu kommen. Mit dem Befehl Kampf kannst du gegen ihn kämpfen, mit dem Befehl Flucht flüchtest du!  " + color.END)
        Action = input("Was tust du? ")
        while Action != "Flucht" and Action != "Kampf":
            Action = input(color.ITALIC + "Eure Eingabe war nicht korrekt, bitte passt sie an. " + color.END)
        if Action == "Flucht":
            leave()
        else:
            fighting.Kampf()#Benötigt noch Parameter --> auslagern?!?
        del(Action)



class Weapon:
        def __init__(self, name, weapontype, dammageboost):
                self.name = name
                self.weapontype = weapontype
                self.dammageboost = dammageboost
class Armor:
        def __init__(self, name, protection, dammageboost):
                self.name = name
                self.protection = protection
                self.dammageboost = dammageboost
class User:
        def __init__(self, fname, sname, age, rank, armor, armorvalue, weapon, weapontype, weaponvalue, lvl, money, items):
                self.sname = sname
                self.fname = fname
                self.age = age
                self.rank = rank
                self.lvl = lvl
                self.armor = armor
                self.armorvalue = armorvalue
                self.weapon = weapon
                self.weapontype = weapontype
                self.weaponvalue = weaponvalue
                self.money = money
                self.items = items
print("")
print("")
print("")
print(color.BOLD + color.GREEN + "Seid gegrüßt Abenteurer. " + color.END)
print("")
print(color.ITALIC + "Du erwachst in einer Taverne ohne zu Wissen, wie du hier her gekommen bist. Du schaust dich um und siehst hinter dir drei Ritter in Rüstung." + color.END)
print("")
Fname = input(color.BOLD + color.GREEN + "Wie nennt ihr euch? " + color.END)
Sname = input(color.BOLD + color.GREEN + "Und wie nennt sich eure Familie? " + color.END)
player = User(Fname, Sname, 20, "Bauer", "Lumpen", 1, "Mistgabel", "Nahkampf", 1, 1, 20, ["Brot", "Landkarte", "Beutel"] )
print("")
print(color.BOLD + color.GREEN + "Nun gut " + player.fname + ". Seid ihr bereit, in den Dienst des Königs zu treten? " + color.END)
print("")
print(color.ITALIC + "Wenn du mit den Wachen gehen willst, gebe leave ein, ansonsten tippe stay ein. " + color.END)
Dessision = input()
while Dessision != "leave" and Dessision != "stay":
        Dessision = input(color.ITALIC + "Eure Eingabe war nicht korrekt, bitte passt sie an. " + color.END)
if Dessision == "leave":
        leave()
else:
        print("Le")
        Tavern()
del(Dessision)





