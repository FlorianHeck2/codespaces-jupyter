import random

user = input("Gib bitte Schere, Stein oder Papier ein. ")
while user != "Schere" and user != "Stein" and user != "Papier":
    user = input("Gib bitte einen richtigen Wert ein! ")
possible_actions = ["Schere", "Stein", "Papier"]
comp = random.choice(possible_actions)
print('\033[92m' + "Der Spieler wählt " + user +'\033[91m' + " Der Computer wählt " + comp)
if user == comp:
    print('\033[0m'+"Unentschieden, ihr habt beide " + user + " gewählt.")
elif user == "Schere":
    if comp == "Stein":
        print('\033[91m' + "Der Computer gewinnt mit " + comp + " gegen " + user)
    else: print('\033[92m'+"Der Spieler gewinnt mit " + user + " gegen " + comp)
elif user == "Stein":
    if comp == "Papier":
        print('\033[91m' + "Der Computer gewinnt mit " + comp + " gegen " + user)
    else: print('\033[92m'+"Der Spieler gewinnt mit " + user + " gegen " + comp)
else:
    if comp == "Stein":
        print('\033[92m'+"Der Spieler gewinnt mit " + user + " gegen " + comp)
    else: print('\033[91m' + "Der Computer gewinnt mit " + comp + " gegen " + user)
print('\033[0m')