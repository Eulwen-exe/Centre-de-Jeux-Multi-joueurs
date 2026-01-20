import random
import time
import msvcrt  # windows only

def calcul_mental_menu():
    """
    affiche le menu de difficulté du calcul mental et retourne la valeur max utilisée.
    """
    menu = """
choisis la difficulté :
1 - facile (1 à 10)
2 - moyen (1 à 20)
3 - difficile (1 à 50)
"""
    try:
        global difficulte_calcul_mental
        difficulte_calcul_mental = int(input(menu))
        if difficulte_calcul_mental == 1:
            return 10
        elif difficulte_calcul_mental == 2:
            return 20
        elif difficulte_calcul_mental == 3:
            return 50
        else:
            print("choix invalide")
            return None
    except ValueError:
        print("entre un nombre valide")
        return None


def input_avec_timeout(prompt, limite=30):
    """
    demande une saisie utilisateur avec un temps limite (windows only via msvcrt).

    paramètres :
        prompt (str) : texte affiché
        limite (int) : temps limite en secondes

    retourne :
        str | None : réponse saisie ou None si temps écoulé
    """
    debut = time.time()
    texte = ""
    while True:
        restant = limite - int(time.time() - debut)
        if restant <= 0:
            print(f"\r{prompt}{texte}   (0s) ")
            return None
        print(f"\r{prompt}{texte}   ({restant}s) ", end="", flush=True)
        if msvcrt.kbhit():
            c = msvcrt.getwch()
            if c == "\r":
                print()
                return texte
            elif c == "\b":
                texte = texte[:-1]
            elif c in ("\x00", "\xe0"):
                _ = msvcrt.getwch()
            else:
                texte += c
        time.sleep(0.05)


def calcul_mental(max_valeur):
    """
    lance une partie de calcul mental (5 questions), puis met à jour score/parties/succès.

    paramètre :
        max_valeur (int) : valeur max utilisée pour générer les nombres
    """
    prenom = input("Quel est votre prénom ? : ")
    compte = charger_profil(f"{prenom}.json")
    score = 0
    questions = 5
    temps_limite = 30
    succes_1 = "maitre du calcul débutant (mode facile)"
    succes_2 = "maitre du calcul vétéran (mode moyen)"
    succes_3 = "maitre du calcul ultime (mode difficile)"
    succes_4 = "gg (premiere victoire)"
    print("\nLe calcul mental a commencé ! (30s par question)\n")
    for i in range(questions):
        operation = random.choice(["+", "-", "*"])
        nombre_1 = random.randint(1, max_valeur)
        nombre_2 = random.randint(1, max_valeur)
        if operation == "-":
            if nombre_2 > nombre_1:
                nombre_1, nombre_2 = nombre_2, nombre_1
            resultat = nombre_1 - nombre_2
        elif operation == "+":
            resultat = nombre_1 + nombre_2
        else:
            resultat = nombre_1 * nombre_2
        prompt = f"question {i+1} : {nombre_1} {operation} {nombre_2} = "
        reponse = input_avec_timeout(prompt, temps_limite)
        if reponse is None:
            print("temps écoulé")
            print(f"faux, la bonne réponse était {resultat} !\n")
            continue
        if reponse.isdigit() and int(reponse) == resultat:
            print("juste !\n")
            score += 1
        else:
            print(f"faux, la bonne réponse était {resultat} !\n")
    print(f"Ton score final est de : {score}/{questions} !")
    if score == 0 and difficulte_calcul_mental == 1:
        compte["parties"] += 1
        compte["score_total"] += 0
    if score <= 2 and difficulte_calcul_mental == 1:
        compte["parties"] += 1
        compte["score_total"] += 25
    if score == 5 and difficulte_calcul_mental == 1:
        compte["parties"] += 1
        compte["score_total"] += 50
        if succes_1 not in compte["succes"]:
            compte["succes"].append(succes_1)
    if score <= 0 and difficulte_calcul_mental == 2:
        compte["parties"] += 1
        compte["score_total"] += 20
    if score <= 2 and difficulte_calcul_mental == 2:
        compte["parties"] += 1
        compte["score_total"] += 50
    if score == 5 and difficulte_calcul_mental == 2:
        compte["parties"] += 1
        compte["score_total"] += 100
        if succes_2 not in compte["succes"]:
            compte["succes"].append(succes_2)
    if score <= 0 and difficulte_calcul_mental == 3:
        compte["parties"] += 1
        compte["score_total"] += 20
    if score <= 2 and difficulte_calcul_mental == 3:
        compte["parties"] += 1
        compte["score_total"] += 150
    if score == 5 and difficulte_calcul_mental == 3:
        compte["parties"] += 1
        compte["score_total"] += 300
        if succes_3 not in compte["succes"]:
            compte["succes"].append(succes_3)
    elif succes_4 not in compte["succes"]:
        compte["succes"].append(succes_4)
    sauvegarder(f"{prenom}.json", compte)
    succes_jeu(f"{prenom}.json")

def main():
    max_valeur = calcul_mental_menu()
    if max_valeur is not None:
        calcul_mental(max_valeur)
