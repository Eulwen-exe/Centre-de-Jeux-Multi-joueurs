import random

def deviner_nombre_menu():
    menu = """
    1 - difficulté  facile (1 à 50)
    2 - difficulté moyen (1 à 100)
    3 - difficulté difficile (1 à 500)
    """
    try:
        difficulte = int(input(menu))
        if difficulte == 1:
            deviner_nombre(50)
        elif difficulte == 2:
            deviner_nombre(100)
        elif difficulte == 3:
            deviner_nombre(500)
    except ValueError:
        print("Erreur : vous devez entrer un nombre entier.")
 
def deviner_nombre(max):    
    chiffres = list(range(1, max+1))
    nombre_a_deviner = random.choice(chiffres)
    nombre_utilisateur = int(input(f"Saisi un nombre entre 1 et {max} : "))
    while not nombre_utilisateur == nombre_a_deviner:
        if nombre_utilisateur < nombre_a_deviner:
            print("Plus grand !")
        else:
            print("Plus petit !")
        nombre_utilisateur = int(input(f"Saisi un nombre entre 1 et {max} : "))
    print("Gagné !")
  
deviner_nombre_menu() 

