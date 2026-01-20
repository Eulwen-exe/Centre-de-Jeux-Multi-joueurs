import random
import json
import time
import msvcrt  # windows only
from datetime import datetime
import os

profil = {"prenom": "",
          "date_creation": "",
          "parties": 0,
          "score_total": 0,
          "succes": []}

liste_succes = [
    ["gg (premiere victoire)"],
    ["apprentit puant (10 parties joués)"],
    ["puant ultime (50 parties joués)"],
    ["tryhardeur (atteindre les 1000 points)"],
    ["encore en vie ! (gagner au pendue)"],
    ["maitre du calcul débutant (mode facile)"],
    ["maitre du calcul vétéran (mode moyen)"],
    ["maitre du calcul ultime (mode difficile)"],
    ["petit veinard (trouver le chiffre en moins de 5 essaies en mode facile)"],
    ["veinard (trouver le chiffre en moins de 8 essaies en mode moyen)"],
    ["veinard ultime (trouver le chiffre en moins de 15 essaies en mode difficile)"]
]

regle_calcul = (
    "Regles du jeu Calcul Mental :\n"
    "- Vous devez resoudre un maximum d'operations en 30 secondes.\n"
    "- Les operations peuvent etre des additions, soustractions, multiplications ou divisions.\n"
    "- Chaque bonne reponse rapporte 1 point.\n"
    "- Le chrono demarre des la premiere question.\n"
    "- Le but est d'obtenir le meilleur score possible avant la fin du temps."
)

regle_devine = (
    "Regles du jeu Devine le Nombre :\n"
    "- Le but est de trouver le nombre choisi aleatoirement par l'ordinateur.\n"
    "- Vous choisissez un niveau de difficulte :\n"
    "    * Facile : nombre entre 1 et 10\n"
    "    * Moyen : nombre entre 1 et 100\n"
    "    * Difficile : nombre entre 1 et 500\n"
    "-A chaque tentative, l'ordinateur indique si le nombre est plus grand ou plus petit.\n"
    "- Vous gagnez lorsque vous trouvez le bon nombre."
)

regle_pendu = (
    "Trouvez le mot cache en proposant des lettres.\n "
    "Chaque erreur complete le dessin du pendu.\n "
    "Vous avez droit Ã 6 erreurs.\n "
    "Trouvez toutes les lettres avant la fin pour gagner.\n"
)


def afficher_regle():
    """
    affiche les règles des trois jeux (calcul mental, deviner le nombre, pendu).
    """
    print(regle_calcul)
    print(regle_devine)
    print(regle_pendu)


def sauvegarder(nom_fichier, dictionnaire):
    """
    sauvegarde un dictionnaire python dans un fichier json.

    paramètres :
        nom_fichier (str) : nom du fichier (ex: "leo.json")
        dictionnaire (dict) : données à enregistrer
    """
    with open(nom_fichier, "w", encoding="utf-8") as f:
        json.dump(dictionnaire, f, indent=4)


def charger_profil(nom_fichier):
    """
    charge un profil depuis un fichier json.

    paramètre :
        nom_fichier (str) : nom du fichier json à ouvrir

    retourne :
        dict : contenu du fichier json
    """
    with open(nom_fichier, "r", encoding="utf-8") as f:
        return json.load(f)


def voir_profil_joueur():
    """
    demande le prénom d'un joueur et affiche son profil depuis <prenom>.json.
    """
    nom_joueur = input("Saisi le nom du joueur dont tu veux voir le profil : ")
    profil_joueur = charger_profil(f"{nom_joueur}.json")
    print(profil_joueur)


def creer_profil():
    """
    crée un nouveau profil joueur.

    fonctionnement :
        - demande le prénom
        - crée le fichier <prenom>.json
        - initialise le profil et ajoute la date de création
        - sauvegarde le tout dans le fichier
    """
    prenom = input("Entrez votre prénom : ")
    with open(f"{prenom}.json", "x"):
        pass
    sauvegarder(f"{prenom}.json", profil)
    temp = charger_profil(f"{prenom}.json")
    temp["prenom"] = prenom
    temp["date_creation"] = datetime.now().strftime("%d/%m/%Y %H:%M")
    sauvegarder(f"{prenom}.json", temp)


