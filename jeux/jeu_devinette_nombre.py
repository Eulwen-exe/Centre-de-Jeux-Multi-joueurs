from succes import *
from option_joueur import *
import random

def deviner_nombre_menu():
    """
    affiche un menu de difficulté pour deviner le nombre et lance la partie correspondante.
    """
    menu = """
    1 - difficulté  facile (1 à 50)
    2 - difficulté moyen (1 à 100)
    3 - difficulté difficile (1 à 500)
    """
    try:
        global difficulte_deviner_nombre
        difficulte_deviner_nombre = int(input(menu))
        if difficulte_deviner_nombre == 1:
            deviner_nombre(50)
        if difficulte_deviner_nombre == 2:
            deviner_nombre(100)
        if difficulte_deviner_nombre == 3:
            deviner_nombre(500)
    except ValueError:
        print("Erreur : vous devez entrer un nombre entier.")


def deviner_nombre(max):
    """
    lance une partie de devinette de nombre et met à jour score/parties/succès.

    paramètre :
        max (int) : valeur max du nombre à deviner
    """
    prenom = input("Quel est votre prénom ? : ")
    compte = charger_profil(f"{prenom}.json")
    succes_1 = "petit veinard (trouver le chiffre en moins de 5 essaies en mode facile)"
    succes_2 = "veinard (trouver le chiffre en moins de 8 essaies en mode moyen)"
    succes_3 = "veinard ultime (trouver le chiffre en moins de 15 essaies en mode difficile)"
    succes_4 = "gg (premiere victoire)"
    compteur = 0
    chiffres = list(range(1, max + 1))
    nombre_a_deviner = random.choice(chiffres)
    nombre_utilisateur = int(input(f"Saisi un nombre entre 1 et {max} : "))
    while not nombre_utilisateur == nombre_a_deviner:
        compteur += 1
        if nombre_utilisateur < nombre_a_deviner:
            print("Plus grand !")
        else:
            print("Plus petit !")
        nombre_utilisateur = int(input(f"Saisi un nombre entre 1 et {max} : "))
    print("Gagné !")
    if compteur <= 5 and difficulte_deviner_nombre == 1:
        compte["parties"] += 1
        compte["score_total"] += 50
        if succes_1 not in compte["succes"]:
            compte["succes"].append(succes_1)
    if compteur <= 10 and difficulte_deviner_nombre == 1:
        compte["parties"] += 1
        compte["score_total"] += 25
    if compteur > 10 and difficulte_deviner_nombre == 1:
        compte["parties"] += 1
        compte["score_total"] += 10
    if compteur <= 8 and difficulte_deviner_nombre == 2:
        compte["parties"] += 1
        if succes_2 not in compte["succes"]:
            compte["succes"].append(succes_2)
        compte["score_total"] += 100
    if compteur <= 15 and difficulte_deviner_nombre == 2:
        compte["parties"] += 1
        compte["score_total"] += 50
    if compteur > 15 and difficulte_deviner_nombre == 2:
        compte["parties"] += 1
        compte["score_total"] += 20
    if compteur <= 15 and difficulte_deviner_nombre == 3:
        compte["parties"] += 1
        compte["score_total"] += 500
        if succes_3 not in compte["succes"]:
            compte["succes"].append(succes_3)
    if compteur <= 25 and difficulte_deviner_nombre == 3:
        compte["parties"] += 1
        compte["score_total"] += 250
    if compteur > 25 and difficulte_deviner_nombre == 3:
        compte["parties"] += 1
        compte["score_total"] += 100
    elif succes_4 not in compte["succes"]:
        compte["succes"].append(succes_4)
    sauvegarder(f"{prenom}.json", compte)
    succes_jeu(f"{prenom}.json")

