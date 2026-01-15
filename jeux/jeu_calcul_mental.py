import random

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
    
def calcul_mental(max):
    score = 0
    question = 5 
    
    print("Le calcul mental a commencé !")
    for nombre in range(question):
        operation = random.choice(["+","-","*"])
        nombre_1 = random.randint(1 , max)
        nombre_2 = random.randint(1, max)

        if operation == "-":
            if nombre_2 > nombre_1:
                nombre_1, nombre_2 = nombre_2, nombre_1
                resultat = nombre_1 - nombre_2
        elif operation == "+":
            resultat = nombre_1 + nombre_2
        else:
            resultat = nombre_1 * nombre_2
        
        try:
            reponse = (input(f"question {nombre+1} : {nombre_1} {operation} {nombre_2} = "))
        except ValueError:
            print("réponse invalide")
            reponse = None
        
        if reponse.isdigit() and int(reponse) == resultat:
            print("juste !")
            score += 1
        else:
            print(f"faux, la bonne réponse était {resultat} !")
        
    print(f"Ton score final est de : {score}/ {question} !")

def main():
    max = calcul_mental_menu()
    if max is not None:
        calcul_mental(max)
    
main()