import random
import json
import time
import msvcrt  # windows only


profil = {"prenom": "",
          "date_creation":"",
          "parties": 0,
          "score_total": 0,
          "succes": ""}


def sauvegarder(nom_fichier, dictionnaire):
    with open(nom_fichier, "w", encoding="utf-8") as f:
        json.dump(dictionnaire, f, indent=4)
        
 
def charger_profil(nom_fichier):
    with open(nom_fichier, "r", encoding="utf-8") as f:
        return json.load(f)
    
def voir_profil_joueur():
    nom_joueur = input("Saisi le nom du joueur dont tu veux voir le profil : ")
    profil_joueur = charger_profil(f"{nom_joueur}.json")
    print(profil_joueur)
    
    
def creer_profil():
    prenom = input("Entrez votre prénom : ")
    with open(f"{prenom}.json", "x") as f:
        f.close()
    sauvegarder(f"{prenom}.json", profil)
    temp = charger_profil(f"{prenom}.json")
    temp["prenom"] = prenom
    sauvegarder(f"{prenom}.json", temp)
    

def verifier_succes(nom_fichier):
    profil = charger_profil(nom_fichier)
    print(f"Voici tous tes succès : {profil["succes"]}")
    

def calculer_points(nom_fichier):
    profil = charger_profil(nom_fichier)
    print(f"Voici tous tes succès : {profil["succes"]}")
    
    
