import random
import time
import msvcrt  # windows only

def calcul_mental_menu():
    menu = """
choisis la difficulté :
1 - facile (1 à 10)
2 - moyen (1 à 20)
3 - difficile (1 à 50)
"""
    try:
        difficulte = int(input(menu))
        if difficulte == 1:
            return 10
        elif difficulte == 2:
            return 20
        elif difficulte == 3:
            return 50
        else:
            print("choix invalide")
            return None
    except ValueError:
        print("entre un nombre valide")
        return None


def input_avec_timeout(prompt, limite=30):
    # saisie non bloquante + timeout
    debut = time.time()
    texte = ""

    while True:
        restant = limite - int(time.time() - debut)
        if restant <= 0:
            print(f"\r{prompt}{texte}   (0s) ")
            return None

        # affiche le prompt + texte tapé + temps restant
        print(f"\r{prompt}{texte}   ({restant}s) ", end="", flush=True)

        if msvcrt.kbhit():
            c = msvcrt.getwch()

            if c == "\r":  # entrée
                print()
                return texte
            elif c == "\b":  # backspace
                texte = texte[:-1]
            elif c in ("\x00", "\xe0"):  # touches spéciales (flèches, etc.)
                _ = msvcrt.getwch()
            else:
                texte += c

        time.sleep(0.05)


def calcul_mental(max_valeur):
    score = 0
    questions = 5
    temps_limite = 30

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


def main():
    max_valeur = calcul_mental_menu()
    if max_valeur is not None:
        calcul_mental(max_valeur)

main()