def verifier_succes():
    """
    affiche la liste des succès du joueur.

    fonctionnement :
        - demande le prénom
        - charge <prenom>.json
        - affiche la liste profil["succes"]
    """
    nom = input("Quel est ton nom ? : ")
    profil_informations = charger_profil(f"{nom}.json")
    print(f"Voici tous tes succès : {profil_informations['succes']}")


def succes_jeu(nom_fichier):
    """
    ajoute automatiquement certains succès en fonction des stats du joueur.

    paramètres :
        nom_fichier (str) : fichier profil du joueur (ex: "leo.json")

    succès gérés ici :
        - 10 parties jouées
        - 50 parties jouées
        - 1000 points cumulés
    """
    profil_information = charger_profil(nom_fichier)
    succes_1 = "apprentit puant (10 parties joués)"
    succes_2 = "puant ultime (50 parties joués)"
    succes_3 = "tryhardeur (atteindre les 1000 points)"

    if succes_1 not in profil_information["succes"]:
        if profil_information["parties"] >= 10:
            profil_information["succes"].append(succes_1)

    if succes_2 not in profil_information["succes"]:
        if profil_information["parties"] >= 50:
            profil_information["succes"].append(succes_2)

    if succes_3 not in profil_information["succes"]:
        if profil_information["score_total"] >= 1000:
            profil_information["succes"].append(succes_3)

    sauvegarder(nom_fichier, profil_information)


def recupere_info_joueur():
    """
    récupère tous les profils (fichiers .json) présents dans le dossier courant.

    retourne :
        list[dict] : liste des profils trouvés
    """
    profils = []
    fichiers = os.listdir()
    for fichier in fichiers:
        if fichier.endswith(".json"):
            with open(fichier, "r", encoding="utf-8") as f:
                profil = json.load(f)
                profils.append(profil)
    return profils


def classement():
    """
    affiche un classement trié par score_total décroissant.
    """
    profils = recupere_info_joueur()
    profils.sort(key=lambda p: p["score_total"], reverse=True)
    for index, profil in enumerate(profils, start=1):
        print(index, profil["prenom"], ":", profil["score_total"])


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
    """
    retourne l'affichage du mot du pendu avec des '_' pour les lettres non trouvées.

    paramètres :
        mot (str) : mot secret
        lettres (list[str]) : lettres déjà trouvées

    retourne :
        str : affichage du mot (avec espaces)
    """
    return " ".join([l if l in lettres else "_" for l in mot])


def jeu_pendu():
    """
    lance une partie du pendu, met à jour le score, les parties et certains succès.
    """
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
        succes_1 = "gg (premiere victoire)"
        succes_2 = "encore en vie ! (gagner au pendue)"
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
                if succes_1 not in compte["succes"]:
                    compte["succes"].append(succes_1)
                if succes_2 not in compte["succes"]:
                    compte["succes"].append(succes_2)
                compte["parties"] += 1
                compte["score_total"] += 100
                sauvegarder(f"{prenom}.json", compte)
                succes_jeu(f"{prenom}.json")
                break
        else:
            print(pendu[erreur])
            print("Tu as perdu !")
            compte["parties"] += 1
            compte["score_total"] += 20
            sauvegarder(f"{prenom}.json", compte)
            succes_jeu(f"{prenom}.json")
    except ValueError:
        print("Erreur : vous devez entrer un nombre entier.")


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
    """
    lance le calcul mental : demande la difficulté puis démarre la partie.
    """
    max_valeur = calcul_mental_menu()
    if max_valeur is not None:
        calcul_mental(max_valeur)


def menu():
    """
    menu principal du programme.

    options :
        1 créer profil
        2 voir profil
        3 afficher liste des succès
        4 afficher règles
        5 classement
        6 jouer
        7 quitter
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
                2 - jeu de devinette du chiffre
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
                2 - arreter
                """
                continuer_jeu = int(input(menu_fin))
                if continuer_jeu == 1:
                    continue
                else:
                    break
            elif temp == 7:
                break
    except ValueError:
        print("Erreur : vous devez entrer un nombre entier.")


menu()