theme_pendu = [
[
    "chien", "chat", "lion", "tigre", "elephant", "girafe", "singe", "lapin",
    "cheval", "loup", "ours", "renard", "requin", "dauphin", "serpent", "aigle",
    "hibou", "panda", "koala", "kangourou", "zebre", "rhinoceros", "hippopotame",
    "crocodile", "alligator", "panthere", "leopard", "guepard", "baleine",
    "phoque", "otarie", "tortue", "pingouin", "manchot", "corbeau", "perroquet",
    "moineau", "souris", "rat", "hamster", "ecureuil", "herisson", "blaireau",
    "sanglier", "cerf", "biche", "chamois", "bouquet"
],


[
    "pizza", "hamburger", "fromage", "pates", "riz", "poulet", "boeuf", "porc",
    "poisson", "chocolat", "gateau", "pomme", "banane", "fraise", "orange",
    "raisin", "poire", "ananas", "mangue", "pasteque", "salade", "tomate",
    "carotte", "brocoli", "courgette", "aubergine", "oignon", "ail", "pain",
    "baguette", "croissant", "sandwich", "soupe", "glace", "yaourt", "beurre",
    "creme", "lait", "oeuf", "omelette", "lasagne", "tacos", "kebab", "sushi",
    "ramen", "couscous", "paella", "quiche", "gratin"
],


[
    "france", "espagne", "italie", "allemagne", "portugal", "belgique",
    "suisse", "autriche", "pologne", "grece", "suede", "norvege", "finlande",
    "danemark", "irlande", "royaumeuni", "islande", "canada", "etatsunis",
    "mexique", "bresil", "argentine", "chili", "perou", "colombie", "venezuela",
    "japon", "chine", "coree", "vietnam", "thailande", "inde", "pakistan",
    "nepal", "indonesie", "australie", "nouvellezelande", "egypte", "maroc",
    "algerie", "tunisie", "senegal", "nigeria", "kenya", "ethiopie",
    "afriquedusud", "turquie", "israel", "iran"
],


[
    "ordinateur", "clavier", "souris", "ecran", "serveur", "reseau", "internet",
    "logiciel", "programme", "algorithme", "donnees", "base", "python", "java",
    "javascript", "html", "css", "sql", "linux", "windows", "macos", "processeur",
    "memoire", "disque", "stockage", "cloud", "securite", "parefeu", "cryptage",
    "hash", "motdepasse", "authentification", "api", "backend", "frontend",
    "framework", "bibliotheque", "debug", "compilation", "virtualisation",
    "conteneur", "docker", "git", "github", "commit", "branche", "merge",
    "bug", "latence"
],


[
    "medecin", "enseignant", "ingenieur", "developpeur", "pompier", "policier",
    "avocat", "boulanger", "cuisinier", "journaliste", "architecte", "infirmier",
    "chirurgien", "dentiste", "pharmacien", "psychologue", "psychiatre",
    "electricien", "plombier", "menuisier", "charpentier", "maçon", "peintre",
    "decorateur", "designer", "graphiste", "photographe", "videaste",
    "realisateur", "acteur", "musicien", "compositeur", "chanteur", "professeur",
    "chercheur", "scientifique", "technicien", "administrateur", "analyste",
    "consultant", "comptable", "auditeur", "economiste", "banquier",
    "assureur", "courtier", "vendeur", "commercial", "manager"
],


[
    "table", "chaise", "lampe", "telephone", "sac", "stylo", "cahier", "montre",
    "cle", "porte", "bouteille", "lunettes", "ordinateur", "telecommande",
    "television", "radio", "horloge", "miroir", "canape", "fauteuil", "lit",
    "oreiller", "couverture", "tapis", "rideau", "fenetre", "etagere", "armoire",
    "tiroir", "placard", "four", "microonde", "refrigerateur", "congelateur",
    "mixeur", "grillepain", "bouilloire", "aspirateur", "balai", "serpillere",
    "seau", "marteau", "tournevis", "perceuse", "scie", "clou", "vis",
    "chargeur", "batterie"
]
]
theme_pendu = [
[
    "chien", "chat", "lion", "tigre", "elephant", "girafe", "singe", "lapin",
    "cheval", "loup", "ours", "renard", "requin", "dauphin", "serpent", "aigle",
    "hibou", "panda", "koala", "kangourou", "zebre", "rhinoceros", "hippopotame",
    "crocodile", "alligator", "panthere", "leopard", "guepard", "baleine",
    "phoque", "otarie", "tortue", "pingouin", "manchot", "corbeau", "perroquet",
    "moineau", "souris", "rat", "hamster", "ecureuil", "herisson", "blaireau",
    "sanglier", "cerf", "biche", "chamois", "bouquet"
],


[
    "pizza", "hamburger", "fromage", "pates", "riz", "poulet", "boeuf", "porc",
    "poisson", "chocolat", "gateau", "pomme", "banane", "fraise", "orange",
    "raisin", "poire", "ananas", "mangue", "pasteque", "salade", "tomate",
    "carotte", "brocoli", "courgette", "aubergine", "oignon", "ail", "pain",
    "baguette", "croissant", "sandwich", "soupe", "glace", "yaourt", "beurre",
    "creme", "lait", "oeuf", "omelette", "lasagne", "tacos", "kebab", "sushi",
    "ramen", "couscous", "paella", "quiche", "gratin"
],


[
    "france", "espagne", "italie", "allemagne", "portugal", "belgique",
    "suisse", "autriche", "pologne", "grece", "suede", "norvege", "finlande",
    "danemark", "irlande", "royaumeuni", "islande", "canada", "etatsunis",
    "mexique", "bresil", "argentine", "chili", "perou", "colombie", "venezuela",
    "japon", "chine", "coree", "vietnam", "thailande", "inde", "pakistan",
    "nepal", "indonesie", "australie", "nouvellezelande", "egypte", "maroc",
    "algerie", "tunisie", "senegal", "nigeria", "kenya", "ethiopie",
    "afriquedusud", "turquie", "israel", "iran"
],


[
    "ordinateur", "clavier", "souris", "ecran", "serveur", "reseau", "internet",
    "logiciel", "programme", "algorithme", "donnees", "base", "python", "java",
    "javascript", "html", "css", "sql", "linux", "windows", "macos", "processeur",
    "memoire", "disque", "stockage", "cloud", "securite", "parefeu", "cryptage",
    "hash", "motdepasse", "authentification", "api", "backend", "frontend",
    "framework", "bibliotheque", "debug", "compilation", "virtualisation",
    "conteneur", "docker", "git", "github", "commit", "branche", "merge",
    "bug", "latence"
],


[
    "medecin", "enseignant", "ingenieur", "developpeur", "pompier", "policier",
    "avocat", "boulanger", "cuisinier", "journaliste", "architecte", "infirmier",
    "chirurgien", "dentiste", "pharmacien", "psychologue", "psychiatre",
    "electricien", "plombier", "menuisier", "charpentier", "maçon", "peintre",
    "decorateur", "designer", "graphiste", "photographe", "videaste",
    "realisateur", "acteur", "musicien", "compositeur", "chanteur", "professeur",
    "chercheur", "scientifique", "technicien", "administrateur", "analyste",
    "consultant", "comptable", "auditeur", "economiste", "banquier",
    "assureur", "courtier", "vendeur", "commercial", "manager"
],


[
    "table", "chaise", "lampe", "telephone", "sac", "stylo", "cahier", "montre",
    "cle", "porte", "bouteille", "lunettes", "ordinateur", "telecommande",
    "television", "radio", "horloge", "miroir", "canape", "fauteuil", "lit",
    "oreiller", "couverture", "tapis", "rideau", "fenetre", "etagere", "armoire",
    "tiroir", "placard", "four", "microonde", "refrigerateur", "congelateur",
    "mixeur", "grillepain", "bouilloire", "aspirateur", "balai", "serpillere",
    "seau", "marteau", "tournevis", "perceuse", "scie", "clou", "vis",
    "chargeur", "batterie"
]
]

