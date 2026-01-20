from option_joueur import *
from succes import *
from regle import *
from jeu_chifumi import *
from jeu_calcul_mental import *
from jeu_devinette_nombre import *
from jeu_pendu import *

def menu():
    """
    menu principal du programme.
    """
    menu = """
    1 - creer un profil
    2 - voir profil d'un joueur
    3 - voir la liste des succès
    4 - règle des jeux
    5 - classement
    6 - jouer
    7 - Quitter
    """
    try:
        while True:
            temp = int(input(menu))
            if temp == 1:
                creer_profil()
            elif temp == 2:
                voir_profil_joueur()
            elif temp == 3:
                print(f"Voici la liste des succès : {liste_succes}")
            elif temp == 4:
                afficher_regle()
            elif temp == 5:
                classement()
            elif temp == 6:
                menu_jeu = """
                1 - jeu du pendu
                2- jeu de devinette du chiffre
                3 - jeu de calcul mental
                4 - jeu du pierre papier ciseau
                """
                jeu = int(input(menu_jeu))
                if jeu == 1:
                    jeu_pendu()
                elif jeu == 2:
                    deviner_nombre_menu()
                elif jeu == 3:
                    main()
                elif jeu == 4:
                    jeu_pierre_papier_ciseau()
                menu_fin = """
                1 - continuer de jouer
                2- arreter
                """
                continuer_jeu = int(input(menu_fin))
                if continuer_jeu == 1:
                    continue
                else:
                    print("Merci d'avoir joué !")
                    break
            elif temp == 7:
                print("Merci d'avoir joué !")
                break
    except ValueError:
        print("Erreur : vous devez entrer un nombre entier.")


menu()