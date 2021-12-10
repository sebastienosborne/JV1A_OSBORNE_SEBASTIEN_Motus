from colorama import init
init()

tentatives = 8
nbDeLettre = 6
#une fonction qui cherche une lettre dans un mot et renvoie sa position

import random
tableauMotus = ['pommes','orange','banane','citron','fraise','dattes','figues','poires','legume','cerise']
mot = "fruits"
print("Votre mot à ", len(mot), "letters")
while True:
    tentative = input("Entrer un mot:")
    if len(tentative) != len(mot): print("Entrer un mot avec", len(mot),"lettres")
    elif tentative == mot: break
    elif tentative != mot:
        for position, lettre in enumerate(tableauMotus):
            if lettre == mot[position]:
                print(lettre, end="")
            elif lettre not in mot:
                print("-", end="")
            else:
                print("?", end="")
        print("")
print("Bravo, vous avez deviné le mot!")

from colorama import Fore, Back, Style
print(Fore.RED + 'some red text')#Si bien placé
from colorama import Fore, Back, Style
print(Fore.Yellow + 'some red text')#Si présente
from colorama import Fore, Back, Style
print(Fore.BLUE + 'some red text')#Si Absente










    