pendu = [
    """
     +---+
     |   |
         |
         |
         |
         |
    =========
    """,
    """
     +---+
     |   |
     O   |
         |
         |
         |
    =========
    """,
    """
     +---+
     |   |
     O   |
     |   |
         |
         |
    =========
    """,
    """
     +---+
     |   |
     O   |
    /|   |
         |
         |
    =========
    """,
    """
     +---+
     |   |
     O   |
    /|\  |
         |
         |
    =========
    """,
    """
     +---+
     |   |
     O   |
    /|\  |
    /    |
         |
    =========
    """,
    """
     +---+
     |   |
     O   |
    /|\  |
    / \  |
         |
    =========
    """
]

def afficher_mot(mot, lettres):
    return " ".join([l if l in lettres else "_" for l in mot])


def jeu_pendu():
    prenom = input("Quel est votre prénom ? : ")
    compte = charger_profil(f"{prenom}.json")
    menu = """
    1 - animaux
    2 - nourriture
    3 - pays
    4 - informatique
    5 - metiers
    6 - objets
    """
    try:
        index = int(input(menu))
        theme = theme_pendu[index - 1]
        mot_secret = random.choice(theme)
        lettre_trouve = []
        erreur = 0
        erreur_max = 6
        while erreur < erreur_max:
            print(f"Mot : {afficher_mot(mot_secret, lettre_trouve)}")
            lettre = input("Choisis une lettre : ")
            print(f"Lettre proposé : {lettre}")
            if lettre in lettre_trouve:
                print("Tu as déjà trouvé cette lettre")
                continue
            if lettre in mot_secret:
                lettre_trouve.append(lettre)
                print("Tu as trouvé une lettre !")
            else:
                print("La lettre n'est pas dans le mot")
                print(pendu[erreur])
                erreur += 1
            if "_" not in afficher_mot(mot_secret, lettre_trouve):
                print("tu as gagné !")
                compte["parties"] += 1
                compte["score_total"] += 100
                sauvegarder(f"{prenom}.json", compte)
                break
        else:
            print(pendu[erreur])
            print("Tu as perdu !")
            compte["parties"] += 1
            compte["score_total"] += 20
            sauvegarder(f"{prenom}.json", compte)
    except ValueError:
        print("Erreur : vous devez entrer un nombre entier.")


def deviner_nombre_menu():
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
        elif difficulte_deviner_nombre == 2:
            deviner_nombre(100)
        elif difficulte_deviner_nombre == 3:
            deviner_nombre(500)
    except ValueError:
        print("Erreur : vous devez entrer un nombre entier.")
 
def deviner_nombre(max):
    prenom = input("Quel est votre prénom ? : ")
    compte = charger_profil(f"{prenom}.json")
    compteur = 0
    chiffres = list(range(1, max+1))
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
        sauvegarder(f"{prenom}.json", compte)
    if compteur <= 10 and difficulte_deviner_nombre == 1:
        compte["parties"] += 1
        compte["score_total"] += 25
        sauvegarder(f"{prenom}.json", compte)
    if compteur > 10 and difficulte_deviner_nombre == 1:
        compte["parties"] += 1
        compte["score_total"] += 10
        sauvegarder(f"{prenom}.json", compte)
    if compteur <= 8 and difficulte_deviner_nombre == 2:
        compte["parties"] += 1
        compte["score_total"] += 100
        sauvegarder(f"{prenom}.json", compte)
    if compteur <= 15 and difficulte_deviner_nombre == 2:
        compte["parties"] += 1
        compte["score_total"] += 50
        sauvegarder(f"{prenom}.json", compte)
    if compteur > 15 and difficulte_deviner_nombre == 2:
        compte["parties"] += 1
        compte["score_total"] += 20
        sauvegarder(f"{prenom}.json", compte)
    if compteur <= 15 and difficulte_deviner_nombre == 3:
        compte["parties"] += 1
        compte["score_total"] += 500
        sauvegarder(f"{prenom}.json", compte)
    if compteur <= 25 and difficulte_deviner_nombre == 3:
        compte["parties"] += 1
        compte["score_total"] += 250
        sauvegarder(f"{prenom}.json", compte)
    if compteur > 25 and difficulte_deviner_nombre == 3:
        compte["parties"] += 1
        compte["score_total"] += 100
        sauvegarder(f"{prenom}.json", compte)


def calcul_mental_menu():
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
    prenom = input("Quel est votre prénom ? : ")
    compte = charger_profil(f"{prenom}.json")
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
    if score == 0 and difficulte_calcul_mental == 1:
        compte["parties"] += 1
        compte["score_total"] += 0
        sauvegarder(f"{prenom}.json", compte)
    if score <= 5 and difficulte_calcul_mental == 1:
        compte["parties"] += 1
        compte["score_total"] += 25
        sauvegarder(f"{prenom}.json", compte)
    if score == 10 and difficulte_calcul_mental == 1:
        compte["parties"] += 1
        compte["score_total"] += 50
        sauvegarder(f"{prenom}.json", compte)
    if score <= 5 and difficulte_calcul_mental == 2:
        compte["parties"] += 1
        compte["score_total"] += 20
        sauvegarder(f"{prenom}.json", compte)
    if score <= 14 and difficulte_calcul_mental == 2:
        compte["parties"] += 1
        compte["score_total"] += 50
        sauvegarder(f"{prenom}.json", compte)
    if score == 20 and difficulte_calcul_mental == 2:
        compte["parties"] += 1
        compte["score_total"] += 100
        sauvegarder(f"{prenom}.json", compte)
    if score <= 15 and difficulte_calcul_mental == 3:
        compte["parties"] += 1
        compte["score_total"] += 50
        sauvegarder(f"{prenom}.json", compte)
    if score <= 35 and difficulte_calcul_mental == 3:
        compte["parties"] += 1
        compte["score_total"] += 400
        sauvegarder(f"{prenom}.json", compte)
    if score == 50 and difficulte_calcul_mental == 3:
        compte["parties"] += 1
        compte["score_total"] += 750
        sauvegarder(f"{prenom}.json", compte)


def main():
    max_valeur = calcul_mental_menu()
    if max_valeur is not None:
        calcul_mental(max_valeur)
        
def menu():
    menu = """
    1 - creer un profil
    2 - voir profil d'un joueur
    3 - jouer
    """
    try:
        while True:
            temp = int(input(menu))
            if temp == 1:
                creer_profil()
            elif temp == 2:
                voir_profil_joueur()
            elif temp == 3:
                menu_jeu = """
                1 - jeu du pendu
                2- jeu de devinette du chiffre
                3 - jeu de calcul mental
                """
                jeu = int(input(menu_jeu))
                if jeu == 1:
                    jeu_pendu()
                elif jeu == 2:
                    deviner_nombre_menu()
                elif jeu == 3:
                    main() 
                menu_fin = """
                1 - continuer de jouer
                2- arreter
                """
                continuer_jeu = int(input(menu_fin))
                if continuer_jeu == 1:
                    continue
                else:
                    break
    except ValueError:
        print("Erreur : vous devez entrer un nombre entier.")